#Buat class Akun dengan private attribute saldo. Buat method untuk cek saldo dan tarik dana.


class Akun:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    def cek_saldo(self):
        print(f"Saldo {self.nama}: {self.__saldo}")

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"{jumlah} berhasil ditarik.")
        else:
            print("Saldo tidak cukup.")


akun = Akun("Indra", 1000)
akun.cek_saldo()
akun.tarik(500)
akun.cek_saldo()