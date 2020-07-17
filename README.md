# Ins-Spamv2
Ins-Spam yazılımının 2. versiyonudur. Birinci versiyona ulaşmak için : https://github.com/Ustrif/Ins-Spam

**Neler Yeni**

+ Günlük tutma özelliği eklendi.
+ Hızlı başlayabilmesi için argparse yapısına geçildi.
+ Hatalı şikayet sebebi verilmesini önlemek için liste şeklinde şikayet numarası alım yapısına geçildi.
+ 2 Adımdan oluşan yazılım (Hedef verisi toplama + Hedef'e atak) artık sadece 1 adımdan oluşuyor. 
+ Bazı küçük hataların onarılması ve zaman tutabilme özelliği.

**Test**

Program, 2 hesapla Windows x64 Single Language sistemde Python 'ın 3.8 sürümüyle, Google Chrome 83.0.4103.116 (Resmi Derleme) sürümüyle ve chromedriver ChromeDriver 83.0.4103.39 denenmiş olup hata vermemiştir.

Program, hesapsız Kali Linux sistemde (Sanal Makine) Python'ın 3.8.3 sürümüyle Google Chrome'un 84.0.4147.89 (Resmi Derleme) sürümüyle ve ChromeDriver'ın 83.0.4103.116 sürümüyle denenmiş olup hata vermemiştir.

**Kullanım - Kali Linux (Sanal Makine)**

apt-get update

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

dpkg -i google-chrome-stable_current_amd64.deb

apt-get install chromium-driver

git clone https://github.com/Ustrif/Ins-Spamv2.git

Not: pip3 -V yazıp bekleyin hata dönerse pip -V yazıp bekleyin bu komutlar sürümünü döndürür 2 olmamasına ve çalışıp çalışmadığına dikkat edin. Bu da olmazsa apt-get install python3-pip yazın ve kurun.

pip3 install -r requirements.txt

Hesaplarınızı kullanicilar.txt ve şifreler.txt ye ekleyin.

Hedef hesabın User İd bilgisini edinin ;

Bu komutu Konsol kısmına yazıp verdiği 10 haneli numarayı kopyalayın.

window._sharedData.entry_data.ProfilePage[0].graphql.user.id

![Image description](https://i.hizliresim.com/UvigUw.png)

cd Ins-Spamv2

python insspamv2.py -n aldığınıznumara

En son log.txt deki günlüğü okuyabilirsiniz.

**Kullanım - Windows**

Yazılımı indirip klasörden çıkarın.

Google Chrome sisteminizde yüklü olsun ve chrome sürümünüzden bir sürü düşük chrome driver ı indirip sisteminizdeki C:/Windows/System32 ve klasörden çıkardığınız içeriğin konumuna kopyalayın.

Google Chrome 84.0.4147.89 (Resmi Derleme) (64 bit) Sürümü için ChromeDriver 83.0.4103.39 indirme bağlantısı:

https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip

kullanicilar.txt ve şifreler.txt yi düzenleyip hesaplarınızı ekleyin...

cd konum

pip install -r requirements.txt

Hedef hesabın User İd bilgisini edinin ;

Bu komutu Konsol kısmına yazıp verdiği 10 haneli numarayı kopyalayın.

window._sharedData.entry_data.ProfilePage[0].graphql.user.id

![Image description](https://i.hizliresim.com/UvigUw.png)

python insspamv2.py -n aldığınıznumara

En son log.txt deki günlüğü okuyabilirsiniz.

**Programdan Kareler**

![Image_description](https://i.hizliresim.com/WjwCeK.png)

![Image_description](https://i.hizliresim.com/mWOVVt.png)

![Image_description](https://i.hizliresim.com/Yi0N85.png)

**İletişim**

https://t.me/atmaca7887
https://turkhackteam.org/members/818472.html
https://twitter.com/Atmaca7887

**Not: Kötüye kullanımda sorumluluk kabul etmemekle beraber yaptığınız her şeyden siz sorumlusunuz.**
