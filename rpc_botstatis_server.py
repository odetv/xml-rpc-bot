from xmlrpc.server import SimpleXMLRPCServer

XMLRPC_SERVER_HOST = 'localhost'
XMLRPC_SERVER_PORT = 8000

# Fungsi untuk melakukan tanya jawab
def question_answer(question):
    if question.lower() == '/start':
        return 'Halo saya adalah bot Telegram yang dibuat untuk uji coba Sistem Terdistribusi menggunakan RPC.'
    elif question.lower() == '/help':
        return 'Maaf, untuk saat ini saya belum diprogram untuk bisa membantu anda. Programmer sedang sibuk dengan tugas yang lainnya.'
    else:
        return 'Maaf, saya tidak mengerti dengan maksud Anda.'

# Daftarkan fungsi question_answer sebagai metode XML-RPC
server = SimpleXMLRPCServer((XMLRPC_SERVER_HOST, XMLRPC_SERVER_PORT))
server.register_function(question_answer, 'question_answer')

print(f"Server XML-RPC berjalan di http://{XMLRPC_SERVER_HOST}:{XMLRPC_SERVER_PORT}")
# Jalankan server XML-RPC
server.serve_forever()