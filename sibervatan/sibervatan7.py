#1-)saatlik çalışanı
#2-)komisyon çalışanı
#saatlik işçiye çalıştığı ilk 40 saat için saat başına 50TL , 40 saatin üzerindeki her saat için
#(fazla mesai saatlerinden) "bir buçuk saat" (50TL saatlik ücretin 1,5 katı) ödeme yapılır, komisyon çalışanı
#ise 500tl ye ek olarak aylık satışlarının %5,5 ini alıyor
#program çalışan türüne göre maaş hesaplarına gerçekleştirmek için hesaplamasaatlik() ve hesaplakomisyon() üzere
#İKİ (2) fonksiyon gerçekleştirmelidir Fonksiyonların her biri hesaplanan maaş tutarı döndürür
#programın girdisi ödeme kodu ve ödeme koduna dayalı olarak her çalışanın maaşını hesaplamak için gereken
#uygun bilgilerdir (saatlik işçiler için toplam çalışma saati komisyonlu çalışanlar içinde satış mikratı girilmelidir)
#girilen ödeme kodu geçersizse uygun bir hata mesajı götüntüleyin kullanıcıya tekrar denetin
"""
try:
    import time
    print(" ----HOŞ GELDİNİZ----")
    print(" --LÜTFEN SINIF SEÇİNİZ--")
    print("1-) SAATLİK ÇALIŞANI")
    print("2-) KOMİSYON ÇALIŞANI")
    secenek1=input("Komisyon çalışanı mısınız ? yada Saatlik çalışan mı ? :")
    if secenek1=="1":
        s_saat=int(input("Kaç saat çalıştığınızı giriniz:"))
        if s_saat<=40:
            para=s_saat*50
            print("Alıcağınız ücret:",para)
        elif s_saat>40:
            x=(s_saat-40)*75
            f_para=(s_saat*50)+x
            print("Alıcağınız tutar:",f_para)
            #fazladan_para=s_saat+x
            #para=(s_saat*50)+fazladan_para
            #print("Alıcağınız ücret:",para)
        else:
            print("Lütfen geçerli bir sayı giriniz!!")
    if secenek1=="2":
        satis=input("Satış yaptınız mı ? :")
        satis2=int(input("Kaç tane satış yaptınız :"))
        if satis=="evet":
            ek_para=(satis2*0.05)+500
            para=ek_para+500
            print("Maaşınız:",ek_para)


except KeyboardInterrupt:
    print("Lütfen bir sayı giriniz:")
except TypeError:
    print("Bir şeyler ters gitti!!")
except SyntaxError:
    print("Bir hata oluştu")
except ValueError:
    print("Lütfen geçerli sayı bir sayı giriniz:")
except SyntaxWarning:
    print("Lütfen geçerli bir karakter giriniz")

"""
    

#günlük ortalama sıcaklık değerleri -20 ile 40 derece arasında da dır
# (-20) - (0)
# 0 - 20
# 20 - 40

try:
    import time
    sayac=0
    sayac1=0
    sayac2=0
    liste=[5,-15,25,12,2,30,18,-5,35,-18,8]
    for i in liste:
        if -20 <= i <= 0: # 0 ile -20 arasında ki sayıları kontrol ediyor
            sayac+=1      #eğer bu aralıkta bir eleman varsa sayacı 1 arttırıyor
            
        elif 0<= i <=20: # 0 ile +20 arasında ki sayıları kontrol ediyor 
            sayac1+=1    # eğer bu aralıkta bir eleman varsa sayacı 1 arttırıyor
            
        elif 20<= i <=40:# 20 ile 40 arasında ki sayıları kontrol ediyor 
            sayac2+=1    #eğer bu aralıkta bir eleman varsa sayacı 1 arttırıyor
            
        else:
            print("Geçerli bir değer giriniz!!")
    
    print("0 ile -20 arasındaki sayılar",sayac)
    print("0 ile 20 arasında ki sayılar",sayac1)
    print("20 ile 40 arasında ki sayılar:",sayac2)



finally:
    print("Program kapatılıyor...")
    time.sleep(2.5)