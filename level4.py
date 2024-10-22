def sapa(nama):
    print(f"Halo, {nama}! Selamat belajar Python.")

# Memanggil fungsi
sapa("Indra")


def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print(f"Hasil penjumlahan: {hasil}")


def perkenalan(nama, umur=25):
    print(f"Halo, nama saya {nama}. Umur saya {umur} tahun.")

# Memanggil fungsi      
perkenalan("Indra",35)
perkenalan("Gunawan")


#Gunakan *args dan **kwargs untuk parameter tak terbatas.
def cetak_semua(*args):
    for arg in args:
        print(arg)

cetak_semua("Python", "JavaScript", "Flutter")


#Buat fungsi yang menerima dua angka dan mengembalikan hasil perkaliannya.
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

def perkalian(bil1, bil2):
    return bil1 * bil2

hasil = perkalian(bil1, bil2)
print(f"Hasil perkalian: {hasil}")

nama = input("masukkan nama anda: ")
hobi = input("masukkan hobi anda: ")
if not hobi.strip():  # .strip() untuk menghapus spasi kosong
    hobi = "coding"


def biodata(nama, hobi="coding"):
    print(f"Nama: {nama}")
    print(f"Hobi: ", hobi)

biodata(nama, hobi)


#Buat fungsi yang menerima sejumlah angka dan mencetak total penjumlahan semua angka tersebut.
def penjumlahan(*args):
    total = 0
    for arg in args:
        total += arg
    return total

total = penjumlahan([1, 2, 3, 4, 5])
print(f"Total penjumlahan: {total}")