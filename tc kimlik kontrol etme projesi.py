tc=input("tc numaranız girin...")

uzunluk=len(tc)
ilkonrakam=tc[:10]
sonrakam=tc[10]
toplam=0

if (uzunluk!=11):
    print("hatalı tc kimlik numarası girdiniz...")
else:
    for rakam in ilkonrakam:
        toplam=toplam+int(rakam)
    toplam=str(toplam)

    if (toplam[-1]==sonrakam):
        print("geçerli tc kimlik no...")
    else:
       print("geçersiz tc kimlik no...") 
        
