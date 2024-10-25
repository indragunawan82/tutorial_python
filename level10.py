#Buat class Kendaraan dengan atribut merk. Buat class Motor yang mewarisi class Kendaraan dan tambahkan atribut jenis_motor.

class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

class Motor(Kendaraan):
    def __init__(self, merk, jenis_motor):  
        super().__init__(merk)
        self.jenis_motor = jenis_motor

info = Kendaraan("honda")
print(info.merk)

motor = Motor("yamaha", "mio")
print(motor.merk)
print(motor.jenis_motor)
