class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo  # Private attribute

    def cek_saldo(self):
        print(f"Saldo {self.nama}: {self.__saldo}")

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"{jumlah} berhasil ditarik.")
        else:
            print("Saldo tidak cukup.")

akun = AkunBank("Indra", 100000)
akun.cek_saldo()
akun.tarik(50000)
akun.cek_saldo()
