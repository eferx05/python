while (True):
    print("-"*30)

    print("(1) Topla \n(2) Çıkar \n(3) Çarp \n(4) Böl \n(5) üstel işlem \n(6) alt küme sayısı \n(7) e sayısının kuvvetlerini bulma \n(8) asal sayı bulan formül \n(9) pisagor teoremi ile dik olan üçgenin hipatenüsünü bulma \n(0) Çık")

    print("-"*30)

    işlem=int(input("lütfen bir işlem seçiniz."))

    if işlem==0:
        break
    elif işlem==1:
        sayi1=int(input("ilk sayıyı yazın..."))
        sayi2=int(input("ikinci sayıyı yazın..."))
        print(sayi1, "+" ,sayi2, "=" ,sayi1+sayi2)

    elif işlem==2:
        sayi1=int(input("ilk sayıyı yazın..."))
        sayi2=int(input("ikinci sayıyı yazın..."))
        print(sayi1, "-" ,sayi2, "=" ,sayi1-sayi2)

    elif işlem==3:
        sayi1=int(input("ilk sayıyı yazın..."))
        sayi2=int(input("ikinci sayıyı yazın..."))
        print(sayi1, "." ,sayi2, "=" ,sayi1*sayi2)

    elif işlem==4:
        sayi1=int(input("ilk sayıyı yazın..."))
        sayi2=int(input("ikinci sayıyı yazın..."))
        print(sayi1, ".\." ,sayi2, "=" ,sayi1/sayi2)
    elif işlem==5:
        sayi1=int(input("Taban sayısını yazın..."))
        sayi2=int(input("Kuvvet sayısını yazın..."))
        print(sayi1, "^" ,sayi2, "=" ,sayi1**sayi2)

    elif işlem==6:
        sayi1=int(input("küme kaç elemanlı?"))
        print(sayi1,"elemanlı kümenin alt küme sayısı=",2*sayi1)

    elif işlem==7:
        sayi1=int(input("e sayısının kaçıncı kuvvetini almak istersiniz?"))
        print("e sayısının",sayi1,"kuvveti=",2.7182818**sayi1)
    elif işlem==8:
        sayi1=int(input("lütfen herahangi bir asal sayı yazın..."))
        print(sayi1,"sayısına göre üretilmiş yeni asal sayı=",2**sayi1-1)
    elif işlem==9:
        sayi1=int(input("Dik üçgenin 1. kenar uzunluğunu yazın..."))
        sayi2=int(input("Dik üçgenin 2. kenar uzunluğunu yazın..."))
        import math
        print("Hipatenüs=",math.sqrt(sayi1**2+sayi2**2)) 


print("programdan çıkıldı...")

  

