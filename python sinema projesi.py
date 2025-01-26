gun=int(input("hafta içi için 1, hafta sonu için 2"))

servisbedeli=200
öğrencisayısı=30


if (gun==1):
    ucret=8
else :
    ucret=12.5

geneltoplam=öğrencisayısı*ucret+servisbedeli

print("toplam=", str(geneltoplam))
