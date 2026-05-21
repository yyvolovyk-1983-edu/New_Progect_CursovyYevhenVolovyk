# GitHub Action Plan — Покроковий план

## Крок 1 — GitHub Profile README (10 хвилин, найбільший ефект)

GitHub Profile README — спеціальний репо, що показується на головній сторінці профілю.

```
1. Іди на github.com → New repository
2. Назва репо: yyvolovyk-1983-edu   (ТОЧНО як твій username!)
3. Поставити галочку "Add a README file"
4. Натисни Create repository
5. Відкрий README.md → Edit → вистав вміст з:
   C:\Users\User\Documents\Claude_Code\portfolio\github-profile\README.md
6. Commit changes
```

Результат: на github.com/yyvolovyk-1983-edu з'явиться красива презентація.

---

## Крок 2 — Новий репо: router-security-toolkit (30 хвилин)

```
1. New repository → назва: router-security-toolkit
2. Description: "Python tools for authorized router security auditing"
3. Public
4. Add README: НЕ ставити галочку (ми маємо свій README)
5. Create

6. Завантаж файли з:
   C:\Users\User\Documents\Claude_Code\portfolio\router-security-toolkit\

Файли для завантаження:
  - README.md
  - http_probe.py
  - backdoor_test.py
  - upnp_ssl_test.py
  - requirements.txt
```

Також можна додати з реального аудиту (попередньо видали hardcoded IPs):
  - default_creds_test.py  (з C:\Users\User\security-audit\2026-05-17\)
  - analyze_history.py     (версію без реальних шляхів Chrome)

### Topics для цього репо (Settings → Topics):
```
network-security  router-audit  python  cve  upnp  wifi-security  
penetration-testing  security-tools  home-network
```

---

## Крок 3 — WiFi Security Auditor (Android) репо (20 хвилин)

Work Experience
Yevhen Volovyk | Network Engineer | Kharkiv, Ukraine
+380 75 148 42 07
Telegram & WhatsApp.
volovykyevhen@icloud.com
Telecommunications Technician (Contractor)
Kyivstar — Fixed-line Internet Division | Kharkiv | March 2024 – Present
• Managed the full cycle of installation for network construction and modernization.
• Installed and deployed structured cabling systems (SCS) and local area networks
(LAN).
• Configured and maintained network equipment to ensure uninterrupted service
operation.
• Diagnosed and resolved network hardware faults using systematic root cause
analysis.
• Performed fiber optic splicing and maintained FTTB/PON infrastructure.
• Operated measurement tools (twisted pair testers, optical power meters) and
portable power tools.
• Monitored network health and service availability using Zabbix.
• Analysed network traffic and diagnosed connectivity issues with Wireshark,
tcpdump, and nmap.
Tech stack: TCP/IP · VLAN · NAT · Routing · VPN · Firewall · DHCP · LAN ·
Ethernet · FTTB · PON · MikroTik/RouterOS · Zabbix · Wireshark · tcpdump · nmap ·
Bash · Linux (Ubuntu/Debian)
Infantry Platoon Commander
Defense Forces of Ukraine | March 2023 – May 2024
• Commanded a rifle platoon of 15+ personnel, organizing execution of combat and
strategic tasks.
• Coordinated subordinate actions in high-intensity operational environments,
maintaining unit cohesion and discipline.
• Planned and conducted comprehensive training and personnel development
programs.
• Demonstrated critical decision-making under severe time pressure with full
accountability for personnel, equipment, and mission outcomes.
• Maintained internal reporting, technical documentation, and equipment readiness
records.
Combat veteran of the Russian-Ukrainian war.
Internet Connection Technician
WinSERVICE Ukraine | Kharkiv | November 2018 – March 2023
• Connected residential and business subscribers to the internet network; provided onsite technical consultancy.
• Performed technical maintenance of Ethernet networks and installed structured
cabling systems (SCS).
• Configured routers, switches, and modems; diagnosed and resolved network
hardware and configuration faults.
• Escalated complex issues with structured reproduction steps and technical
documentation.
Tech stack: LAN · Ethernet · FTTB · PON · DHCP · TCP/IP · Network equipment
configuration · SCS installation
Rifleman
Defense Forces of Ukraine | July 2014 – February 2015
• Executed combat and service missions within unit operations.
• Maintained readiness of personal equipment, gear, and weaponry.
• Operated under high responsibility and extreme stress with strict adherence to
military discipline.
Combat veteran of the Russian-Ukrainian war (ATO, Donbas, 2014–2015).
Service Engineer — Technical Equipment Repair
MasterService | Kharkiv | July 2012 – September 2014
• Diagnosed causes of technical failures and executed repair work based on client and
management requests.
• Prepared repair plans and managed procurement of spare parts and components.
• Developed preventative maintenance regulations and service manuals.
• Maintained accounting, reporting, and technical documentation.
SUMMARY OF CHANGES
• WinSERVICE start date: Sep 2019 => Nov 2018 (+10 months of real experience)
• MasterService dates: Aug 2012–Apr 2014 => Jul 2012–Sep 2014 (+5 months of
real experience)
• Kyivstar: added full tech stack block (TCP/IP, VLAN, VPN, Zabbix, Wireshark,
MikroTik, etc.)
• Kyivstar: added fiber optic splicing and Zabbix monitoring as explicit bullet points
• Infantry Commander: platoon size (15+) added for concrete context
• WinSERVICE: added escalation and documentation bullet (transferable to
QA/SysAdmin)

