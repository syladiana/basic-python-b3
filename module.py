def greeting(nama):
    print("Hallo,"+nama)

def ling():
    r = int(input("Masukkan jari-jari : "))
    phi = 22/7
    L = phi*r*r
    text = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,L)
    print(text)

class Person:
    def __init__(self,name,age,nama_lawan):
        self.name = name
        self.age = age
        self.nama_lawan = nama_lawan
    
    def sapa(self):
        print("Hallo namaku "+self.name)
        print("Nama kamu siapa ?")
    
    def salamkenal(self):
        print("Salam kenal "+self.nama_lawan)
        print("Senang bertemu denganmu. sampai jumpa kembali")