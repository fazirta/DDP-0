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
panjang = float(input("Masukan panjang (cm): "))
lebar = float(input("Masukan lebar (cm): "))

# Menampilkan pemisah antara input dan output
print("----------------------------------------")

# Menghitung luas name tag dan harga
luas = float(int(panjang) * int(lebar))
harga = float(luas * 100)

# Menampilkan informasi hasil
print('Halo {} dari {}.\nLahir pada {} dengan motto "{}" \nLuas name tag {}: {} cm^2\nHarga name tag {}: Rp{}'.format(nama, jurusan, tl, motto, nama, str(luas), nama, harga))

# Menampilkan penutup toko
print("----------------------------------------\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!")
