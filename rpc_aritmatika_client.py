import xmlrpc.client

# Inisialisasi proxy klien
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Panggil fungsi-fungsi remote
result = proxy.add(4, 5)
print("4 + 5 =", result)

result = proxy.subtract(10, 3)
print("10 - 3 =", result)

result = proxy.multiply(2, 6)
print("2 * 6 =", result)

# Panggil fungsi-fungsi remote
number = 17
result = proxy.is_prime(number)
print(f"{number} adalah bilangan prima: {result}")

number = 5
result = proxy.factorial(number)
print(f"Faktorial dari {number} adalah: {result}")

text = "Halo Dunia!"
result = proxy.reverse_text(text)
print(f"Text terbalik dari '{text}' adalah: {result}")

key = 'name'
result = proxy.get_data(key)
print(f"Nilai dari kunci '{key}': {result}")

key = 'age'
result = proxy.get_data(key)
print(f"Nilai dari kunci '{key}': {result}")

key = 'country'
result = proxy.get_data(key)
print(f"Nilai dari kunci '{key}': {result}")