""""
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)
sayi = int(input("faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))
print(faktoriyel(sayi))
"""
"""
x="global değildir"

def fuction():
    x= "local değildir"
    print(x)
fuction()
print(x)

"""


#print(a) name error
#int("topal amed") valu error
#print(kayranın "annesi") 
"""
try:
    x=int(input("Birinci sayıyı giriniz:"))
    y=int(input("İkinci sayıyı giriniz:"))
    print(x/y)
except ValueError:
    print("Lütfen sayı giriniz")
except SyntaxError:
    print("Lütfen geçerli bir değer giriniz")
"""
import re
def parola_kontrol(parola):
    if len(parola)<=8:
        raise Exception("Parola en az 8 karakterli olmalı")
    elif not re.search("a-z",parola):
        raise Exception("Parola küçük harfler icermelidir")
    elif not re.search("A-Z",parola):
        raise Exception("Parola büyük harf içermelidir")

password=int=(input("Oluşturmak istediğiniz parolayı giriniz:"))
try:
    parola_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("Parola oluşturma hatalı")


#reguler exception şeyine bak ÖDEV özel karakterleri kabul edicek şekilde yap