#Irenne Dwita Natalia
#71210752
#Unguided 4

import json

with open("karyawan.json") as file:
    data = json.load(file)

hasil = {}
n = int(input("Masukkan jumlah karyawan baru : "))

for i in range (n):
    nama = input("Masukan nama : ")
    alamat = input("Masukkan alamat : ")
    kolega = []
    jumlah_kolega = int(input("Masukkan jumlah kolega : "))
    for j in range (jumlah_kolega):
        kolega_tambahan = input("Masukkan nama kolega ke-"+ str(j+1)+":" )
        kolega.append(kolega_tambahan)
    print("=== Data berhasil ditambahkan ===")
    print()

    hasil[nama] = [{"Alamat" : alamat},{"Kolega" : kolega}]

with open("karyawan.json","w") as file:
    json.dump(hasil, file)
