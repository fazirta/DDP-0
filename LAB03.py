# Nama: Muhammad Fazil Tirtana
# Kelompok: 02
# Jurusan: Ilmu Komputer
# NPM: 2306274983

import math
import random

list_nametag = []  # Inisialisasi daftar yang akan digunakan untuk menyimpan detail pesanan name tag.

jenis_kertas = {  # Dictionary yang berisi jenis kertas dan harganya per cm^2.
    "HVS": 100,
    "Karton": 150,
    "Buffalo": 170,
    "Art Paper": 190
}

# Fungsi untuk mencetak menu aplikasi.
def print_menu():
    print("Welcome to Dek Depe's Name Tag Store!")
    print("----------------------------------------")
    print("(1) Buat name tag")
    print("(2) Lihat pesanan name tag")
    print("(3) Exit\n")

# Fungsi untuk mencetak daftar harga jenis kertas yang tersedia.
def print_list_harga():
    print("Bahan kertas name tag yang tersedia:")
    for i, j in jenis_kertas.items():
        print(f"> {i}: Rp{j}/cm^2")

# Fungsi untuk menghitung luas setiap bentuk.
def hitung_segiempat(panjang, lebar):
    return panjang * lebar

def hitung_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_lingkaran(diameter):
    return math.pi * (diameter / 2) ** 2

# Fungsi untuk memilih bentuk secara acak.
def randomizer():
    return random.choice(["segiempat", "segitiga", "lingkaran"])

# Fungsi untuk membuat pesanan name tag.
def buat_nametag(counter):
    jumlah_orang = int(input("Masukkan jumlah pelanggan: "))  # Meminta jumlah pelanggan.
    print()
    
    for pelanggan in range(1, jumlah_orang + 1):
        print(f"======= PELANGGAN {pelanggan}")
        nama_pelanggan = input(f"Masukkan nama pelanggan ke-{pelanggan}: ")  # Meminta nama pelanggan.
        jumlah_nametag = int(input(f"Masukkan jumlah name tag yang ingin dibuat: "))  # Meminta jumlah name tag.
        
        harga_nametag_pelanggan = 0  # Inisialisasi total harga nametag pelanggan.
        
        for nametag_ke in range(1, jumlah_nametag + 1):
            print(f"\nBentuk name tag ke-{nametag_ke} (segiempat/segitiga/lingkaran/random): ", end="")
            bentuk = input().lower()
            while bentuk not in ["segiempat", "segitiga", "lingkaran", "random"]:
                print("Bentuk tidak valid! Masukkan ulang bentuk yang diinginkan (segiempat/segitiga/lingkaran/random): ", end="")
                bentuk = input().lower()
            
            if bentuk == "random":
                bentuk = randomizer()  # Jika bentuk dipilih secara acak, gunakan fungsi randomizer.
                print(f"Bentuk yang terpilih adalah {bentuk}")
                
            if bentuk == "segiempat":
                panjang = float(input("Masukkan panjang (cm): "))
                lebar = float(input("Masukkan lebar (cm): "))
                luas = hitung_segiempat(panjang, lebar)  # Hitung luas segiempat.
            elif bentuk == "segitiga":
                alas = float(input("Masukkan alas (cm): "))
                tinggi = float(input("Masukkan tinggi (cm): "))
                luas = hitung_segitiga(alas, tinggi)  # Hitung luas segitiga.
            elif bentuk == "lingkaran":
                diameter = float(input("Masukkan diameter (cm): "))
                luas = hitung_lingkaran(diameter)  # Hitung luas lingkaran.
            
            print_list_harga()
            jenis_kertas_input = input("Masukkan jenis kertas yang ingin digunakan: ")
            harga_kertas = jenis_kertas.get(jenis_kertas_input, 0)  # Dapatkan harga kertas dari kamus jenis_kertas.
            
            if harga_kertas == 0:
                print("Jenis kertas tidak valid.")
                continue
            
            total_harga_nametag = luas * harga_kertas  # Hitung total harga nametag.
            harga_nametag_pelanggan += total_harga_nametag  # Tambahkan ke total harga nametag pelanggan.
            
            print(f"Sukses membuat pesanan name tag! Nomor antrian name tag ini adalah: {counter + 1}")
            list_nametag.append((nama_pelanggan, bentuk, luas, jenis_kertas_input, total_harga_nametag))  # Tambahkan detail pesanan ke daftar.
            counter += 1
        
        print(f"\nTotal harga kertas yang diperlukan untuk membuat {jumlah_nametag} name tag untuk pelanggan atas nama {nama_pelanggan} adalah Rp{harga_nametag_pelanggan:.2f}\n")
        print("----------------------------------------")

# Fungsi untuk mencetak ringkasan pesanan.
def cetak_summary():
    if not list_nametag:
        print("Belum ada name tag yang terdaftar!\n")
        print("----------------------------------------")
    else:
        nomor_antrian = int(input("Masukkan nomor antrian pesanan yang ingin dilihat: "))
        if nomor_antrian < 1 or nomor_antrian > len(list_nametag):
            print(f"Nomor antrian tidak valid. Harap masukkan nomor antara 1 dan {len(list_nametag)}")
        else:
            print(f"\n======= PESANAN NAME TAG NO. {nomor_antrian}")
            nama, bentuk, luas, bahan_kertas, harga = list_nametag[nomor_antrian - 1]
            print(f"Nama: {nama}")
            print(f"Bentuk name tag: {bentuk}")
            print(f"Bahan Kertas: {bahan_kertas} (Rp{jenis_kertas[bahan_kertas]}/cm^2)")
            print(f"Luas name tag: {luas:.2f} cm^2")
            print(f"Harga name tag: Rp{harga:.2f}")
            print()
            print("----------------------------------------")

running = True
counter = 0

while running:
    print_menu()
    choice = int(input("Pilih fitur yang ingin Anda gunakan: "))  # Meminta pilihan fitur dari pengguna.
    print("----------------------------------------")
    if choice == 1:
        buat_nametag(counter)  # Memanggil fungsi untuk membuat pesanan name tag.
    elif choice == 2:
        cetak_summary()  # Memanggil fungsi untuk mencetak ringkasan pesanan.
    else:
        print("Terima kasih sudah berbelanja di Dek Depe's Name Tag")
        running = False