# def lingkaran (Π,r):
#     luas = Π * r * r
#     keliling = Π * 2 * r
#     return luas,keliling

# print(lingkaran(22/7,70))

def lingkaran(jari):
    phi = 22/7
    L = phi*jari*jari
    K = 2*phi*jari
    return L,K

def Luas(jari):
    phi = 22/7
    L = phi*jari*jari
    L = float("{:.2f}".format(Luas(10)))
    return L

def Kel(jari):
    phi = 22/7
    K = 2*phi*jari
    return K

# print(Luas(10))
l = float("{:.2f}".format(Luas(10)))
print(type(l))
# luas = lingkaran(7)[0]
# kel = lingkaran(7)[1]

# print(luas)
# print(kel)

# input_data = float(input("Masukkan Jari - jari : "))
# print(Luas(input_data))
# print(Kel(input_data))



# # lingkaran(7)
# print(lingkaran(10))
# ling = lingkaran(10)
# # print(ling[0])
# # print(ling[1])
# print("Luas     : {:.2f} cm\u00b2".format(ling[0]))
# print("Keliling : {:.2f} cm".format(ling[1]))