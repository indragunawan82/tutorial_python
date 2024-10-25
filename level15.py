# Menghubungkan Python dengan Database (SQLite)
import sqlite3

# Membuat koneksi dan cursor
koneksi = sqlite3.connect('contoh.db')
cursor = koneksi.cursor()

# Membuat tabel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        umur INTEGER
    )
''')

cursor.execute("INSERT INTO mahasiswa (nama, umur) VALUES (?, ?)", 
               ("Indra", 35))

cursor.execute("SELECT * FROM mahasiswa")
data = cursor.fetchall()

for row in data:
    print(row)

print("Data berhasil ditambahkan!")
koneksi.commit()
koneksi.close()


# cara membuka Sqllite di terminal :  sqlite3 contoh.db