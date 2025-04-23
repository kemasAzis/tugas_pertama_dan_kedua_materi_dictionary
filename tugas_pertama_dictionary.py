print("DAFTAR NAMA BARANG YANG TERTERA DIBAWAH INI")
print(" ' prirng lucky ' ")
print(" ' piring kl ' ")
print(" ' piring sunbird ' ")
print(" ' mangkok ayam ' ")
print(" ' mangkok kl ' ")
print(" ")

# Kamus sederhana menggunakan dictionary
kamus = {
    "pring lucky": "piring ini biasanya sering digunakan dimasyarakat",
    "piring kl": "piring ini berwarna coklat",
    "piring sunbird": "piring ini mempunyai pinggiran list emas",
    "mangkok ayam": "mangkok ayam biasanya untuk soto",
    "mangkok kl": "mangkok ini berwarna coklat"
}

# Meminta input dari pengguna
kata = input("silahkan masukkan jenis barang yang ingin dicari : ").lower()

# Mencari dan menampilkan arti kata
if kata in kamus:
    print(f"jenis barang dari '{kata}' adalah: {kamus[kata]}")
else:
    print(f"Maaf, nama jenis barang yang dicari '{kata}' tidak ditemukan dalam kamus.")
