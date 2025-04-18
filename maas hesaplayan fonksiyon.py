maas=[20000, 58000, 68000, 55000,10000]

for x in range(5):
    i=0

    def zam_hesaplayıcı(i):
       
       a= ((int(maas[i])*35)/100)+int(maas[i])
       print(a)
    i=i+1
    print(zam_hesaplayıcı(x))


#ikinci fonksiyon:

def yeni_hesap(x):
    return((x*35/100)+x)
maas=[20000, 58000, 68000, 55000,10000]
for i in range(5):
    print(yeni_hesap(maas[i]))


