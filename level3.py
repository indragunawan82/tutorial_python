umur = int(input("Masukkan umur kamu: "))

if umur > 30:
    print("Kamu lebih dari 30 tahun.")
elif umur == 30:
    print("Kamu berumur tepat 30 tahun.")
else:
    print("Kamu kurang dari 30 tahun.")


# Looping untuk mencetak angka 1 sampai 5
for i in range(1, 6):
    print(i)


count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment count


suhu = int(input("masukan suhu"))
if suhu > 37:
    print("suhu badan anda diatas normal")
else:
    print("suhu badan anda dibawah normal") 


# Buat program yang mencetak bilangan genap dari 0 hingga 10.
for i in range(0, 11, 2):
    print(i)


# Buat program yang meminta input angka dari user dan terus menjumlahkan angka yang dimasukkan sampai user memasukkan angka 0. Tampilkan total penjumlahan di akhir.
total = 0
while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        break
    total += angka
print("Total penjumlahan:", total)

