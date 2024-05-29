import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = f"https://ваш_домен:8443/{TOKEN}"

def set_webhook():
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
    if response.status_code == 200:
        print("Webhook установлен успешно.")
    else:
        print("Ошибка при установке вебхука:", response.text)

if __name__ == "__main__":
    set_webhook()