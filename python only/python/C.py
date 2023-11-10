import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Membuat daftar 1000 kata acak dengan panjang antara 3 hingga 10 karakter
random_words = [generate_random_word(random.randint(3, 10)) for _ in range(1000)]

# Menggabungkan kata-kata menjadi satu string
random_text = ' '.join(random_words)

# Menampilkan teks acak
print(random_text)
