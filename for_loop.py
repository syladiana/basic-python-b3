fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

banyak_data = len(fruits)
for j in range(banyak_data):
    print(fruits[j])

berapa_data = 3
for j in range(berapa_data):
    fruits.append(input("Input data : "))

print(fruits)