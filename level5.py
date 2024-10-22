buah = ["apel", "jeruk", "mangga"]
print(buah[0])  # Output: apel

# Menambah elemen
buah.append("pisang")
print(buah)

# Mengubah elemen
buah[1] = "durian"
print(buah)

# Looping melalui list
for item in buah:
    print(item)


koordinat = (10, 20)
print(koordinat[0])  # Output: 10

# Tuple tidak bisa diubah
# koordinat[0] = 15  # Akan menghasilkan error


mahasiswa = {
    "nama": "Indra",
    "umur": 35,
    "jurusan": "Informatika"
}
print(mahasiswa["nama"])  # Output: Indra

# Menambah atau mengubah nilai
mahasiswa["umur"] = 36
print(mahasiswa)


angka = {1, 2, 3, 3, 4}
print(angka)  # Output: {1, 2, 3, 4}

# Menambah elemen
angka.add(5)
print(angka)
