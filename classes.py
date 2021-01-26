class Myclass:
    x = 5
    y = 10
    Luas_Persegi = x*y
    Luas_lin = 22/7*x*x

def Myclasses():
    x = 5
    y = 10
    Luas_Persegi = x*y
    Luas_lin = 22/7*x*x
    return Luas_Persegi,Luas_lin
    
p1 = Myclass()
p2 = Myclass()

print(p1.Luas_Persegi)
print(p1.Luas_lin)
print(p2.Luas_lin)
print(p2.Luas_lin)
print(Myclasses()[0])
print(Myclasses()[1])