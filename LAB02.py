# Nama: Muhammad Fazil Tirtana
# Kelompok: 02
# Jurusan: Ilmu Komputer
# NPM: 2306274983

import math
import random

# Function untuk menghitung luas setiap bentuk
def hitung_segiempat(panjang, lebar):
    return panjang * lebar

def hitung_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_lingkaran(diameter):
    return math.pi * (diameter / 2) ** 2

def randomizer():
    return random.choice(["segiempat", "segitiga", "lingkaran"])

# Main program
HARGA = 100  # Harga kertas per cm^2
print("Welcome to Dek Depe's Name Tag Store!")

jumlah_pelanggan = int(input("Masukkan jumlah pelanggan: ").strip())
print("----------------------------------------")

# Loop setiap pelanggan
for i in range(1, jumlah_pelanggan + 1):
    print(f"======= PELANGGAN {i}")
    nama_pelanggan = input(f"Masukkan nama pelanggan ke-{i}: ")
    jumlah_name_tag = int(input("Masukkan jumlah name tag yang ingin dibuat: "))
    luas_total = 0

    # Loop setiap name tag yang ingin dibuat
    for j in range(1, jumlah_name_tag + 1):
        bentuk_name_tag = input("Bentuk name tag ke-" + str(j) + " (segiempat/segitiga/lingkaran/random): ").lower()

        # Jika pilihan bentuk adalah "random", pilih bentuk secara acak
        if bentuk_name_tag == "random":
            bentuk_name_tag = randomizer()
            print(f"Bentuk yang terpilih adalah {bentuk_name_tag}")

        # Hitung luas sesuai bentuk yang dipilih
        if bentuk_name_tag in ["segiempat", "segitiga", "lingkaran"]:
            if bentuk_name_tag == "segiempat":
                panjang = float(input("Masukkan panjang (cm): "))
                lebar = float(input("Masukkan lebar (cm): "))
                luas_total += hitung_segiempat(panjang, lebar)
            elif bentuk_name_tag == "segitiga":
                alas = float(input("Masukkan panjang alas (cm): "))
                tinggi = float(input("Masukkan tinggi (cm): "))
                luas_total += hitung_segitiga(alas, tinggi)
            elif bentuk_name_tag == "lingkaran":
                diameter = float(input("Masukkan diameter (cm): "))
                luas_total += hitung_lingkaran(diameter)

            print()

    harga_total = luas_total * HARGA

    # Menampilkan total harga untuk pelanggan
    print(f"Total harga kertas yang diperlukan untuk membuat {jumlah_name_tag} name tag untuk pelanggan atas nama {nama_pelanggan} adalah Rp{harga_total}\n")

print("----------------------------------------")
print("Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!")
