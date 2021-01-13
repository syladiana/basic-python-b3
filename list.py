angka = "ini adalah angka 10"
angka_list = ["ini","adalah","angka","10"]

#sebelum
print(angka_list)

#sesudah ditambah
angka_list.append("loh rek")
print(angka_list)

#edit
angka_list[3] = 100 
print(angka_list)

hasil = ""
angka = 0
for x in range(0,len(angka_list)): #range(0,4)
    hasil = hasil+angka_list[x]+" "
    print(hasil)
print(hasil)

for x in angka_list:
    print(x)

angka = angka_list[0]+" "+angka_list[1]+" "+angka_list[2]+" "+angka_list[3]
print(angka)

# angka*=1
# angka = angka * 1