# print(10<6)
# print(10>6)
# print(10==6)

# > : lebih dari
# < : kurang dari
# == : sama dengan
# >= : lebih besar sama dengan
# <= : kurang dari sama dengan

# and : benar keduanya
# or : pilih satu
# != : tidak sama dengan

a = int(input("masukkan nilai teori : "))
b = int(input("masukkan nilai praktek : "))
# if(kondisi):

if((a>=70) and (b>=70)):
    print("Selamat, anda lulus!")
elif((a>=70) and (b<70)):
    print("Anda harus mengulang ujian praktek.")
elif((a<70) and (b>=70)):
    print("Anda harus mengulang ujian teori.")
elif((a<70) and (b<70)):
    print("Anda harus mengulang ujian teori dan praktek.")