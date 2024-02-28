#5 elemana sahip bir liste oluşturunuz
"""
try:
    liste=[]

    x=int(input("Kaçta biteceğini giriniz:"))
    y=int(input("Kaçta başlayacağını giriniz:"))
    for i in range(y,x+1):
        if i%3==0:
            liste.insert(1,i)
        elif i%3==1:
            liste.append(i)
        else:
            print("Lütfen sayı giriniz!!")
    print(liste)

except ValueError:
    print("Geçerli bir değer giriniz!!")
"""

#append listenin sonuna
#insert ise listenin başına ekleme yapar



"""
class Kisi:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
    def __str__(self):
        return f"{self.isim}{self.yas}"

k1=Kisi(isim="Ahmet ",yas=35)
print(k1)
"""

"""

class Soru:
    def __init__(self,soru1,soru2,soru3,sayac):
        self.soru1=soru1
        self.soru2=soru2
        self.soru3=soru3
        self.sayac=sayac
    def cevaplar(self):
        x=input("Türkiye nin başkenti neresidir:")
        y=input("Karabük ün plakası kaçtır:")
        z=input("Türkiye hangi kıtaya daha yakındır:")
        if x==p1.soru1:
            print("Doğru bildiniz")
            sayac=sayac+1
        elif y==p1.soru2:
            sayac=sayac+1
            print("Doğru bildiniz")
        elif z==p1.soru3:
            sayac=sayac+1
            print("Doğru bildiniz")
        
        print("Doğru bilinen soru sayısı:",p1.sayac)


p1=Soru(soru1="Ankara",soru2="78",soru3="Asya",sayac=0)

"""

class Soru:
    def __init__(self,soru,cevap):
        self.soru=soru
        self.cevap=cevap
    def dogru_mu(self,tahmin):
        return self.cevap==tahmin
soru1 = Soru("Türkiyenin başkenti Neresidir ? :","Ankara")
soru2 = Soru("En kalabalık şehir ? :","İstanbul")
soru3 = Soru("Türkiye nin en güzel şehiri ? :","Konya")
sayac=0

sorular=[soru1,soru2,soru3]

for i in sorular:
    cevap=input(i.soru)
    if i.dogru_mu(cevap):
        sayac+=1
print("Doğru cevap sayısı:",sayac)







