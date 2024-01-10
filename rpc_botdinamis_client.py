import xmlrpc.client
import telebot
import datetime
import requests

# Token Bot Telegram
BOT_TOKEN = '6021996634:AAGzhNIszRVjeXKHXqKWbFZ1WuZBP_6k3ms'
# Membuat koneksi ke RPC server
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')
# Membuat objek bot
bot = telebot.TeleBot(BOT_TOKEN)

# Fungsi untuk mencatat log aktivitas
def log_activity(user_id, question):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] User ID: {user_id} - Question: {question}")

# Fungsi Menangani pesan yang diterima dari pengguna
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    question = message.text
    log_activity(user_id, question)
    if message.text.lower() == '/start':
        bot.reply_to(message, "Halo, saya adalah bot Telegram yang dibuat untuk uji coba Sistem Terdistribusi menggunakan RPC.")
    elif message.text.lower() == '/help':
        bot.reply_to(message, "Bot ini hanya memiliki fitur pencarian identitas mahasiswa berdasarkan NIM. Silakan masukkan NIM mahasiswa yang ingin Anda cari.")
    else:
        try:
            nim = int(message.text)
            mahasiswa = proxy.find_mahasiswa_by_nim(str(nim))
            if mahasiswa:
                response = f"NIM: {mahasiswa['nim']}\nNama: {mahasiswa['nama_mhs']}\nTTL: {mahasiswa['ttl_mhs']}\nSemester: {mahasiswa['semester']}\nKelas: {mahasiswa['kelas_mhs']}\nNo.HP: {mahasiswa['no_hp_mhs']}\nEmail: {mahasiswa['email_mhs']}\nProdi: {mahasiswa['prodi']}\nJurusan: {mahasiswa['jurusan']}\nFakultas: {mahasiswa['fakultas']}\nStatus: {mahasiswa['status_mhs']}"
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "Mahasiswa dengan NIM tersebut tidak ditemukan.")
        except ValueError:
            bot.reply_to(message, "Maaf, saya tidak mengerti dengan maksud Anda.")
        except xmlrpc.client.Fault as e:
            # Mengambil gambar kartu NIM dari URL
                nim_image_url = f"https://sso.undiksha.ac.id:8443/verif/ktm.php?nim={nim}"
                response = requests.get(nim_image_url)
                
                # Mengirim gambar ke pengguna
                if response.status_code == 200:
                    bot.send_photo(message.chat.id, response.content)
                else:
                    bot.reply_to(message, "Gambar kartu NIM tidak dapat ditemukan.")

# Menjalankan bot
bot.infinity_polling()






# import xmlrpc.client
# import telebot
# import datetime

# # Token Bot Telegram
# BOT_TOKEN = '6021996634:AAGzhNIszRVjeXKHXqKWbFZ1WuZBP_6k3ms'
# # Membuat koneksi ke RPC server
# proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')
# # Membuat objek bot
# bot = telebot.TeleBot(BOT_TOKEN)

# # Fungsi untuk mencatat log aktivitas
# def log_activity(user_id, question):
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{current_time}] User ID: {user_id} - Question: {question}")

# # Fungsi Menangani pesan yang diterima dari pengguna
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     user_id = message.chat.id
#     question = message.text
#     log_activity(user_id, question)
#     if message.text.lower() == '/start':
#         bot.reply_to(message, "Halo saya adalah bot Telegram yang dibuat untuk uji coba Sistem Terdistribusi menggunakan RPC.")
#     elif message.text.lower() == '/help':
#         bot.reply_to(message, "Bot ini hanya memiliki fitur pencarian identitas mahasiswa berdasarkan NIM. Silakan masukkan NIM mahasiswa yang ingin Anda cari.")
#     else:
#         try:
#             nim = int(message.text)
#             mahasiswa = proxy.find_mahasiswa_by_nim(str(nim))
#             if mahasiswa:
#                 response = f"NIM: {mahasiswa['nim']}\nNama: {mahasiswa['nama_mhs']}\nTTL: {mahasiswa['ttl_mhs']}\nSemester: {mahasiswa['semester']}\nKelas: {mahasiswa['kelas_mhs']}\nNo.HP: {mahasiswa['no_hp_mhs']}\nEmail: {mahasiswa['email_mhs']}\nProdi: {mahasiswa['prodi']}\nJurusan: {mahasiswa['jurusan']}\nFakultas: {mahasiswa['fakultas']}\nStatus: {mahasiswa['status_mhs']}"
#             bot.reply_to(message, response)
#         except ValueError:
#             bot.reply_to(message, "Maaf, saya tidak mengerti dengan maksud Anda.")
#         except xmlrpc.client.Fault as e:
#             bot.reply_to(message, "Mahasiswa dengan NIM tersebut tidak ditemukan.")
    
# # Menjalankan bot
# bot.infinity_polling()