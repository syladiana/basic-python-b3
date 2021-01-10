angka = "ini adalah angka 10"
angka_list = ["ini","adalah","angka","10"]

# #sebelum
print(angka_list)

#sesudah ditambah
angka_list.append("loh rek")
print(angka_list)

#edit
angka_list[3] = 100
print(angka_list)

hasil = ""
angka = 0
for x in range(0, len(angka_list)): #range(0,4)
    hasil = hasil+angka_list[x]+""