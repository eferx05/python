buyukharf="QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
kucukharf="qwertyuıopğüasdfghjklşizxcvbnmöç"
rakam="1234567890"
özelkarakter="!^+&*~<>-"

bhsayı=0
khsayı=0
rakamsayı=0
özelkarektersayı=0

sifre=input("Lütfen güçlü bir şifre giriniz...")

for harf in sifre:
    if harf in buyukharf:
        bhsayı+=1
    if harf in kucukharf:
        khsayı+=1
    if harf in rakam:
        rakamsayı+=1
    if harf in özelkarakter:
        özelkarektersayı+=1

if (bhsayı==0 and khsayı==0 and rakamsayı==0 and özelkarektersayı==0):
    print("bu şifre yerine , hiç şifre yazma daha güvenli olur...")
else:
    print("şifre güvenli dostum :)")
