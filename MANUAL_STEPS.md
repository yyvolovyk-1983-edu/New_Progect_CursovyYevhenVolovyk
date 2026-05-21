# Ручні кроки монетизації — що і де робити

> Все що створено автоматично — готове. Цей файл — тільки те, що треба зробити ТЕБЕ РУКАМИ.
> Статус: [ ] не зроблено  [~] в процесі  [x] готово

---

## ДЕНЬ 1–2: GitHub + GitHub Pages (30 хвилин)

### Крок 1 — Створи GitHub акаунт (якщо немає)
- [ ] Зайди: https://github.com/signup
- [ ] Username: `yvolovyk` або `yaroslav-volovyk` (перевір доступність)
- [ ] Email: y.y.volovyk@student.khai.edu
- [ ] Верифікуй email

### Крок 2 — Створи репозиторій портфоліо-сайту
- [ ] GitHub → New repository
- [ ] Repository name: `[твій_username].github.io` (ТОЧНО так, з твоїм username)
- [ ] Public (обов'язково!)
- [ ] НЕ додавай README при створенні
- [ ] Натисни Create repository

### Крок 3 — Завантаж сайт на GitHub
Відкрий PowerShell і виконай:
```powershell
cd "C:\Users\User\Documents\Claude_Code\github-pages"
git init
git add index.html
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/yyvolovyk-1983-edu/yyvolovyk-1983-edu.github.io.git
git push -u origin main
```

### Крок 4 — Увімкни GitHub Pages
- [ ] Зайди в репозиторій → Settings → Pages
- [ ] Source: Deploy from a branch
- [ ] Branch: main / (root)
- [ ] Натисни Save
- [ ] Через 1-2 хвилини сайт буде на https://yyvolovyk-1983-edu.github.io

### Крок 5 — Заміни плейсхолдери в сайті
- [x] `YOUR_GITHUB_USERNAME` → yyvolovyk-1983-edu ✓ (вже замінено)
- [x] `YOUR_LINKEDIN` → євген-євгенович-воловик-b9a77b409 ✓ (вже замінено)
- [ ] `YOUR_UPWORK_ID` → замінити після реєстрації на Upwork

### Крок 6 — Опублікуй multi-ai-collab
- [ ] GitHub → New repository → назва: `multi-ai-collab`
- [ ] Public, без README
```powershell
cd "C:\Users\User\.claude\skills\multi-ai-collab"
git init
git add SKILL.md README.md
git commit -m "Initial release: multi-ai-collab Claude Code skill"
git branch -M main
git remote add origin https://github.com/yyvolovyk-1983-edu/multi-ai-collab.git
git push -u origin main
```
- [ ] Додай тег: `claude-code`, `ai-agents`, `prompt-engineering`, `multi-ai`
- [ ] Додай "About" опис у репозиторій: "Claude Code skill for multi-model AI collaboration"

---

## ДЕНЬ 2–3: Upwork (45 хвилин)

### Крок 7 — Зареєструйся на Upwork
- [ ] https://www.upwork.com/signup
- [ ] Email: y.y.volovyk@student.khai.edu (або новий для роботи)
- [ ] Вибери: "Work as a freelancer"
- [ ] Заповни профіль (скопіюй bio з `C:\Users\User\.claude\templates\upwork_profile.md`)

### Крок 8 — Верифікуй акаунт
- [ ] Завантаж фото (ділове, нейтральний фон)
- [ ] ID Verification — потрібен паспорт або ID-картка
- [ ] Connect: GitHub (якщо Upwork дозволяє) → показує реальні проекти

### Крок 9 — Підключи платіжний метод
ВАЖЛИВО: без цього не отримаєш гроші.
- [ ] Зареєструйся на Payoneer: https://payoneer.com
  - Country: Ukraine
  - Додай до Upwork як платіжний метод
- [ ] АБО Wise: https://wise.com
  - Швидша верифікація для України
  - Нижчі комісії для малих сум

### Крок 10 — Заповни Upwork профіль
Скопіюй готовий текст з `C:\Users\User\.claude\templates\upwork_profile.md`:
- [ ] Professional title: `AI Agent Developer (Claude Code) & Security Auditor`
- [ ] Overview/Bio: скопіюй розділ "PROFESSIONAL OVERVIEW"
- [ ] Hourly rate: $30
- [ ] Skills: додай 10 тегів зі списку в upwork_profile.md
- [ ] Portfolio: додай 3 картки (описи в upwork_profile.md)
- [ ] Availability: More than 30 hrs/week (навіть якщо насправді менше)

### Крок 11 — Перші 20 заявок
- [ ] Знайди гіги за ключовими словами: "Claude Code", "AI agent", "prompt engineering", "security audit"
- [ ] Для кожної заявки: відкрий шаблон A/B/C з upwork_profile.md, адаптуй 2-3 реченнями під конкретний гіг
- [ ] Ціль: 10 заявок в день 1, 10 в день 2
- [ ] Не відправляй без персоналізації — шаблон треба адаптувати, не просто копіювати

---

## ДЕНЬ 3–4: Fiverr (20 хвилин)

### Крок 12 — Створи Fiverr профіль
- [ ] https://www.fiverr.com/join
- [ ] Username: `yaroslav_volovyk` або `yvolovyk`
- [ ] Зв'яжи з LinkedIn (якщо є)

### Крок 13 — Опублікуй перший gig
Скопіюй з `C:\Users\User\.claude\templates\upwork_profile.md` розділ "FIVERR GIG":
- [ ] Gig title: "Build you a custom Claude Code skill or AI agent for your workflow"
- [ ] Category: Programming & Tech → AI Services
- [ ] Вставити опис та таблицю пакетів
- [ ] Thumbnail: зроби просте зображення (Canva безкоштовно) — темний фон, білий текст "Claude Code Agent Developer"

---

## ДЕНЬ 4–5: PromptBase (30 хвилин)

### Крок 14 — Зареєструйся на PromptBase
- [ ] https://promptbase.com → Sign in with Google
- [ ] Натисни "Sell" → заповни seller profile

### Крок 15 — Опублікуй 5 промтів
Всі тексти готові в `C:\Users\User\Documents\Claude_Code\promptbase-prompts.md`:
- [ ] Промт 1: Security Audit Report Writer ($7)
- [ ] Промт 2: Home Network Security Checklist ($5)
- [ ] Промт 3: Claude Code Agent Designer ($9)
- [ ] Промт 4: Technical Documentation Writer ($6)
- [ ] Промт 5: Avionics Engineering Assistant ($9)

Для кожного:
1. Скопіюй заголовок, категорію, ціну
2. Скопіюй текст з блоку ``` ... ```
3. Протестуй промт перед публікацією
4. Напиши 2-3 речення опису

---

## ДЕНЬ 5–7: Локальний UA ринок

### Крок 16 — Список потенційних клієнтів
- [ ] Склади список 15 знайомих хто може бути зацікавлений в аудиті домашньої мережі:
  - Одногрупники ХАІ
  - Друзі родини старшого покоління (менш технічні — більш вразливі)
  - Знайомі зі своїм бізнесом (кафе, магазин, офіс)

### Крок 17 — Надішли повідомлення
Шаблон (скопіюй і адаптуй):
```
Привіт! Зараз проводжу аудити безпеки домашніх мереж — перевіряю роутер, WiFi,
всі підключені пристрої на вразливості. Недавно в одному хоумнет знайшов
backdoor-порт з публічним CVE — власник не знав 10+ років.

Якщо цікаво — зроблю за 1500₴ з повним звітом.
Займає 1 вечір, результат — список конкретних ризиків і як їх закрити.
```

### Крок 18 — Роздрукуй акт-дозвіл
- [ ] Відкрий `C:\Users\User\.claude\templates\audit_consent_form.md`
- [ ] Роздрукуй 5 копій UA версії
- [ ] Підписувати ПЕРЕД початком будь-якого аудиту

---

## ДЕНЬ 7+: LinkedIn (20 хвилин)

### Крок 19 — Налаштуй LinkedIn профіль
- [ ] https://linkedin.com (увійди або створи)
- [ ] Headline: `AI Agent Developer (Claude Code) | Aerospace Security Researcher | KHAI University`
- [ ] About: (нижче готовий текст)
- [ ] Add URL: посилання на GitHub Pages сайт

**LinkedIn About (EN, скопіюй як є):**
```
I build custom Claude Code AI agents for complex technical workflows, and conduct 
structured security audits for homes and small businesses.

Background: Aerospace engineering student at KHAI University, Ukraine — specializing 
in avionics, safety-critical systems (DO-178C), and navigation (INS/GPS). 
My engineering training means I approach every problem methodically and document everything.

What I've built:
→ Suite of 5 interconnected Claude Code agents for aerospace academic writing 
  (reduced 40-hour document workflows to 8 hours)
→ Multi-AI orchestration pipeline: Claude + Gemini + Groq with automatic routing,
  consensus verification, and health monitoring
→ Security audit framework: 8-phase methodology, 23 findings documented in first audit, 
  including CVE-2015-0552

Currently available for:
• Custom Claude Code agents and skills
• Multi-AI pipeline architecture and implementation  
• Home and SMB security audits (with signed authorization agreement)
• Prompt engineering for technical domains

→ Portfolio: https://yyvolovyk-1983-edu.github.io
→ Hire me: [YOUR_UPWORK_URL — додати після реєстрації]
```

---

## ТИЖДЕНЬ 2: Реєстрація Bug Bounty (10 хвилин)

### Крок 20 — HackerOne
- [ ] https://hackerone.com → Sign up → Hacker
- [ ] Заповни профіль (можна мінімально)
- [ ] Знайди програми з тегом VDP (Vulnerability Disclosure Program) — безкоштовно, без виплат, але для портфоліо

### Крок 21 — Bugcrowd
- [ ] https://bugcrowd.com → Register
- [ ] Аналогічно — шукай VDP або programs з низьким entry bar

**Перші 4 тижні — тільки навчання, НЕ рахуй на гроші.**
1-2 год/тиждень. Мета: перша валідна знахідка за 2-3 місяці.

---

## МІСЯЦЬ 2: Реєстрація ФОП (якщо дохід > $200/міс)

### Крок 22 — ФОП 3-ї групи
- [ ] Додаток "Дія" → Бізнес → Стати підприємцем
- [ ] Вибрати: 3 група, єдиний податок 5%
- [ ] КВЕД: 62.01 (розроблення комп'ютерного програмного забезпечення)
       62.09 (інша діяльність у сфері ІТ)
       74.90 (інша професійна, наукова та технічна діяльність)
- [ ] Payoneer прив'язати до рахунку ФОП у банку (Monobank, ПриватБанк, Skybank)

---

## ЧЕКЛІСТ "ПЕРШИЙ КЛІЄНТ ОТРИМАНИЙ"

- [ ] GitHub Pages сайт живий і виглядає добре
- [ ] Upwork профіль 100% заповнений
- [ ] ≥20 заявок надіслано
- [ ] Payoneer/Wise підключений
- [ ] Акт-дозвіл роздрукований
- [ ] ≥1 відповідь від потенційного клієнта

**Якщо через 2 тижні жодної відповіді:** знизь ставку до $20/год тимчасово, 
відправ ще 20 заявок, переглянь cover letter шаблон.

---

## Важливі посилання

| Ресурс | URL |
|--------|-----|
| Upwork | https://upwork.com |
| Fiverr | https://fiverr.com |
| PromptBase | https://promptbase.com |
| Payoneer | https://payoneer.com |
| Wise | https://wise.com |
| HackerOne | https://hackerone.com |
| Bugcrowd | https://bugcrowd.com |
| YesWeHack | https://yeswehack.com |
| GitHub | https://github.com |
| Canva (безкоштовно) | https://canva.com |
| Дія ФОП | https://diia.gov.ua |

---

*Оновлено: 2026-05-18. Всі інші файли (portfolio, prompts, consent form, upwork bio) — в `C:\Users\User\Documents\Claude_Code\` та `C:\Users\User\.claude\templates\`*
