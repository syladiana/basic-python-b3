while True:
    print("--- Menu ---")
    print("1. Daftar kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        read = open("file.txt","r")
        data = read.readlines()
        # print(data)
        # for i in data:
        #     splitting = i.split("\t")
        #     print(splitting)
        # for i in splitting:
        #     print(i)
        for i in range(0,len(data),3):
            print("Nama : {}Telp : {}Alamat: {}".format(data[i],data[i+1],data[i+2]))
        read.close()
    elif pilihan == 2:
        create = open("file.txt","a")
        nama = input("Masukkan nama : ")
        telepon = input("Nomor telp : ")
        alamat = input("Alamat      : ")
        create.write(nama+"\n")
        create.write(telepon+"\n")
        create.write(alamat+"\n")
        create.close()
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia\n")