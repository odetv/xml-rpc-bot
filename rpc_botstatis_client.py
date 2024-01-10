import xmlrpc.client
import telebot
import datetime

# Token bot Telegram yang diberikan oleh BotFather
TOKEN = '6021996634:AAGzhNIszRVjeXKHXqKWbFZ1WuZBP_6k3ms'
# URL server XML-RPC
XMLRPC_SERVER_URL = 'http://localhost:8000/'

# Inisialisasi bot Telegram
bot = telebot.TeleBot(TOKEN)

# Fungsi untuk mengirim pertanyaan ke server XML-RPC dan mendapatkan jawaban
def get_answer_from_server(question, chat_id):
    # Kirim pertanyaan ke server XML-RPC
    proxy = xmlrpc.client.ServerProxy(XMLRPC_SERVER_URL)
    answer = proxy.question_answer(question)
    log_message(question, answer, chat_id)
    return answer

# Fungsi untuk mencatat log
def log_message(question, answer, chat_id):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = f'{timestamp} | ID: {chat_id} | Q: {question} | A: {answer}'
    print(log)

# Fungsi untuk menangani pesan yang diterima dari bot Telegram
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Tanggapi hanya jika pesan yang diterima adalah teks
    if message.content_type == 'text':
        question = message.text
        chat_id = message.chat.id
        answer = get_answer_from_server(question, chat_id)
        bot.send_message(message.chat.id, answer)

# Jalankan bot Telegram
bot.infinity_polling()