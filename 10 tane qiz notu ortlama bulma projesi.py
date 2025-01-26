quiz=[]

sayac=1
toplam=0
ort=0

while (sayac<=10):
    notunuz=int(input("notunuzu giriniz..."))
    quiz.append(notunuz)
    toplam=toplam+notunuz
    sayac=sayac+1

quiz.sort()

print("en düşük notunuz=", quiz[0])
print("en yüksek notunuz=", quiz[-1])

ort=int(toplam/sayac)

print("quiz ortalamanız...", ort)
