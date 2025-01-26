import random
pcsayi=random.randint(1,10)
tahmin=0

while (tahmin!=pcsayi):
    tahmin=int(input("1 ile 10 arasında bir sayı yazın."))


    if (tahmin>pcsayi):
        print("tahmininiz çok büyük, aşağı")
    if (tahmin<pcsayi):
        print("tahmininiz çok küçük, yukarı")

print("Bravo, doğru :)")
