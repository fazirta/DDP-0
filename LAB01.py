# Nama: Muhammad Fazil Tirtana
# Kelompok: 02
# Jurusan: Ilmu Komputer
# NPM: 2306274983

# Menampilkan header toko name tag
print("Welcome to Dek Depe's Name Tag Store!\n----------------------------------------")

# Meminta input dari pengguna
nama = input("Nama: ")
tl = input("Tanggal lahir: ")
jurusan = input("Jurusan: ")
motto = input("Motto Hidup: ")
n = int(input("Silahkan masukkan banyak name tag: "))  # Mengubah input menjadi integer sekaligus

luas_total = 0  # Inisialisasi variabel untuk menyimpan luas total name tag

# Loop untuk mengambil input bentuk dan menghitung luas name tag
for i in range(n):
    print("Name Tag {}:".format(i+1))
    bentuk = input("Silahkan masukan bentuk name tag anda: ")
    
    if bentuk == "segiempat":
        panjang = float(input("Masukan panjang (cm): "))
        lebar = float(input("Masukan lebar (cm): "))
        luas_total += panjang * lebar
    elif bentuk == "segitiga":
        alas = float(input("Masukkan panjang alas (cm): "))
        tinggi = float(input("Masukkan tinggi (cm): "))
        luas_total += (alas * tinggi) / 2

# Menampilkan pemisah antara input dan output
print("----------------------------------------")

# Menghitung harga name tag berdasarkan luas total
harga = luas_total * 100

# Menampilkan informasi hasil kepada pengguna
print('Halo {} dari {}.\nLahir pada {} dengan motto "{}" \nTotal biaya untuk memproduksi ke-{} name tag adalah: Rp{}'.format(nama, jurusan, tl, motto, n, harga))

# Menampilkan penutup toko
print("----------------------------------------\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!")
