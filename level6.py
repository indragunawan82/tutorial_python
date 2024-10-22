# Definisi Class
class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def perkenalkan(self):
        print(f"Nama saya {self.nama}, umur {self.umur}, jurusan {self.jurusan}.")

# Membuat Objek
mhs1 = Mahasiswa("Indra", 35, "Informatika")
mhs1.perkenalkan()
