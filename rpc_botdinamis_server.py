import xmlrpc.server
import mysql.connector


# Konfigurasi koneksi ke database
XMLRPC_SERVER_HOST = 'localhost'
XMLRPC_SERVER_PORT = 8000
db_user = 'root'
db_password = ''
db_name = 'db_bot'

# Membuat koneksi ke database
db = mysql.connector.connect(
    host=XMLRPC_SERVER_HOST,
    user=db_user,
    password=db_password,
    database=db_name
)

# Membuat objek cursor untuk menjalankan query
cursor = db.cursor(dictionary=True)

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def find_mahasiswa_by_nim(nim):
    # Menjalankan query untuk mencari mahasiswa berdasarkan NIM
    query = f"SELECT * FROM mahasiswa WHERE nim = '{nim}'"
    cursor.execute(query)
    # Mengambil hasil query
    result = cursor.fetchone()
    # Mengembalikan hasil pencarian
    return result

# Membuat server RPC
server = xmlrpc.server.SimpleXMLRPCServer((XMLRPC_SERVER_HOST, XMLRPC_SERVER_PORT))
server.register_function(find_mahasiswa_by_nim, 'find_mahasiswa_by_nim')

# Menjalankan server
print(f"Server XML-RPC berjalan di http://{XMLRPC_SERVER_HOST}:{XMLRPC_SERVER_PORT}")
server.serve_forever()