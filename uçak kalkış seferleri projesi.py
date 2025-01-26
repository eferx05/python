while (True):
    seferno=input("sefer no. girin...")

    sirket=seferno[:2]
    sefersayısı=seferno[3:]
    uzunluk=len(seferno)

    if(sirket.isalpha() and sefersayısı.isnumeric and uzunluk==6):
        print("sefer numarası doğru...")
    else:
        print("hatalı sefer numarası girdiniz...")
