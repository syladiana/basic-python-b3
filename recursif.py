def sapa():
    inputan = input("Lanjut lagi ? ")
    if inputan == "no":
        print("no")
    else:
        sapa()

sapa()