'''
Bu kısmda yapacaklarım;
* karşılaştırma kısmındaki sorunların düzeltilmesi
* bulunan kitabı sesli okuma sistemi
'''

# SABİT NOTLAR: arama kısmına 3 hane yazında sadece artvine özel bir barkod kütüphane kodu içermiyor onun için 3 hanelilerde kod var bilginize...

# AMAÇ_1: Arama algoritmasını düzenlemek ve daha iyi bir arama algoritmasına geçerek aramada hız kazanmak*

# EKLENECEK_1: Tarih kısmını gün/ay/yıl şeklinde yapılacak *
'''*****okuyucudaki kitaplarda ve kayıt dosyasında en sonda kesinlikle bir tane boşluk olması gerekiyor aksi halde karşılaştırma kısmı düzgün çalışmıyor'''

# bitirişte kayıt alması için bir barkod tanımlaancak: 121101100101107 *

# eklememe barkodu tanımlanacak: 0000000110111 *

# kütüphane kodunu otomatikleştirme *

# kitap listesi 1. eleman varsayılandan farklı kontrollerini yap *

# kitap sayar tam otomatik versiyon-string değer-şifreli *

# okuyucunun elinde de kitap var, bunları da kayıda ekle ya da son belgeden (listede olup kayıtta olmayanlar) sil *

# aynı kitaptan var mı varsa sil: belgenin ilk elemanıyla ondan sonraki elemanlarına bakarız.. ** yeni kararım bu işlemi daha sonraya bırak ya da koyma kardeşim *

# yedek klasörü kontrol ve başka bir yere daha ekleme bilgilendirmede olması gereken gereksinimleri yazacağız *

# renklendirme *

# lisanslama *

# arana bulunamayınca uyarı versin

# düşülen kitapları farklı bir renkte yazsın DÜŞÜLDÜ *




import os
import time
import shutil
import colorama
from datetime import datetime
from colorama import Fore, Back, Style
import sys
colorama.init()

def comparison(listeDizi,bakilacakDizi,kayitDosyasi):
    try:
        bulundu_mu = 0
        for x in listeDizi:
            for y in bakilacakDizi:
                if x == y:
                    bulundu_mu = 1
                    break
            if bulundu_mu == 0:
                kayitDosyasi.write(x)
            bulundu_mu = 0
        print(Fore.GREEN, "Karşılaştırma işlemi tamamlandı ve dosyaya yazildı...\n\n", Style.RESET_ALL)
        time.sleep(1)
    except:
        print("\a")
        print(Fore.RED,"Karşılaştırma işlemiinde beklenmeyen bir hata oluştu...",Style.RESET_ALL)



devam=1
hata=0

# Lisanslama işlemi
lisans_date=2024
currently_date=datetime.now()
currently_year=currently_date.year

if str(currently_year)>=str(lisans_date):
    print(Fore.RED)
    print("\n\n************\n")
    print("\a")
    print("Program açılırken hata oluştu. Lütfen geliştiricinizle iletişime geçiniz.")
    print("Mail adres: kmuhammetriza@gmail.com")
    print("\n************")
    print(Style.RESET_ALL)
    sys.exit()


date=datetime.now()
print(Fore.CYAN)
print("Şu anki tarih: ",date,"\n")


yedek_barkodu=121101100101107
eklememe_barkodu=1111111110111
admin_panel=97100109105110105110
eklememe=0

okunacakMetinBelgesi = open("liste.txt", mode='r', encoding='utf-8')
kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')
kayıtMetinBelgesi.close()


liste = okunacakMetinBelgesi.readlines()
uzunluk = (len(liste))
i = 0



# ---- Bilgi kütüphane kodu kısmı

libraryCode_belge=open("Bilgi.txt","r")
libraryCode_dizi=libraryCode_belge.readlines()
libraryCode_split=libraryCode_dizi[0].split(":")

