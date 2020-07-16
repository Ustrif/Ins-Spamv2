#/usr/bin/env python3
#coding = "utf-8"

"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
"""

try:
    from selenium import webdriver
    import re
    import argparse
    import os
    import colorama
    from selenium.webdriver.chrome.options import Options
    open("kullanicilar.txt","r", encoding= "utf-8")
    open("şifreler.txt","r", encoding= "utf-8")
except ModuleNotFoundError:
    print("* Modüllerden biri sisteminizde bulunmamaktadır. Yüklemek için : pip install -r requirements.txt")
    input("* Bir tuşa basın ve modülleri yükleyin.")
    exit()
except FileNotFoundError:
    print("* kullanicilar.txt veya şifreler.txt programın bulunduğu dizinde yoktur.")
    input("* Bir tuşa basın ve yazılımı sonlandırın.")
    exit()

from datetime import datetime
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
from datetime import datetime
import time
import re
from PyInquirer import prompt, Separator
init(autoreset=True)
başarılıatak = []
başarısızatak = []

def uyar(metin1):
    print(Fore.RED + "* " + metin1)

def bildirim(metin2):
    print(Fore.GREEN + "* " + metin2)
    
def log(yazı):
    filesss = open("log.txt","a", encoding= "utf-8")
    a = str(datetime.now())
    filesss.write(a)
    filesss.write(" ")
    filesss.write(yazı + "\n")
    filesss.close()

def giris():
    print(Fore.BLUE + """

     ______                             ______                                    
    /      |                           /      \                                   
    $$$$$$/  _______    _______       /$$$$$$  |  ______    ______   _____  ____  
      $$ |  /       \  /       |      $$ \__$$/  /      \  /      \ /     \/    \ 
      $$ |  $$$$$$$  |/$$$$$$$/       $$      \ /$$$$$$  | $$$$$$  |$$$$$$ $$$$  |
      $$ |  $$ |  $$ |$$      \        $$$$$$  |$$ |  $$ | /    $$ |$$ | $$ | $$ |
     _$$ |_ $$ |  $$ | $$$$$$  |      /  \__$$ |$$ |__$$ |/$$$$$$$ |$$ | $$ | $$ |
    / $$   |$$ |  $$ |/     $$/       $$    $$/ $$    $$/ $$    $$ |$$ | $$ | $$ |
    $$$$$$/ $$/   $$/ $$$$$$$/         $$$$$$/  $$$$$$$/   $$$$$$$/ $$/  $$/  $$/ 
                                                $$ |                              
                                                $$ |                              
                                                $$/                               
                                                                                    v2.py
        """)

    time.sleep(3)
 
class insspam():
    def __init__(self):
        super().__init__()
        self.ilksaniye = time.time()
        self.string = string
        self.insspambasla()
    def insspambasla(self):
        log("Browser harekete geçti.")
        self.options = Options()
        self.options.headless = True
        self.browser = webdriver.Chrome(options=self.options)
        self.url = "https://www.instagram.com/accounts/login/?next=/users/{}/report/".format(string)
        self.browser.get(self.url)
        time.sleep(3)
        sayı1 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main/article/div"))
        if sayı1 == 2 :
            self.browser.quit()
            self.insspambasla()
            log("Yanlış giriş ekranı, yeniden deneniyor.")
        else :
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(kkadı)
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(parola)
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
            time.sleep(3)
            sayı = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div"))
            log("Bilgiler ekrana başarıyla yazdırıldı.")
            if sayı == 7 : 
                uyar(f"{kkadı} hesabının şifresi veya parolası hatalı.")
                time.sleep(1)
                uyar("Bu hesabın atağı başarısız!")
                self.ikisaniye = time.time()
                bildirim(str(self.ikisaniye - self.ilksaniye) + " saniye sürmüştür.")
                self.browser.quit()
                log(f"{kkadı} hesabının şifresi veya parolası hatalı.")
                başarısızatak.append(1)
            else:
                sayı2 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div"))
                if sayı2 == 3 :
                    self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
                time.sleep(1)
                say3 = len(self.browser.find_elements_by_xpath("//*[@id='react-root']/section/div/div/div"))
                if say3 == 4:
                    uyar(f"{kkadı} Bu hesap doğrulamaya düşmüş.")
                    uyar("Bu hesabın atağı başarısız!")
                    self.ucsaniye = time.time()
                    bildirim(str(self.ucsaniye - self.ilksaniye) + " saniye sürmüştür.")
                    self.browser.quit()
                    log(f"{kkadı} Bu hesap doğrulamaya düşmüş.")
                    başarısızatak.append(1)
                else:
                    sayı4 = len(self.browser.find_elements_by_xpath("/html/body/div"))
                    if sayı4 == 3:
                        self.altisaniye = time.time()
                        bildirim(str(self.altisaniye - self.ilksaniye) + "saniye sürmüştür.")
                        self.sayi()
                        bildirim(f"Başarılı atak sayısı {sum(başarılıatak)} / Başarısız atak sayısı {sum(başarısızatak)}")
                        log(f"Başarılı atak sayısı {sum(başarılıatak)} / Başarısız atak sayısı {sum(başarısızatak)}")
                        kapan()
                    else:
                        if şikayetn == "1":
                            self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[2]").click()
                            
                        elif şikayetn == "2":
                            self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                            self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[1]").click()
                            
                        elif şikayetn == "3":
                            self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                            self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[4]").click()
                            
                        elif şikayetn == "4":
                            self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                            self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[5]").click()

                        elif şikayetn == "5":
                            self.browser.get(f"https://www.instagram.com/users/{string}/report/inappropriate")
                            self.browser.find_element_by_xpath("//*[@id='react-root']/div/ul/li[6]").click()

                        time.sleep(1.3)
                        bildirim("Atak başarılı!")
                        başarılıatak.append(1)
                        self.bessaniye = time.time()
                        bildirim(str(self.bessaniye - self.ilksaniye) + " saniye sürmüştür.")
                        log(f"{kkadı} Bu hesabın atağı başarılı.")
                        self.browser.quit()                   

def kapan():
        bildirim("Atak bitmiştir....")
        print(Fore.CYAN + """* Yapımcı : ZuL-RaA """)
        bildirim("Çıkmak için tuşa basınız...")
        input()
        log("Program kapatılıyor.")
        log("+++++ZuL-RaA+++++")
        exit()

def inpu():
    print(Fore.GREEN + """
    ****************************
    *1 = Spam                  *
    *--------------------------*
    *2 = Taciz veya Zorbalık   *
    *--------------------------*
    *3 = Çıplaklaklık          *
    *--------------------------*
    *4 = Nefret Söylemi        *
    *--------------------------*
    *5 = Kendine Zarar Verme   *
    ****************************
    """)
    questions = [
        {
            'type': 'list',
            'name': 'Seçilen',
            'message': 'Şikayet sebebi seçiniz?',
            'choices': [
            '1',
            '2',
            '3',
            '4',
            '5',
            ]
        },
    ]

    answers = prompt(questions)
    global şikayetn
    şikayetn = str(answers)[13]

if __name__ == "__main__":
    bassaniye = time.time()
    log("Modüller kontrol ediliyor.")
    veri = argparse.ArgumentParser(add_help=True, epilog="İşlem bittikten sonra log.txt dosyasından yaptıklarını okuyabilirsiniz.", usage="Bu şekilde kullanabilirsiniz: python insspamv2.py -n 10hanelinumara", description="""İnstagram da bir hesaba spam atmak için kullanabilirsiniz. ZuL-RaA tarafından kodlanmıştır. İletişim : https://t.me/atmaca7887""")
    veri.add_argument("-n", help="Kullanıcının İd Numarası")
    options = veri.parse_args()
    string = str(options.n)

    if 10 == len(string[::]):
        log("Yanlış değer verilmedi.")
        giris()
        log("Giriş ekranı bastırıldı.")
        ab = open("kullanicilar.txt","r", encoding= "utf-8").readlines()
        bildirim(f"{len(ab)} tane hesap tespit edildi.")
        log(f"{len(ab)} tane hesap tespit edildi.")
        inpu()
        log("Şikayet sebebi kullanıcıdan alındı.")
        a = open("kullanicilar.txt","r", encoding= "utf-8").read().strip()
        b = open("şifreler.txt","r",encoding= "utf-8").read().strip()
        s = re.compile(r'\s+')
        log("Atak başlıyor.")
        log(f"{string} nin hesabı {şikayetn} bu sebeple şikayet edilecek.")
        for i,j in zip(*map(s.split, [a,b])):
            kkadı = i
            parola = j
            insspam()
        sonsaniye = time.time()
        bildirim(str(sonsaniye - bassaniye) + "saniye sürmüştür.")
        bildirim(f"Başarılı atak sayısı {sum(başarılıatak)} / Başarısız atak sayısı {sum(başarısızatak)}")
        log(f"Başarılı atak sayısı {sum(başarılıatak)} / Başarısız atak sayısı {sum(başarısızatak)}")
        kapan()
           
    else:
        giris()
        uyar("Numara hanesi 10 değil veya numara verilmedi.")
        print(veri.print_help())
        log("Yanlış açıldı. \n")
        exit()  
