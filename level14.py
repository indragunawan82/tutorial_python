# 18. Pemrosesan File di Python
# Python memungkinkan kita untuk membaca, menulis, dan memanipulasi file dengan sangat mudah.

# 1. Membuka dan Membaca File
# Gunakan fungsi open() untuk membuka file.
# Mode yang sering digunakan:

# 'r': Baca file (default).
# 'w': Tulis file (overwrite).
# 'a': Tulis file (append).
# 'b': Mode biner (untuk file gambar, PDF, dll.).



with open('contoh.txt', 'r') as file:
    data = file.read()
    print(data)


    # Menulis ke file (overwrite)
with open('contoh.txt', 'w') as file:
    file.write("Ini adalah baris pertama.\n")

# Menambah isi ke file
with open('contoh.txt', 'a') as file:
    file.write("Ini adalah baris kedua.\n")


with open('contoh.txt', 'r') as file:
    data = file.read()
    print(data)

with open('contoh.txt', 'r') as file:
    for baris in file:
        print(baris.strip())  # .strip() untuk menghapus karakter newline
