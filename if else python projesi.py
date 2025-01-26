cinsiyet=input("lütfen cinsiyetinizi girin [K/E]")

yas=int(input("yasınızı girin"))

if (cinsiyet=="K"):
   print("kadınlar için askerlik zorunlu değildir")
elif (cinsiyet=="E" and yas>=20):
    print("askere gitmelisiniz")
elif (cinsiyet=="E" and yas<20):
    print("henüz askerlik yaşınız gelmemiş")
