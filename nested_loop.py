for i in range(2):
    for j in range(3):
        print("i:{},j:{}".format(i,j))
print("")

for i in range(4):
    print("i = ",i)
    for j in range(3): #0 s/d 3
        print("j = ",j)
        for k in range(2): #0 s/d 3
            print("k = ",k)
            for l in range(1): #0 s/d 3
                print("l = ",l)
    print("")

list_angka = [
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ],
]
for i in list_angka: 
    print("ini i = ",i)
    for j in i:
        print("ini j = ",j)
        for k in j:
            print("ini k = ",k)
    print("")