Якщо файли є на Desktop або в іншій директорії:

```
1. New repository → назва: wifi-security-auditor
2. Description: "Android app for Wi-Fi network security analysis"
3. Public

4. Завантаж файли через GitHub Desktop або git push
```

README для нього — створити окремо або я допоможу.

Topics:
```
android  kotlin  wifi-security  network-scanner  mvvm  security  
port-scanner  evil-twin-detection  material3
```

---

## Крок 4 — Оновити існуючі репо

### video-to-gif
```
1. Іди в репо → README.md → Edit
2. Вистав вміст з:
   C:\Users\User\Documents\Claude_Code\portfolio\repo-readmes\video-to-gif-README.md
3. Commit

Topics додати:
   python  opencv  gif  video-processing  pillow
```

### video-frame-extractor
```
1. README.md → Edit
2. Додай короткий опис (аналогічно video-to-gif)

Topics: python  opencv  video  frame-extraction
```

### avtomaticwebtests* (3 репо)
```
1. Перейменуй репо (Settings → Repository name):
   - avtomaticwebtests1.1    → java-selenium-basics
   - avtamaticWebTestLaba2.2 → java-selenium-pageobject
   - avtomaticwebtests1.3    → java-collections-testing

2. Оновити опис кожного репо

3. Для всіх трьох — Topics:
   java  selenium  testing  automation  junit

4. README замінити на вміст з:
   C:\Users\User\Documents\Claude_Code\portfolio\repo-readmes\web-tests-README.md
```

---

## Крок 5 — Pinned Repositories

На профілі можна закріпити 6 репо. Порядок:

```
1. wifi-security-auditor      ← головний продукт
2. router-security-toolkit    ← security toolkit
3. yyvolovyk-1983-edu         ← profile README (автоматично є)
4. video-to-gif               ← python tools
5. java-selenium-basics       ← QA automation
6. (майбутній: ai-agents-pack)
```

Налаштування: Profile → Customize your pins → обери 6 репо.

---

## Крок 6 — Profile Settings

```
Profile → Edit profile:
  Bio: "AI Security Analyst | Network Auditing | Android | KHAI"
  Location: Kharkiv, Ukraine
  Website: (якщо буде Gumroad або особистий сайт)
  
Profile → Achievements:
  Активно коміть → отримаєш Arctic Code Vault Contributor тощо
```

---

## Пріоритети по часу

| Час | Дія | Ефект |
|-----|-----|-------|
| 10 хв | Profile README | Відразу видно на профілі |
| 30 хв | router-security-toolkit | Перший real security repo |
| 20 хв | Перейменувати Java репо | Виглядає професійно |
| 1 год | WiFi Auditor repo | Найбільший продукт |

---

## Що ВИДАЛИТИ або сховати

- `avtamaticWebTestLaba2.2` — якщо не хочеш перейменовувати, можна зробити Private
- Не публікуй файли з реальними IP/MAC/credentials з аудиту
- Не публікуй chrome_history_copy.db та інші sensitive файли
