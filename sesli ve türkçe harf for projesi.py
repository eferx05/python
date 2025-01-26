turkceharf="İĞÇÖŞişğçöı"
sesliharf="eiıoöaAEİIÖO"


ad=input("adınızı yazın...")

for harf in ad:

    if harf in turkceharf:
        print("türkçe harfleriniz=",harf)



for ikinciharf in ad:

    if ikinciharf in sesliharf:
        print("sesli harfleriniz=",ikinciharf)
