pcsayı=42
tahmin=0

while (tahmin!=pcsayı):
    tahmin=int(input("1-100 arasında bir sayı yazınız"))


    if (tahmin>pcsayı):
        print("tutulan sayı daha küçük; Aşağı")
    if (tahmin<pcsayı):
        print("tutulan sayı daha büyük; Yukarı")

print("tebrikler, bildiniz")
