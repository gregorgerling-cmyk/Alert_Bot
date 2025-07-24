
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/', methods=['POST'])
def handle_alert():
    data = request.json
    message = data.get('message', 'Kein Text empfangen.')
    send_telegram_message(f"📈 Neues Signal:\n{message}")
    return {'status': 'ok'}

@app.route('/test', methods=['GET'])
def test():
    send_telegram_message("✅ Test erfolgreich: Dein Bot funktioniert!")
    return {'status': 'ok'}

def send_telegram_message(text):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        requests.post(telegram_url, json=payload)
    except Exception as e:
        print(f"Fehler beim Senden: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
