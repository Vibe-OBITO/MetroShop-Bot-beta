# MetroShop-Bot-beta
### Руководство по запуску, установке и настройке бота

#### Оглавление:
1. [Русский](#русский)
2. [English](#english)
3. [Українська](#українська)

---

## Русский

### Установка и запуск

1. **Клонирование репозитория и переход в директорию проекта:**

    ```bash
    git clone https://github.com/your/repo.git
    cd repo
    ```

2. **Создание виртуального окружения и установка зависимостей:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Настройка переменных окружения:**

    Создайте файл `.env` в корневой директории проекта и добавьте туда ваш токен бота:

    ```env
    TELEGRAM_TOKEN=ваш_токен_бота
    ```

4. **Настройка базы данных:**

    ```bash
    python -m app.db
    ```

5. **Установка вебхука:**

    ```bash
    python -m app.set_webhook
    ```

6. **Запуск сервера:**

    ```bash
    python -m app.server
    ```

### Структура проекта

```
/app
│
├── db.py
├── main.py
├── server.py
└── set_webhook.py
requirements.txt
```

---

## English

### Installation and Setup

1. **Clone the repository and navigate to the project directory:**

    ```bash
    git clone https://github.com/your/repo.git
    cd repo
    ```

2. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your bot token:

    ```env
    TELEGRAM_TOKEN=your_bot_token
    ```

4. **Initialize the database:**

    ```bash
    python -m app.db
    ```

5. **Set up the webhook:**

    ```bash
    python -m app.set_webhook
    ```

6. **Start the server:**

    ```bash
    python -m app.server
    ```

### Project Structure

```
/app
│
├── db.py
├── main.py
├── server.py
└── set_webhook.py
requirements.txt
```

---

## Українська

### Встановлення та запуск

1. **Клонування репозиторію та перехід до директорії проекту:**

    ```bash
    git clone https://github.com/your/repo.git
    cd repo
    ```

2. **Створення віртуального середовища та встановлення залежностей:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Налаштування змінних середовища:**

    Створіть файл `.env` у кореневій директорії проекту та додайте туди ваш токен бота:

    ```env
    TELEGRAM_TOKEN=ваш_токен_бота
    ```

4. **Налаштування бази даних:**

    ```bash
    python -m app.db
    ```

5. **Встановлення вебхука:**

    ```bash
    python -m app.set_webhook
    ```

6. **Запуск сервера:**

    ```bash
    python -m app.server
    ```

### Структура проекту

```
/app
│
├── db.py
├── main.py
├── server.py
└── set_webhook.py
requirements.txt
```

Теперь у вас есть подробное руководство по запуску, установке и настройке бота на трех языках.
