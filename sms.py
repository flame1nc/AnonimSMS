import requests
from os import system as s

import os

banner = """
         	             >Codeing By FLAME
                          
|> İstediginiz telefon numarasına her gün *1 defa* mesaj atma hakkınız vardır!

|> Mesajınızdaki karakter sayısı 70'i geçmemelidir.

|> Telefon numarasını doğru girmezseniz hata vericektir. (numara arasında bo)

|> Çalıştığını onaylamak için kendinizde deneyebilirsiniz.

|> Arkadaşlar doğru girdiğiniz halde hata veriyorsa 2. defa tekrar deneyin hata verse bile çalışacaktır.

|> Discord: flame.inc
"""

print(banner)

sor = input("Mesajı göndermek istediğiniz telefon numarası, *Örn: 5438385599* >>> ")

mesaj = input("Göndermek istediğiniz mesaj >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi? [e/h] >>> ")

if drlm == "e" or drlm == "H":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "h" or drlm == "H":
    quit()
else:
    print("\n|HATA, Düzgünce girip tekrar deneyiniz!")
