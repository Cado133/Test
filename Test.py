import requests
import telebot
from flask import Flask 
import threading

TOKEN = "7551822124:AAHso0B44mwdJdhzfL9eqrwySodOHel9czE"
bot = telebot.TeleBot(TOKEN)

# Fonction pour ajouter une réaction à un message
def ajouter_reaction(chat_id, message_id, emoji):
    url = f"https://api.telegram.org/bot{TOKEN}/setChatReaction"
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "emoji": emoji
    }
    response = requests.post(url, data=payload)
    print(response.json())  # Affiche la réponse de Telegram pour vérifier

# Surveille tous les messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    message_id = message.message_id
    ajouter_reaction(chat_id, message_id, "👍")  # Emoji de test
    
# ▶️ Flask pour Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telegram actif via Render ✅"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

# ▶️ Démarrage
if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    bot.infinity_polling()
