liste=""
toplam=0

for x in range(80,120):
    if (x%2==1):
        liste=liste+str(x)+"-"
        toplam=toplam+x

print("liste:" ,liste)
print("tek sayıların toplamı=",toplam)
