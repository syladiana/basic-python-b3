sekolah = {
    "kelas7" : 30,
    "kelas8" : 28,
    "kelas9" : 40,
}

jumlah = [0,1,2,3,4]
jumlah[0] = 10
print(jumlah)

print("Jumlah anak kelas 7 adalah {}".format(sekolah["kelas7"]))
print("Jumlah anak kelas 8 adalah {}".format(sekolah["kelas8"]))
print("Jumlah anak kelas 9 adalah {}".format(sekolah["kelas9"]))

sekolah["kelas8"] = 35
print("Jumlah anak kelas 7 adalah {}".format(sekolah["kelas7"]))
print("Jumlah anak kelas 8 adalah {}".format(sekolah["kelas8"]))
print("Jumlah anak kelas 9 adalah {}".format(sekolah["kelas9"]))

# for a in sekolah:
#     print(a)

for x in sekolah:
    print(sekolah[x]) #sekolah["kelas7"]