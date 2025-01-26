def asalsayi_bulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1 :
            for i in range(2,sayi):
                if (sayi%i==0):
                    print(f"{sayi} sayısı asal değil")
                else :
                    print(sayi)
        else:
            pass            

sayi1=int(input("1. sayıyı girin..."))
sayi2=int(input("2. sayıyı girin..."))
print(asalsayi_bulma(sayi1,sayi2))