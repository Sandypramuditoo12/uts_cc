# Aplikasi Perpustakaan Sederhana dengan CRUD
# Menggunakan Python (tanpa database)

perpustakaan = []  # List untuk menyimpan data buku

def tampilkan_buku():
    if not perpustakaan:
        print("\n=== Tidak ada buku dalam perpustakaan ===")
    else:
        print("\n=== Daftar Buku ===")
        for i, buku in enumerate(perpustakaan, start=1):
            print(f"{i}. Judul: {buku['judul']} | Penulis: {buku['penulis']} | Tahun: {buku['tahun']}")

def tambah_buku():
    print("\n=== Tambah Buku ===")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun = input("Masukkan tahun terbit: ")
    buku = {"judul": judul, "penulis": penulis, "tahun": tahun}
    perpustakaan.append(buku)
    print("Buku berhasil ditambahkan!")

def update_buku():
    tampilkan_buku()
    if perpustakaan:
        try:
            index = int(input("\nPilih nomor buku yang ingin diupdate: ")) - 1
            if 0 <= index < len(perpustakaan):
                print("Kosongkan jika tidak ingin mengubah.")
                judul = input("Judul baru: ") or perpustakaan[index]['judul']
                penulis = input("Penulis baru: ") or perpustakaan[index]['penulis']
                tahun = input("Tahun baru: ") or perpustakaan[index]['tahun']
                perpustakaan[index] = {"judul": judul, "penulis": penulis, "tahun": tahun}
                print("Buku berhasil diperbarui!")
            else:
                print("Nomor buku tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")

def hapus_buku():
    tampilkan_buku()
    if perpustakaan:
        try:
            index = int(input("\nPilih nomor buku yang ingin dihapus: ")) - 1
            if 0 <= index < len(perpustakaan):
                perpustakaan.pop(index)
                print("Buku berhasil dihapus!")
            else:
                print("Nomor buku tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")

def menu():
    while True:
        print("\n=== Aplikasi Perpustakaan ===")
        print("1. Tampilkan Buku")
        print("2. Tambah Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_buku()
        elif pilihan == "3":
            update_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi perpustakaan!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan program
menu()
