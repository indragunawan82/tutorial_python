# Buat class Mobil dengan atribut merk, tahun, dan method tampilkan_info() untuk menampilkan informasinya.
class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk    
        self.tahun = tahun  

    def tampilkan_info(self):
        print(f"merk: {self.merk}, tahun: {self.tahun}")






mobil1 = Mobil("Toyota", 2020)
mobil1.tampilkan_info()