#!/usr/bin/env python3
"""Додає thelobbyx.com до списку дозволених доменів розширення Claude-in-Chrome"""

import struct
import json
import os
import uuid
import time
import sys

EXTENSION_ID = "fcoeoabgfenejglbffodgkkbkcdhcgfn"
PROFILE_PATH = r"C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile 1"
STORAGE_PATH = os.path.join(PROFILE_PATH, "Local Extension Settings", EXTENSION_ID)

LDB_FILE   = os.path.join(STORAGE_PATH, "000016.ldb")
LOG_FILE   = os.path.join(STORAGE_PATH, "000014.log")
MANIFEST_F = os.path.join(STORAGE_PATH, "MANIFEST-000001")

# ── CRC32c (Castagnoli) ──────────────────────────────────────────────────────

def _make_crc32c_table():
    poly = 0x82F63B78
    t = []
    for i in range(256):
        crc = i
        for _ in range(8):
            crc = (crc >> 1) ^ poly if crc & 1 else crc >> 1
        t.append(crc)
    return t

_CRC_TABLE = _make_crc32c_table()

def crc32c(data: bytes) -> int:
    crc = 0xFFFFFFFF
    for b in data:
        crc = (crc >> 8) ^ _CRC_TABLE[(crc ^ b) & 0xFF]
    return crc ^ 0xFFFFFFFF

def mask_crc(crc: int) -> int:
    return (((crc >> 15) | (crc << 17)) + 0xa282ead8) & 0xFFFFFFFF

# ── Varint ───────────────────────────────────────────────────────────────────

def encode_varint32(n: int) -> bytes:
    out = bytearray()
    while n >= 0x80:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    out.append(n)
    return bytes(out)

def put_len_prefixed(s) -> bytes:
    b = s.encode('utf-8') if isinstance(s, str) else bytes(s)
    return encode_varint32(len(b)) + b

# ── Читання last_sequence з MANIFEST ─────────────────────────────────────────

def decode_varint(data: bytes, pos: int):
    r, shift = 0, 0
    while pos < len(data):
        b = data[pos]; pos += 1
        r |= (b & 0x7F) << shift
        if not (b & 0x80):
            return r, pos
        shift += 7
    return r, pos

def read_last_sequence(manifest_path: str) -> int:
    try:
        with open(manifest_path, 'rb') as f:
            data = f.read()
        last_seq = 0
        pos = 0
        while pos + 7 <= len(data):
            _crc    = struct.unpack_from('<I', data, pos)[0]
            length  = struct.unpack_from('<H', data, pos + 4)[0]
            _rtype  = data[pos + 6]
            pos += 7
            if pos + length > len(data):
                break
            rec = data[pos:pos + length]
            pos += length
            i = 0
            while i < len(rec):
                try:
                    tag, i = decode_varint(rec, i)
                    if tag == 4:      # kLastSequence
                        val, i = decode_varint(rec, i)
                        last_seq = max(last_seq, val)
                    elif tag == 1:    # kComparatorName — рядок
                        slen, i = decode_varint(rec, i); i += slen
                    elif tag in (2, 3, 9):  # kLogNumber / kNextFileNumber / kPrevLogNumber
                        _, i = decode_varint(rec, i)
                    elif tag == 5:    # kCompactPointer
                        _, i = decode_varint(rec, i)
                        slen, i = decode_varint(rec, i); i += slen
                    elif tag == 6:    # kDeletedFile
                        _, i = decode_varint(rec, i)
                        _, i = decode_varint(rec, i)
                    elif tag == 7:    # kNewFile
                        _, i = decode_varint(rec, i)
                        _, i = decode_varint(rec, i)
                        _, i = decode_varint(rec, i)
                        slen, i = decode_varint(rec, i); i += slen
                        slen, i = decode_varint(rec, i); i += slen
                    else:
                        break
                except Exception:
                    break
        return last_seq
    except Exception as e:
        print(f"  Попередження: не вдалось прочитати MANIFEST: {e}")
        return 0

