class Biodata:
    def __init__(self,name,age,alamat,hobi,phone):
        self.name = name
        self.age = age
        self.alamat = alamat
        self.hobi = hobi
        self.phone = phone

    def display(self):
        print("Perkenalkan namaku {}, umurku {} tahun, aku menetap di {}. Hobiku adalah {}.".format(self.name,self.age,self.alamat,self.hobi,self.phone))
        print("Salam kenal!")
        print("phone : "+self.phone)

nama = input("Namamu : ")
umur = input("Umurmu : ")
alamat = input("Alamatmu : ")
hobi = input("Hobimu : ")
phone = input("Phonemu : ")

bio = Biodata(nama,umur,alamat,hobi,phone)
bio.display()