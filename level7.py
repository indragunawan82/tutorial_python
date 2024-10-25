# Inheritance
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f"Halo, nama saya {self.nama}.")

# Class Mahasiswa mewarisi dari class Manusia
class Mahasiswa(Manusia):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)  # Memanggil konstruktor class induk
        self.jurusan = jurusan

    def perkenalkan(self):
        print(f"Saya {self.nama}, jurusan {self.jurusan}.")

mhs = Mahasiswa("Indra", 35, "Informatika")
mhs.sapa()
mhs.perkenalkan()
