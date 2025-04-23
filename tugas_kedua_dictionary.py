# Program Manajemen Kontak Sederhana

kontak = {}  # Dictionary untuk menyimpan kontak

def tampilkan_menu():
    print("\nMenu:")
    print("1. silahkan ketik nomor 1 untuk tambah kontak ")
    print("2. silahkan ketik nomor 2 untuk Hapus kontak ")
    print("3. silahkan ketik nomor 3 untuk Cari kontak ")
    print("4. silahkan ketik nomor 4 untuk Tampilkan semua kontak")
    print("5. silahkan ketik nomor 5 untuk Keluar ")

def tambah_kontak():
    nama = input("silahkan Masukkan nama kontak: ").strip()
    if nama in kontak:
        print(f"Kontak dengan nama '{nama}' sudah ada.")
    else:
        nomor = input("silahkan Masukkan nomor telepon: ").strip()
        kontak[nama] = nomor
        print(f"Kontak '{nama}' berhasil ditambahkan.")

def hapus_kontak():
    nama = input("silahkan Masukkan nama kontak yang ingin anda hapus: ").strip()
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak '{nama}' berhasil dihapus.")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def cari_kontak():
    nama = input("silahkan masukkan nama kontak yang ingin anda cari: ").strip()
    if nama in kontak:
        print(f"Nomor telepon '{nama}': {kontak[nama]}")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def tampilkan_semua_kontak():
    if kontak:
        print("\nDaftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"- {nama}: {nomor}")
    else:
        print("Belum ada kontak yang disimpan.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ").strip()
    
    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        hapus_kontak()
    elif pilihan == "3":
        cari_kontak()
    elif pilihan == "4":
        tampilkan_semua_kontak()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")
 