# kütüphane kodu
while(True):
    if len(libraryCode_split)!=2 or libraryCode_split[1].strip()=="":
        print("\a")
        print(Fore.RED,"HATA: Kütüphane kodu 'Bilgi' dosyasına, doğru bir şekilde girilmesi gerekiyor.",Style.RESET_ALL)
        sys.exit()

    else:
        libraryCode = libraryCode_split[1].strip()
        print("Kütüphane Kodu: ", libraryCode)
        break

print("\nListedeki Kitap Sayısı: ",uzunluk,"\n")
print(Style.RESET_ALL)


while(devam!=0):
    aranan_deger_uzunlugu = 0
    while(aranan_deger_uzunlugu!=12 or hata!=0):
        print("\n\n\n\n")

        print(Fore.WHITE + Back.BLACK)
        aranan=input("{devam}- Aramak istediğiniz barkod numarasını giriniz: ".format(devam=devam))
        print("\n",Style.RESET_ALL)
        aranan_deger_uzunlugu= len(aranan)


        # admin kısmı giriş
        admin_login=0
        if str(aranan)=='admin' or aranan==str(admin_panel):
            admin_login=1
            while True:
                print(Fore.BLUE)
                password=input("Admin şifresini giriniz (çıkış/exit): ")
                print(Style.RESET_ALL)
                if password=="exit" or password=="çıkış":
                    break
                if password=="mrk":
                    print(Fore.GREEN,"Giriş Başarılı...\n",Style.RESET_ALL)

                    exit=0
                    choose_control = 0
                    while choose_control == 0 or (choose != 1 and choose != 2 and choose!=3):
                        print(
                            Fore.MAGENTA,
                            "Lütfen seçin...",Style.RESET_ALL,Fore.BLUE,"\n\t1- Raflarda olmayan kitapları tespit etme işlemi(liste-kayıt karşılaştırılması)\n"
                            "\t2- Okuyucudaki kitapları raflarda olmayan kitaplardan çıkarma işlmei (kayıt-okuyucudaki kitapların karşılaştırılması\n"
                            "\t3- Çıkış",)
                        choose = input("Seçiminizi giriniz (1, 2 veya 3): ")
                        print(Style.RESET_ALL)
                        try:
                            choose = int(choose)
                            choose_control = 1
                            print()
                        except:
                            print("\a")
                            print(Fore.RED,"Yanlıca sayısal değerler girilebilir. Tekrar seçim yapın...\n",Style.RESET_ALL)
                            choose_control = 0

                        if choose == 1:
                            kitap_listesi_belgesi = open("liste.txt", "r",
                                                         encoding="utf-8")  # bu kısımlarda başta encoding kısmını yazmadığımdan hata aldım. "'charmap' codec can't decode byte 0x9e in position 125: character maps to <undefined>"
                            kitap_listesi_belgesi_dizi = kitap_listesi_belgesi.readlines()

                            kayıtlı_kitap_listesi = open("kayıt.txt", "r", encoding="utf-8")
                            kayıtlı_kitap_listesi_dizi = kayıtlı_kitap_listesi.readlines()

                            kayit_disi1 = open("kayıt dışı1.txt", "w", encoding="utf-8")

                            print(Fore.CYAN,"Kitap listesi kitap adedi: ", len(kitap_listesi_belgesi_dizi))
                            print(" Kayıt listesi kitap adedi: ", len(kayıtlı_kitap_listesi_dizi),Style.RESET_ALL)
                            comparison(kitap_listesi_belgesi_dizi, kayıtlı_kitap_listesi_dizi, kayit_disi1)
                            kitap_listesi_belgesi.close()
                            kayıtlı_kitap_listesi.close()
                            kayit_disi1.close()
                            choose_control = 0
                            continue

                        elif choose == 2:
                            kayit_disi1 = open("kayıt dışı1.txt", "r", encoding="utf-8")
                            kayit_disi1_dizi = kayit_disi1.readlines()

                            okuyucudaki_kitap_listesi = open("okuyucudaki kitaplar.txt", "r", encoding="utf-8")
                            okuyucudaki_kitap_listesi_dizi = okuyucudaki_kitap_listesi.readlines()

                            kayit_disi2 = open("kayıt dışı2.txt", "w", encoding="utf-8")

                            print(Fore.CYAN,"Okuyucu hariç kitap adedi: ", len(kayit_disi1_dizi))
                            print(" Okuyucudaki kitap adedi: ", len(okuyucudaki_kitap_listesi_dizi),Style.RESET_ALL)
                            comparison(kayit_disi1_dizi, okuyucudaki_kitap_listesi_dizi, kayit_disi2)
                            kayit_disi1.close()
                            okuyucudaki_kitap_listesi.close()
                            kayit_disi2.close()
                            choose_control = 0
                            continue

                        elif choose==3:
                            exit=1
                            break
                    if exit==1:
                        break

        if admin_login==1:
            continue

        try:
            aranan=int(aranan)
        except ValueError:
            print("\a")
            print(Fore.RED,"Sadece sayısal değerler arayabilirsiniz !!!",Style.RESET_ALL)
            continue


        if int(aranan)==yedek_barkodu:
            try:
                okunacakMetinBelgesi = open("okunanlar.txt", mode="a", encoding="utf-8")
                an = datetime.now()
                yil = an.year
                ay = an.month
                gün = an.day
                saat = an.hour
                dakika = an.minute
                tarih = str(gün) + "." + str(ay) + "." + str(yil) + "_" + str(saat) + ";" + str(dakika)
                shutil.copy("kayıt.txt", "Yedek/" + "kayıt " + tarih + ".txt")
                shutil.copy("okunanlar.txt", "Yedek/" + "okunanlar " + tarih + ".txt")
                kayıtMetinBelgesi.close()
                okunacakMetinBelgesi.close()
                print(Fore.GREEN, "Yedekleme İşlemi Başarılı...", Style.RESET_ALL)
                continue
            except:
                print(Fore.RED,"Yedek alma şlemi başarısız oldu", Style.RESET_ALL)

        # aranan değerden son rakamı silme komutu
        if(len(str(aranan))!=5 and len(str(aranan))!=4 and len(str(aranan))!=3):
            aranan=str(int(aranan/10))
            aranan_deger_uzunlugu= len(aranan)

        if(aranan_deger_uzunlugu==5):
            aranan=str(aranan)
            aranan=libraryCode+aranan
            aranan_deger_uzunlugu=len(aranan)

        elif(int(aranan_deger_uzunlugu)==4):
            aranan = str(aranan)
            aranan = libraryCode+"0"+aranan
            aranan_deger_uzunlugu = len(aranan)

        elif(aranan_deger_uzunlugu == 3):
            ## bu kısım artvine özel. aranan  3 hane başka 320 yok ondan dolayı bu şekilde arama yapılamasının istedik
            #if int(aranan)==320:
            #    aranan=100000000320
            #    break
            aranan = str(aranan)
            aranan = libraryCode+"00" + aranan
            aranan_deger_uzunlugu = len(aranan)

        if(aranan_deger_uzunlugu!=12):
            print("\a")
            print(Fore.RED,"Barkod uzunluğu 12 hane olmalı",Style.RESET_ALL)
            continue

        okunanBarkod=open("okunanlar.txt", mode='r', encoding='utf-8')
        aranan_varmi=okunanBarkod.read().find(str(aranan))
        if(aranan_varmi==-1):
            okunanBarkod=open('okunanlar.txt', mode='a', encoding='utf-8')
            okunanBarkod.write(str(aranan)+"\n")
            okunanBarkod.close()
            hata=0
        else:
            i=0

            kayıtMetinBelgesi = open("kayıt.txt", mode='r', encoding='utf-8')
            liste_kayıt = kayıtMetinBelgesi.readlines()
            uzunluk_kayıt = len(liste_kayıt)
            while(i!=uzunluk_kayıt):
                kayıtMetinBelgesi = open("kayıt.txt", mode='r', encoding='utf-8')
                if str(int(aranan)) in liste_kayıt[i]:
                    print(Fore.YELLOW,"\n",aranan," aranan barkod daha önce kaydedilmiş !",Style.RESET_ALL)
                    print("Kaydedilen kitap: ",Fore.CYAN,liste_kayıt[i],Style.RESET_ALL)
                i=i+1

            # ARAMA KISMI 1

            barkod_listesi = open("barkodlar.txt", mode="r", encoding="utf-8")
            barkod_listesi_dizi = barkod_listesi.readlines()
            kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')

            max_value = len(liste)
            min_value = -1
            kontrol = 0
            aranan = int(aranan)
            while (max_value - min_value > 1):
                bakilan = int((max_value + min_value) / 2)
                if int(barkod_listesi_dizi[bakilan]) == aranan:
                    kontrol = 1
                    if  "DÜŞÜLDÜ" in str(liste[bakilan]):
                        print("\a")
                        print(Fore.RED,"Düşülmüş Kitap")
                        print(Fore.CYAN, "  *--------------")
                        print(Fore.RED, liste[bakilan], Style.RESET_ALL, Fore.CYAN, "*--------------")
                    else:
                        print(Fore.YELLOW, "  *--------------")
                        print(Fore.CYAN, liste[bakilan], Style.RESET_ALL, Fore.YELLOW, "*--------------")

                    print(Fore.MAGENTA)
                    ekle = input("Yeniden eklemek istiyor musunuz? (Ekle: Enter)(Ekleme: e): ")
                    print(Style.RESET_ALL)

                    if (ekle) == "e":
                        print(Fore.RED, " ×  Eklenmedi ×  ", Style.RESET_ALL)
                    elif str(ekle) == str(eklememe_barkodu):
                        print(Fore.RED, " ×  Eklenmedi ×  ", Style.RESET_ALL)
                    else:
                        kayıtMetinBelgesi.write(liste[bakilan])
                        print(Fore.GREEN, " * Ekleme başarılı * ", Style.RESET_ALL)
                        kayıtMetinBelgesi.close()

                        kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')
                        devam = devam + 1
                        if (devam % 100 == 0):
                            an = datetime.now()
                            yil = an.year
                            ay = an.month
                            gün = an.day
                            saat = an.hour
                            dakika = an.minute
                            tarih = str(gün) + "." + str(ay) + "." + str(yil) + "_" + str(saat) + ";" + str(dakika)
                            shutil.copy("kayıt.txt", "Yedek/" + "kayıt " + tarih + ".txt")
                            kayıtMetinBelgesi.close()

                    break
                elif int(barkod_listesi_dizi[bakilan]) < aranan:
                    min_value = bakilan
                elif int(barkod_listesi_dizi[bakilan]) > aranan:
                    max_value = bakilan

            if kontrol == 0:
                print("\a")
                print(Fore.RED,"Barkod bulunamadı: ", aranan,Style.RESET_ALL)

            #i=0
            #while (i != uzunluk):
            #    kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')
            #    if str(int(aranan)) in liste[i]:
            #        print("Şu anda bulunan kitap: ",Fore.CYAN,liste[i],Style.RESET_ALL)
            #        print(Fore.MAGENTA)
            #        ekle = input("Yine de eklemek istiyor musunuz?  (Enter)(e): ")
            #        print(Style.RESET_ALL)
            #        if (ekle == "e"):
            #            print(Fore.RED," ×  Eklenmedi ×  ",Style.RESET_ALL)
            #        else:
            #            kayıtMetinBelgesi.write(liste[i])
            #            print(Fore.GREEN," * Ekleme başarılı * ",Style.RESET_ALL)
            #            kayıtMetinBelgesi.close()
            #            devam = devam + 1
            #            if(devam % 3==0):
            #                an = datetime.now()
            #                yil=an.year
            #                ay=an.month
            #                gün = an.day
            #                saat = an.hour
            #                dakika = an.minute
            #                tarih = str(gün) + "." + str(ay) + "." + str(yil) + "_" + str(saat) + ";" + str(dakika)
            #                shutil.copy("kayıt.txt", "Yedek/"+"kayıt " + tarih + ".txt")
            #        break
            #    if (i == uzunluk - 1):
            #        print(Fore.RED,"Aranan barkod bulunamadı !!!",Style.RESET_ALL)
            #    i = i + 1

            hata=1
            continue


    # ARAMA KISMI 2


    barkod_listesi = open("barkodlar.txt", mode="r", encoding="utf-8")
    barkod_listesi_dizi = barkod_listesi.readlines()
    kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')

    max_value=len(liste)
    min_value=-1
    kontrol=0
    aranan=int(aranan)
    while(max_value-min_value>1):
        bakilan=int((max_value+min_value)/2)
        if int(barkod_listesi_dizi[bakilan])==aranan:
            kontrol=1
            if "DÜŞÜLDÜ" in str(liste[bakilan]):
                print("\a")
                print(Fore.RED, "Düşülmüş Kitap")
                print(Fore.CYAN, "  *--------------")
                print(Fore.RED, liste[bakilan], Style.RESET_ALL, Fore.CYAN, "*--------------")
            else:
                print(Fore.YELLOW, "  *--------------")
                print(Fore.CYAN, liste[bakilan], Style.RESET_ALL, Fore.YELLOW, "*--------------")

            print(Fore.MAGENTA)
            ekle=input("Eklemek istiyor musunuz? (Ekle: Enter)(Ekleme: e): ")
            print(Style.RESET_ALL)
            if (ekle) == "e":
                print(Fore.RED," ×  Eklenmedi ×  ",Style.RESET_ALL)
            elif str(ekle)==str(eklememe_barkodu):
                print(Fore.RED, " ×  Eklenmedi ×  ", Style.RESET_ALL)
            else:
                kayıtMetinBelgesi.write(liste[bakilan])
                print(Fore.GREEN," * Ekleme başarılı * ",Style.RESET_ALL)
                kayıtMetinBelgesi.close()

                kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')
                devam = devam + 1
                if (devam % 100 == 0):
                    an = datetime.now()
                    yil = an.year
                    ay = an.month
                    gün = an.day
                    saat = an.hour
                    dakika = an.minute
                    tarih = str(gün) + "." + str(ay) + "." + str(yil) + "_" + str(saat) + ";" + str(dakika)
                    shutil.copy("kayıt.txt", "Yedek/" + "kayıt " + tarih + ".txt")
                    kayıtMetinBelgesi.close()

            break
        elif int(barkod_listesi_dizi[bakilan])<aranan:
            min_value=bakilan
        elif int(barkod_listesi_dizi[bakilan])>aranan:
            max_value=bakilan

    if kontrol==0:
        print("\a")
        print(Fore.RED,"Barkod bulunamadı: ", aranan,Style.RESET_ALL)



   # i=0
   # while(i!=uzunluk):
   #     kayıtMetinBelgesi = open("kayıt.txt", mode='a', encoding='utf-8')
   #     if str(int(aranan)) in liste[i]:
   #         print(Fore.CYAN,liste[i],Style.RESET_ALL)
   #         print(Fore.MAGENTA)
   #         ekle=input("Eklemek istiyor musunuz? (Ekle: Enter)(Ekleme: e): ")
   #         print(Style.RESET_ALL)
   #         if(ekle=="e"):
   #             print(Fore.RED," ×  Eklenmedi ×  ",Style.RESET_ALL)
   #         else:
   #             kayıtMetinBelgesi.write(liste[i])
   #             print(Fore.GREEN," * Ekleme başarılı * ",Style.RESET_ALL)
   #             devam = devam + 1
   #             kayıtMetinBelgesi.close()
   #             if (devam % 100 == 0):
   #                 an = datetime.now()
   #                 gün = an.day
   #                 saat = an.hour
   #                 dakika = an.minute
   #                 tarih = str(gün) + "_" + str(saat) + ";" + str(dakika)
   #                 shutil.copy("kayıt.txt", "Yedek/" + "kayıt" + tarih + ".txt")
   #         break
   #     if(i==uzunluk-1):
   #         print(Fore.RED,"Aranan barkod bulunamadı !!!",Style.RESET_ALL)
   #     i = i + 1
   #
