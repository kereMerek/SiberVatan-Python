def toplam(num1, num2):
    return num1 + num2

def cikarma(num1, num2):
    return num1 - num2

def carpma(num1, num2):
    return num1 * num2

def bolme(num1, num2):
    return num1 / num2

def faktoriyel(num):
    if num == 0:
        return 1
    else:
        return num * faktoriyel(num - 1)



print("-*-*-*-*- Hoşgeldiniz -*-*-*-*-*-*-")
print("Toplama için 1")
print("Çıkarma için 2")
print("Çarpma için 3")
print("Bölme için 4")
print("Faktöriyel hesaplama için 5")
print("Çıkmak için 6")
secenek=int(input("lütfen tercihinizi yazınız:"))


if(secenek==1):
  num1=int(input("birinci sayıyı giriniz:"))
num2=int(input("ikinci sayıyı giriniz:"))
secim=input("hangi işlem olsun:")
if secim =="toplama":
   print(num1+num2)
elif secim=="cıkarma":
   print(num1-num2)

elif secim=="carpma":
    print(num1*num2)

elif secim=="bolme":    
    print(num1/num2)
elif secim=="faktöriyel":
    print()


else:
    print("düzgün yazmayan topal ahmet gibi olsun")