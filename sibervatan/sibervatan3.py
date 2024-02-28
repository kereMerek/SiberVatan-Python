#kullanıcıdan sayı alın o sayıya kadar olan çift sayıları fonksiyon içinde bulan bir listeye ekleyin ve listeyi yazdırın append range 
# ve list kullanın
#import time 
#sayilar=[]
#x=int(input("Sayı giriniz:"))
#x=x+1


#for x in range(0,x,2):
   # sayilar.append(x)

    

#if x%2==0:
    #sayilar==int
    #print(x,"sayısına kadar olan çift sayılar",sayilar)
def ciftsayi(n):
    ciftsayi_list= []
    for i in range (0,n+1):
        if i % 2==0:
            ciftsayi_list.append(i)
    return ciftsayi_list 
    
limit =int(input("bir üst sınır giriniz"))
print("çift sayılar", cifttsayi_list)