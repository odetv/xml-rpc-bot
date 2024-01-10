from xmlrpc.server import SimpleXMLRPCServer

# Fungsi-fungsi yang akan di-remote
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fungsi untuk menghitung faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Fungsi untuk mengubah teks menjadi teks terbalik
def reverse_text(text):
    return text[::-1]

# Data dictionary sebagai contoh penyimpanan data
data = {
    'name': 'John Doe',
    'age': 30,
    'country': 'USA'
}

# Fungsi untuk mendapatkan nilai dari kunci tertentu
def get_data(key):
    return data.get(key)

# Inisialisasi server dan daftarkan fungsi-fungsi
server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(is_prime, 'is_prime')
server.register_function(factorial, 'factorial')
server.register_function(reverse_text, 'reverse_text')
server.register_function(get_data, 'get_data')

# Jalankan server
server.serve_forever()