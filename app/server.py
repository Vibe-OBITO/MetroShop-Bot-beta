# /app/server.py

from aiohttp import web
import ssl
import os

from main import dp, on_startup

API_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = f'/{API_TOKEN}'
WEBHOOK_URL = f'https://ваш_домен:8443/{API_TOKEN}'


async def handle(request):
    update = await request.json()
    await dp.process_update(types.Update(**update))
    return web.Response()


app = web.Application()
app.router.add_post(WEBHOOK_PATH, handle)

if __name__ == '__main__':
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain('path/to/your_cert.pem', 'path/to/your_key.pem')

    web.run_app(app, host='0.0.0.0', port=8443, ssl_context=ssl_context)
