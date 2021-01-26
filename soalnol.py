Nama_kontak = []
No_kontak = []

print("Selamat datang!")
print("---Menu---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")

while True :
    pilih = int(input("Pilih menu: "))
    print()
    if(pilih == 1):
        print("Daftar kontak: ")
        if(len(Nama_kontak)==0):
            for x in range(len(Nama_kontak)):
                print("Nama: {}".format(Nama_kontak[x]))
                print("No telepon: {}".format(No_kontak[x]))
                print()
        else:
            print("Kontak belum ditambahkan")
            print()

    elif(pilih == 2):
        nama_kontak.append(input("Nama: "))
        no_kontak.append(input("No_telepon: "))
        print("Kontak berhasil ditambahkan")
        print()

    elif(pilih == 3):
        print("Program selesai, sampai jumpa!")
    elif(pilih > 3):
        print("Menu tidak tersedia")