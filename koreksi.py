semuaKontak = []

def menu():
    print("\n--- Menu ---")
    print
    print
    print

def tampilKontak():
    print("\nDaftar kontak:")
    for kontak in semuaKontak:
        print("Nama : "+kontak["nama"])
        print("No Telepon : "+kontak["telpon"])

def tambahKontak():
    