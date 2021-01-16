for i in range(5):
    if i == 3:
        break
    print(i)

text = input("Masukkan code:")
while True:
    if text == "stop":
        break
    print("Hasil : {}".format(text))
    print("======================")
    text = input("Masukkan code:")