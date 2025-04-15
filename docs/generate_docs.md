# Інструкція з генерації документації

Ця інструкція пояснює, як створити документацію до проєкту **Telegram Movie Bot** за допомогою інструмента [Sphinx](https://www.sphinx-doc.org).

---

## Передумови

Перед початком переконайтеся, що встановлено:

- Python (версія 3.10 або новіша)
- Пакети: `sphinx`, `sphinx_rtd_theme`, `docutils`

Встановити можна командою:
```bash
pip install sphinx sphinx_rtd_theme docutils
```

---

## Структура проєкту

Telegram_bot/
├── bot.py
└── docs/
    ├── build/           # Готова HTML-документація
    ├── source/          # Файли документації (index.rst, conf.py тощо)
    ├── make.bat         # Скрипт для Windows
    └── generate_docs.md # Інструкція

---

## Генерація документації
1. Перейти до кореня проєкту
```bash
cd "шлях_до_папки_проекту/Telegram_bot"
```

2. Створити файли з описом коду (якщо потрібно)
```bash
sphinx-apidoc -o docs/source .
```

3. Згенерувати HTML-документацію
На Windows:
```bash
cd docs
make.bat html
```

На Linux/Mac:
```bash
cd docs
make html
```

---

## Перевірка результату

Відкрийте файл:
```bash
docs/build/index.html
```

---

### Корисні поради
- Всі функції та класи повинні мати docstring у стилі Google або reStructuredText.
- Якщо структура змінилась — перегенеруйте за допомогою sphinx-apidoc.

---

### Автор
- Ліза Денисенко
- GitHub: lizadenysenko