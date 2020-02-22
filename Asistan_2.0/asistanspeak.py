# _*_ coding: UTF-8 _*_

from tkinter import *
from playsound import *
from gtts import gTTS
from selenium import webdriver
from email.mime.text \
    import MIMEText
import speech_recognition as sr
import os
import sqlite3
import random
import time
import feedparser
import smtplib
import pyqrcode
from getpass import getpass
import wikipedia
from variables import *
from extrafunct import *


def maindq():
    brand()
    while True:
        data = input("Söylemek İstediğiniz Şeyi Yazınız: ")

        # Selamlaşmak 20 GIFW
        if (data == "Merhaba" or data == "merhaba"):

            audiodata = gTTS(text=greetingsvare,lang="tr") # Merhaba, nasılsın?
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")
            print(greetingsvare)
            answergreetings = input("?: ")

            if(answergreetings == "iyiyim" or answergreetings == "İyiyim"):
                svdrandom = random.randint(1,4)

                if(svdrandom == 1):
                    print("Pekala.")
                    audiodata = gTTS(text="Pekala",lang="tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

                elif(svdrandom == 2):
                    print(greetingsvartwo)
                    audiodata = gTTS(text=greetingsvartwo,lang="tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

                elif(svdrandom == 3):
                    print(greetingsvarthree)
                    audiodata = gTTS(text=greetingsvarthree,lang="tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

                elif(svdrandom == 4):
                    print(greetingsvarfour)
                    audiodata = gTTS(text=greetingsvarfour,lang="tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

                    varfourd = input("?:")

                    if(varfourd == "evet" or varfourd == "Evet"):
                        print(greetingsvarfive)
                        audiodata =gTTS(text=greetingsvarfive,lang="tr")
                        audiodata.save("speakeraudio.mp3")
                        playsound("speakeraudio.mp3")

                    elif(varfourd == "hayır" or varfourd == "Hayır"):
                        print(greetingsvarsix)
                        audiodata = gTTS(text=greetingsvarsix,lang = "tr")
                        audiodata.save("speakeraudio.mp3")
                        playsound("speakeraudio.mp3")


            elif(answergreetings == "kötüyüm" or answergreetings == "Kötüyüm"):
                print(greetingsvarsix)
                audiodata = gTTS(text=greetingsvarsix,lang="tr")
                audiodata.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")

            elif(answergreetings == "hiç" or answergreetings == "Hiç"):
                hansrand = random.randint(1,2)

                if(hansrand == 1):
                    print(greetingsvareight)
                    audiodata = gTTS(text = greetingsvareight, lang="tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

                elif(hansrand == 2):
                    print(greetingsvarseven)
                    audiodata = gTTS(text = greetingsvarseven,lang = "tr")
                    audiodata.save("speakeraudio.mp3")
                    playsound("speakeraudio.mp3")

            elif(answergreetings == "seni ilgilendirmez" or answergreetings == "Seni ilgilendirmez"):
                print(":(")
                time.sleep(3)
                break


        elif(data == "naber" or data == "Naber" or data == "N'ber"):

            print(greetingsvarnine)
            audiodata = gTTS(text=greetingsvarnine,lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

            replynb = input("?:" )
            time.sleep(4)
            replyrandom = random.randint(1,2)

            if(replyrandom == 1):
                print(greetingsvarten)
                audiodata = gTTS(text=greetingsvarten,lang="tr")
                audiodata.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")

            elif(replyrandom == 2):
                print(greetingsvareleven)
                audiodata = gTTS(text=greetingsvareleven,lang="tr")
                audiodata.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")


        elif(data == "Nasılsın" or data == "nasılsın"):
            nasrandom = random.randint(1,2)

            if(nasrandom == 1):
                print(greetingsvartwelve)
                audiodata = gTTS(text=greetingsvartwelve,lang="tr")
                audiodata.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")

            elif(nasrandom == 2):
                print(greetingsvarthirtythree)
                audiodata = gTTS(text=greetingsvarthirtythree,lang="tr")
                audiodata.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")


# Saat bilgisi

        elif(data == "saat kaç" or data == "Saat kaç" or data == "saat kaç?" or data == "Saat kaç?"):
            zaman = time.localtime()
            saat = zaman.tm_hour
            dakika = zaman.tm_min
            saniye = zaman.tm_sec

            print(str(saat) + ":" + str(dakika) + ":" + str(saniye))

# Çıkış \ Quit

        elif(data == "kendini kapat" or data == "Kendini kapat"):
            print("Sonra Görüşürüz...")
            time.sleep(4)
            break

# Mail At | Send Mail
        elif(data == "mail at" or data == "Mail at"):

            imail = input("Mail Adresinizi Giriniz: ")
           # ipass = input("Şifrenizi Giriniz: ")
            ipass = getpass("Sifrenizi Giriniz: ")
            sendmail = input("Gönderilecek mail adresini giriniz: ")
            message = input("Gönderilecek Mesajınızı Giriniz: ")

            print(str(sendmail) + "Adresine gönderilecek onaylıyor musunuz Onay İçin E yazın: ")
            choices = input(":> ")

            if (choices == "E" or choices == "e"):
                mail = smtplib.SMTP("smtp.gmail.com",587)
                mail.ehlo()
                mail.starttls()
                mail.login(imail,ipass)
                mail.sendmail(imail,sendmail,message)
                print("Başarı İle Gönderildi.!")

            else:
                print("İşlem İptal Edildi!")

# Sözlük | Wikipedia

        elif(data == "wikipedia" or data == "Wikipedia" or data == "sözlük" or data == "wikipedide ara" or data == "Sözlük" or data == "wikipedia'da ara" or data == "Wikipedia'da ara" or data =="wikipedi" or data == "Wikipedi"):

            word = input("Aramak İstediğiniz Kelimeyi Yazınız: ")
            wikipedia.set_lang("tr")
            infodata = wikipedia.summary(word)
            print("\n")
            print(infodata)
            print("\n")


# Sahip bilgisi | Own info

        elif(data == "bilgilerimi kaydet" or data == "Bilgilerimi kaydet"):

            def owner():
                connect = sqlite3.connect("Bilgiler.db")
                cursor = connect.cursor()

                def createtable():
                    cursor.execute("CREATE TABLE IF NOT EXISTS Sahip_Bilgisi(İsim TEXT, Soyisim TEXT, Yaş INT, Şehir TEXT, Meslek TEXT)")
                def addvalue():
                    isim = input("İsminizi Yazınız: ")
                    soyisim = input("Soyisminizi Yazınız: ")
                    yas = int(input("Kaç Yaşındasın: "))
                    sehir = input("Hangi Şehirde Yaşıyorsun: ")
                    meslek = input("Hangi Meslek ile Uğraşıyorsun: ")
                    cursor.execute("INSERT INTO Sahip_Bilgisi(İsim,Soyisim,Yaş,Şehir,Meslek) VALUES(?,?,?,?,?)",(isim,soyisim,yas,sehir,meslek))
                    print("\nBaşarı ile Kaydedildi!")
                    connect.commit()
                    connect.close()
                
                createtable()
                addvalue()
            owner()
        
        elif(data == "asistan bilgilerini kaydet" or data == "Asistan bilgilerini kaydet"):

            def asistaninf():
                connect = sqlite3.connect("Bilgiler.db")
                cursor = connect.cursor()

                def createasistantable():
                    cursor.execute("CREATE TABLE IF NOT EXISTS Asistan_Bilgisi(İsim TEXT, Cinsiyet TEXT,Yaş INT)")
                def addasistanvalue():
                    isim = input("Asistan'a Vermek İstediğiniz İsim: ")
                    yas = int(input("Asistan'a Vermek İstediğiniz Yaş Değeri: "))
                    cinsiyet = input("Asistan'a Vermek İstediğiniz Cinsiyet: ")
                    cursor.execute("INSERT INTO Asistan_Bilgisi(İsim, Cinsiyet, Yaş) VALUES(?,?,?)",(isim,cinsiyet,yas))

                    print("\n Başarı ile Kaydedildi!")
                    connect.commit()
                    connect.close()

                createasistantable()
                addasistanvalue()

            asistaninf()

        elif(data == "adım ne" or data == "adım ne?" or data == "Adım ne" or data == "Adım ne?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT İsim FROM Sahip_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            tts = gTTS(text=datasq, lang="tr")
            tts.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

        elif(data == "soyadım ne" or data == "soyadım ne?" or data == "Soyadım ne" or data == "Soyadım ne?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT Soyisim FROM Sahip_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

        elif(data == "kaç yaşındayım" or data == "kaç yaşındayım?" or data == "Kaç yaşındayım" or data == "Kaç yaşındayım?" or data == "yaşımı biliyor musun?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT Yaş FROM Sahip_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

        elif(data == "Hangi şehirde yaşıyorum" or data == "Hangi şehirde yaşıyorum?" or data == "hangi şehirde yaşıyorum" or data == "hangi şehirde yaşıyorum?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT Şehir FROM Sahip_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")
        

# Asistan Bilgisi Öğrenmek
        elif(data == "adın ne" or data == "adın ne?" or data == "Adın ne" or data == "Adın ne?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT İsim FROM Asistan_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

        elif(data == "kaç yaşındasın" or data == "kaç yaşındasın?" or data == "Kaç yaşındasın" or data == "Kaç yaşındasın?" or data == "yaşımı biliyor musun?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT Yaş FROM Asistan_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audioddata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

        elif(data == "cinsiyetin ne" or data == "cinsiyetin ne?" or data == "Cinsiyetin ne" or data == "Cinsiyetin ne?"):
            connect = sqlite3.connect("Bilgiler.db")
            cursor = connect.cursor()

            cursor.execute("SELECT Cinsiyet FROM Asistan_Bilgisi")
            datasq = str(cursor.fetchall())
            print(datasq)
            audiodata = gTTS(text=datasq, lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

# Hava Durumu
        elif(data == "hava durumu" or data == "Hava durumu"):
            def weather():
                kita = input("Bulunduğunuz Kıtayı Yazınız: ")
                ulke = input("Yaşadığınız Ülkeyi Yazınız: ")
                postacode = input("Posta Kodunuzu Yazınız: ")
                sehir = input("Yaşadığınız Şehri Yazınız: ")
                print("\nNot: hava durumu için konum bilgilerinizi ingilizce yazmanız gerekmektedir.\n")

                parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode="+kita+"|"+ulke+"|"+postacode+"|"+sehir)
                parse = parse["entries"][0]["summary"]
                parse = parse.split()
                print(parse[2], parse[4], parse[5])
                return (weather)
                #http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=Asia|Turkey|16450|Bursa

            weather()
            audiodata = gTTS(text=weatherone,lang="tr")
            audiodata.save("speakeraudio.mp3")
            playsound("speakeraudio.mp3")

# QR Kod Oluştur
        elif(data == "qr kod oluştur" or data == "qr code oluştur" or data == "Qr kod oluştur" or data == "QR kod oluştur" or data == "QR code oluştur" or data == "QR Kod oluştur" or data == "QR Code oluştur" or data == "QR Kod Oluştur"):

            adres = input("Oluşturmak istediğiniz adresi giriniz: ")
            filename = input("Oluşturmak istediğiniz dosyanın adını giriniz: ")
            
            url = pyqrcode.create(adres)
            filenamedata = (filename+".svg")
            url.svg(filenamedata,scale=8)

            print("QR Kod dosyası başarı ile 'svg' formatında bulunduğunuz klasöre kaydedildi!")

# Dizi
        elif(data == "bana bir dizi öner" or data == "Bana bir dizi öner"):
            dizi()
# Author
        elif(data == "author" or data == "Author" or data == "seni kim yaptı" or data == "Seni kim yaptı"):
            authorinf()


# Tarayıcıda arama yapmak | Browser Search

        elif(data == "tarayıcıda ara" or data == "Tarayıcıda ara"):

            operatingsystem = input("İşletim Sisteminizi Giriniz: ")
            browserch = input("Kullandığınız Tarayıcıyı Giriniz (Chrome/Firefox): ")
            bit = int(input("İşletim Sistemi Mimarinizi Giriniz (32/64): "))


            if(operatingsystem == "Linux" or operatingsystem == "linux" and browserch == "Firefox" or browserch == "firefox" and bit == 32):
                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/linuxfirefox32/geckodriver")
                browser = webdriver.Firefox(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()

            elif(operatingsystem == "Linux" or operatingsystem == "linux" and browserch == "Firefox" or browserch == "firefox" and bit == 64):
                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/linuxfirefox64/geckodriver")
                browser = webdriver.Firefox(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()    
            
            elif(operatingsystem == "Linux" or operatingsystem == "linux" and browserch == "Chrome" or browserch=="chrome" and bit == 32):
                print("Üzgünüm, driver bulunamamaktadır, eğer elinde var ise bu kodu tekrar düzenleyebilirsin!")

            elif(operatingsystem == "Linux" or operatingsystem == "linux" and browserch == "Chrome" or browserch=="chrome" and bit == 32):

                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/linuxchrome64/chromedriver")
                browser = webdriver.Chrome(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()

            elif(operatingsystem == "windows" or operatingsystem == "Windows" and browserch == "firefox" or browserch == "Firefox" and bit == 32):
                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/windowsfirefox32/geckodriver.exe")
                browser = webdriver.Firefox(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()
            
            elif(operatingsystem == "windows" or operatingsystem == "Windows" and browserch == "firefox" or browserch == "Firefox" and bit == 64):
                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/windowsfirefox64/geckodriver.exe")
                browser = webdriver.Firefox(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()

            elif(operatingsystem == "windows" or operatingsystem == "Windows" and browserch == "chrome" or browserch == "Chrome" and bit == 32):
                print("")
                search_data = input("Aramak İstediğiniz Şeyi Yazınız: ")
                path = ("./Drivers/windowschrome32/chromedriver.exe")
                browser = webdriver.Firefox(executable_path=path)

                browser.get("https://www.google.com/")

                searchinput = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchinput.click()
                searchinput.send_keys(search_data)
                
                time.sleep(2)
                searchbutton = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
                searchbutton.click()

            elif(operatingsystem == "windows" or operatingsystem == "Windows" and browserch == "chrome" or browserch == "Chrome" and bit == 64):
                print("Üzgünüm, driver bulunamamaktadır, eğer elinde var ise bu kodu tekrar düzenleyebilirsin!")
                
# kitap önerisi

        elif(data == "bana bir kitap öner" or data == "Bana bir kitap öner"):
            kitap()

# not alma
        
        elif(data == "not al" or data == "Not al"):

            con = sqlite3.connect("Notlar.db")
            cursor = con.cursor()

            def creatememotable():
                cursor.execute("CREATE TABLE IF NOT EXISTS Notlar(Konu Text, İçerik TEXT)")
            def addmemovalue():
                tag = input("Notunuzun Konusunu Giriniz: ")
                icerik = input("Notunuzu Giriniz: ")
                cursor.execute("INSERT INTO Notlar(Konu,İçerik) VALUES(?,?)",(tag,icerik))

                print("\n Başarı ile Kaydedildi!")
                con.commit()
                con.close()

            creatememotable()
            addmemovalue()

# notları göstermek

        elif(data == "notları getir" or data == "Notları getir" or data == "notları göster" or data == "Notarı göster"):
            con = sqlite3.connect("Notlar.db")
            cursor = con.cursor()

            cursor.execute("SELECT * FROM Notlar")

            data = cursor.fetchall()
            print(data)

# notları silmek

        elif(data == "notları sil" or data == "Notları sil"):
            print(memodelete)

# Sürekli tekrarla
        elif(data == "sürekli tekrarla" or data == "Sürekli tekrarla"):
            spdata = input("Tekrarlamamı istediğiniz şeyi yazınız: ")
            vl = int(input("Kaç Kere Tekrarlamamı İstersiniz: "))
            for i in range(vl):
                #spdata = input("Tekrarlamamı istediğiniz şeyi yazınız: ")
                tts = gTTS(text =spdata, lang="tr")
                tts.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")

# Papağan | Dediğimi tekrarla
        elif(data == "papağan" or data == "Papağan" or data == "dediğimi tekrarla" or data == "Dediğimi tekrarla"):
            print("Sonlandırmak için Çıkış yazınız.")
            while True:
                spdata = input("Tekrarlamamı istediğiniz şeyi yazınız: ")
                tts = gTTS(text=spdata, lang="tr")
                tts.save("speakeraudio.mp3")
                playsound("speakeraudio.mp3")
                if(spdata == "çıkış"):
                    break

        elif(data == "nedir"):
            print(errorone)

os.system('cls' if os.name == 'nt' else 'clear')


#