# ── Читання поточного JSON з SSTable ─────────────────────────────────────────

def read_permissions_json(ldb_path: str) -> dict:
    with open(ldb_path, 'rb') as f:
        data = f.read()
    pos = data.find(b'{"rules":[')
    if pos == -1:
        pos = data.find(b'{"rules": [')
    if pos == -1:
        raise ValueError("permissionsStorage JSON не знайдено в SSTable")
    depth, i, in_str, esc = 0, pos, False, False
    while i < len(data):
        b = data[i]; ch = chr(b)
        if esc:
            esc = False
        elif ch == '\\' and in_str:
            esc = True
        elif ch == '"':
            in_str = not in_str
        elif not in_str:
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    i += 1; break
        i += 1
    return json.loads(data[pos:i].decode('utf-8'))

# ── Головна функція ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Додаємо thelobbyx.com до дозволених доменів Claude")
    print("=" * 60)

    # 1. Last sequence
    print("\n[1/4] Читаємо MANIFEST...")
    last_seq = read_last_sequence(MANIFEST_F)
    if last_seq == 0:
        last_seq = 9999
        print(f"  Не вдалось прочитати — використовуємо запасне: {last_seq}")
    else:
        print(f"  kLastSequence = {last_seq}")
    new_seq = last_seq + 1

    # 2. Поточні дозволи
    print("\n[2/4] Читаємо дозволи з SSTable...")
    try:
        perms = read_permissions_json(LDB_FILE)
    except Exception as e:
        print(f"  ПОМИЛКА: {e}")
        sys.exit(1)

    print(f"  Знайдено {len(perms['rules'])} правил:")
    for rule in perms['rules']:
        netloc = rule.get('scope', {}).get('netloc', '?')
        print(f"    - {netloc}")

    existing = {r.get('scope', {}).get('netloc', '') for r in perms['rules']}
    if 'thelobbyx.com' in existing:
        print("\n  thelobbyx.com вже у списку — нічого не змінюємо.")
        return

    # 3. Додаємо правило
    print("\n[3/4] Формуємо нове правило...")
    new_rule = {
        "action": "allow",
        "createdAt": int(time.time() * 1000),
        "duration": "always",
        "id": str(uuid.uuid4()),
        "scope": {"netloc": "thelobbyx.com", "type": "domain"}
    }
    perms['rules'].append(new_rule)
    new_json_str = json.dumps(perms, separators=(',', ':'))
    print(f"  Новий JSON: {len(new_json_str)} байт")
    print(f"  Нове правило ID: {new_rule['id']}")

    # 4. Записуємо WAL
    print("\n[4/4] Записуємо LevelDB WAL запис...")

    key   = b'permissionsStorage'
    value = new_json_str.encode('utf-8')

    # WriteBatch: sequence(uint64) + count(uint32) + kTypeValue + key + value
    batch  = struct.pack('<QI', new_seq, 1)
    batch += b'\x01'             # kTypeValue (PUT)
    batch += put_len_prefixed(key)
    batch += put_len_prefixed(value)

    # Log record: masked_crc(uint32) + length(uint16) + type_FULL(uint8) + batch
    rtype_byte = b'\x01'         # kFullType
    crc    = mask_crc(crc32c(rtype_byte + batch))
    header = struct.pack('<IH', crc, len(batch)) + rtype_byte
    record = header + batch

    try:
        with open(LOG_FILE, 'wb') as f:
            f.write(record)
        print(f"  Записано {len(record)} байт → {os.path.basename(LOG_FILE)}")
        print(f"  Sequence number: {new_seq}")
        print(f"  Key: {key.decode()}")
    except PermissionError as e:
        print(f"\n  ПОМИЛКА доступу: {e}")
        print("  Закрийте Chrome і запустіть скрипт ще раз.")
        sys.exit(1)
    except Exception as e:
        print(f"\n  ПОМИЛКА запису: {e}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("ГОТОВО!")
    print("Перезапустіть Chrome → thelobbyx.com буде дозволено.")
    print("=" * 60)


if __name__ == '__main__':
    main()
