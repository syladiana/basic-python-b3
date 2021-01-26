semuaKontak = []

def menu():
    print("\n--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def tampilKontak():
    print("\nDaftar kontak:")
    for kontak in semuaKontak:
        print("Nama : "+kontak["nama"])
        print("No Telepon : "+kontak["telpon"])

def tambahKontak():
    nama = str(input("\nMasukkan Data\nNama : "))
    telpon = str(input("No Telepon : "))      
    kontak = {
        "nama" : nama,
        "telpon" : telpon,
    }
    semuaKontak.append(kontak)
    print("Kontak berhasil ditambahkan")
    
print("\nSelamat datang!")  
while True:
    menu()
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        tampilKontak()
    elif pilihan == 2:
        tambahKontak()
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia\n")