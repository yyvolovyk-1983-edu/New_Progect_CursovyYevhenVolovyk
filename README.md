<div align="center">

# Network Security Lab

**Документація реальних мережевих сканувань та інструменти захисту DNS**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/yyvolovyk-1983-edu/New_Progect_CursovyYevhenVolovyk)
[![Nmap](https://img.shields.io/badge/Nmap-214478?style=for-the-badge&logoColor=white)](https://github.com/yyvolovyk-1983-edu/New_Progect_CursovyYevhenVolovyk)
[![AdGuard](https://img.shields.io/badge/AdGuard_Home-68BC71?style=for-the-badge&logo=adguard&logoColor=white)](https://github.com/yyvolovyk-1983-edu/New_Progect_CursovyYevhenVolovyk)

</div>

---

## Що в репозиторії

Практична лабораторія мережевої безпеки — реальні результати сканувань Nmap та конфігурація DNS-фільтрації для домашньої мережі.

---

## nmap-output — документація сканувань

8 типів сканувань з реального аудиту мережі у форматах `.nmap`, `.xml`, `.gnmap`.

| Файл | Тип сканування | Команда |
|---|---|---|
| `nmap-quick` | Швидке виявлення хостів | `nmap -T4 -F <target>` |
| `nmap-172-quick` | Швидкий скан підмережі 172.x | `nmap -T4 -F 172.x.x.0/24` |
| `nmap-172-pn` | Скан без ping (обхід ICMP-блокування) | `nmap -Pn 172.x.x.0/24` |
| `nmap-63-quick` | Швидкий скан підмережі 63.x | `nmap -T4 -F 63.x.x.0/24` |
| `nmap-portscan` | Повний скан портів | `nmap -p- <target>` |
| `nmap-targeted` | Цільове сканування сервісів | `nmap -sV -sC <target>` |
| `nmap-udp` | UDP сканування | `nmap -sU <target>` |
| `nmap-vuln` | Сканування вразливостей (NSE) | `nmap --script vuln <target>` |

### Парсинг результатів (Python)

```python
import xml.etree.ElementTree as ET

tree = ET.parse('nmap-vuln.xml')
root = tree.getroot()

for host in root.findall('host'):
    ip = host.find('address').get('addr')
    for port in host.findall('.//port'):
        portid = port.get('portid')
        state  = port.find('state').get('state')
        print(f"{ip}:{portid} — {state}")
```

---

## roblox_block/adguardhome — DNS фільтрація

Конфігурація AdGuard Home для блокування небажаних доменів на рівні DNS.

```
Пристрій → AdGuard Home (DNS) → дозволений домен → інтернет
                               → заблокований домен → BLOCKED
```

---

## Структура репозиторію

```
├── nmap-output/          # Результати мережевих сканувань (24 файли)
├── roblox_block/
│   └── adguardhome/      # Конфігурація DNS-фільтрації
├── KP/                   # Курсовий проект (ХНАДУ, 2026)
└── PORTFOLIO.md          # Опис послуг та кейсів
```

---

> **Увага:** Всі сканування проводились на власній інфраструктурі або з письмовим дозволом власника мережі.

---

<div align="center">

**Автор:** [Євген Воловик](https://github.com/yyvolovyk-1983-edu) · Харків, Україна
📧 y.y.volovyk@student.khai.edu · [LinkedIn](https://www.linkedin.com/in/yevhen-volovyk/)

</div>