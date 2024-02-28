
#HATALI DENEME
"""
try:
    set[233,45,777,81,99999,36,90,88,11,61]
    A=[]
    sayi=233,45,777,81,9999,36,90,88,11,61

    for sayi in range(0,sayi,1):
        if set==sayi:
            print("Sayılar birbirine eşittir")
            A.append(sayi)
        elif set!=sayi:
            print("Sayılar birbirine eşittir değildir")
            A.append(sayi)
        else:
            print("HATA/ERROR")
            

"""

"""
def sayiKontrol(sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str)) == 1:
        return 1
    else:
        return 0

A = [233, 45, 777, 81, 99999, 36, 90, 88, 11, 61]

for sayi in A:
    if sayiKontrol(sayi):
        print(f"{sayi} Sayılar birbirine eşittir")
    else:
        print(f"{sayi} Basamaklar birbirine eşit değildir")
"""
"""""
liste = [10,20,30]
print(type(liste))

"""
"""
class Person:
    def __init__(self,name,lname,adres,dogum_yil):
        self.name=name
        self.lname=lname
        self.adres=adres
        self.dogum_yil=dogum_yil
        self.yas=2024-dogum_yil

p1=Person(name="Ahmet",lname="Topal",adres="100. year",dogum_yil=1992)
print("Merhaba benim adım",p1.name,"ben",p1.dogum_yil,"doğumluyum",p1.adres,"yaşım",p1.yas)
"""

"""
#BENİM YAPTIĞIM
class Daire:
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
        self.daire = 2 * pi * r  
    def intro(self):
        print("Dairenin çevresi:", self.daire)
d1 = Daire(pi=3, r=5,)
d1.intro()
"""
        

#hocanın yaptığı
class Daire:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def cevre_hesaplama(self):
        return 2*self.pi*self.r
d1 = Daire(5)
print(d1.cevre_hesaplama())
