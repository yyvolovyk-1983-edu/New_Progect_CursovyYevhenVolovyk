# WiFi Security Auditor

> Android-застосунок для аналізу безпеки Wi-Fi мереж, виявлення загроз та автоматизованого аудиту бездротової інфраструктури.

[![Android](https://img.shields.io/badge/Android-API_26%2B-34A853?style=flat&logo=android&logoColor=white)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-1.9+-7F52FF?style=flat&logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![MVVM](https://img.shields.io/badge/Architecture-MVVM-blue?style=flat)](https://developer.android.com/topic/architecture)
[![Material3](https://img.shields.io/badge/UI-Material_Design_3-6750A4?style=flat&logo=material-design&logoColor=white)](https://m3.material.io)

## Можливості

- **Сканування мереж** — виявлення та класифікація Wi-Fi точок доступу за типом шифрування (WEP / WPA / WPA2 / WPA3 / WPS)
- **Host Discovery** — ARP-сканування та пошук активних хостів у локальній мережі
- **Port Scanner** — сканування відкритих портів (TCP) на виявлених хостах
- **Evil Twin Detection** — виявлення підроблених точок доступу з однаковим SSID за аналізом BSSID та OUI
- **Honeypot Detection** — визначення аномально сильного сигналу та нетипових параметрів мережі
- **Security Rating** — автоматична оцінка рівня безпеки мережі (Critical / High / Medium / Low)

## Технологічний стек

| Компонент | Технологія |
|-----------|------------|
| Мова | Kotlin 1.9+ |
| Архітектура | MVVM + Repository Pattern |
| UI | Material Design 3, ViewBinding |
| Асинхронність | Kotlin Coroutines + Flow |
| DI | Hilt |
| Сканування | Android WifiManager, NetworkCallback API |
| Мін. SDK | Android 8.0 (API 26) |

## Архітектура

```
app/
├── data/
│   ├── wifi/        # WifiScanner, NetworkClassifier
│   ├── network/     # HostDiscovery, PortScanner
│   └── analysis/    # EvilTwinDetector, AnomalyEngine
├── domain/
│   ├── model/       # WifiNetwork, HostInfo, ThreatAlert
│   └── usecase/     # ScanNetworksUseCase, AuditReportUseCase
└── ui/
    ├── scanner/     # Головний екран сканування
    ├── hosts/       # Список хостів і портів
    └── report/      # Звіт безпеки
```

## Збірка та запуск

```bash
git clone https://github.com/yyvolovyk-1983-edu/wifi-security-auditor
cd wifi-security-auditor
./gradlew assembleDebug
```

Або відкрити в Android Studio Hedgehog (2023.1+) і запустити на пристрої / емуляторі.

**Необхідні дозволи:**
```xml
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

## Приклад: виявлення Evil Twin

```kotlin
fun detectEvilTwin(networks: List<WifiNetwork>): List<ThreatAlert> {
    return networks
        .groupBy { it.ssid }
        .filter { (_, group) -> group.size > 1 }
        .flatMap { (ssid, group) -> analyzeDuplicates(ssid, group) }
}

private fun analyzeDuplicates(ssid: String, group: List<WifiNetwork>): List<ThreatAlert> {
    val reference = group.maxByOrNull { it.rssi } ?: return emptyList()
    return group
        .filter { it.bssid != reference.bssid }
        .map { ThreatAlert(type = ThreatType.EVIL_TWIN, ssid = ssid, bssid = it.bssid) }
}
```

## Шкала оцінки безпеки

| Рівень | Умова |
|--------|-------|
| 🔴 Critical | Відкрита мережа або WEP |
| 🟠 High | WPA з TKIP або WPS увімкнено |
| 🟡 Medium | WPA2-Personal без додаткового захисту |
| 🟢 Low / Safe | WPA3 або WPA2 з PMF + без WPS |

## Статус

Застосунок знаходиться в активній розробці. Основні модулі сканування та виявлення загроз реалізовано. Наступний крок — публікація у Google Play.

---

> **Відповідальність:** Інструмент призначений виключно для авторизованого аудиту власних мереж. Використання стосовно чужих мереж без дозволу є незаконним.
