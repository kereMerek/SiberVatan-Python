#open("Yeni dosya.txt","w")

# "w" Write -> yazma modu  , yoksa oluşturur içeriği silip ekleme yapar
# "a" Append -> ekleme modu  
# "x" Create -> oluşturma modu , aynısı varsa hata verir
# "r" Read -> okuma modu 


#file= open("yenidosya.txt","w")
#print(file)
#file.close()
#file_dizin = open("C:/Users/kerem/OneDrive/Masaüstü/Visual Studio/siber_vatan/yenidosya.txt","w")
#file_dizin.close()

#file = open("C:/Users/kerem/OneDrive/Masaüstü/Visual Studio/siber_vatan/yenidosya.txt","w",encoding="utf-8")
#file.write("Topal ahmet")
#file = open("C:/Users/kerem/OneDrive/Masaüstü/Visual Studio/siber_vatan/yenidosya.txt","a",encoding="utf-8")
#file.write("\nSağlam ahmet")
#file.close()

#file = open("C:/Users/kerem/OneDrive/Masaüstü/Visual Studio/siber_vatan/topal_ahmet.txt","x")
#file.close
"""
try:
    x = input("Dosya adını giriniz:")
    file = open(x,"x")
except FileExistsError:
    print("Dosya ztn mevcut")
except FileNotFoundError:
    print("Dosya bulunamadı")
except NameError:
    print("Dosya adını doğru giriniz")

"""
"""
try:
    dosya = open("yeni_dosya.txt","x")
    print(dosya)
except FileExistsError:
    print("Dosya zaten mevcut")
except FileNotFoundError:
    print("Dosya bulanmıyor")
except FileExistsError:
    print("Dosya adı hatalı")
except NameError:
    print("Dosya bulunamadı")
finally:
    print("Dosya kapandı")
    dosya.close()

"""