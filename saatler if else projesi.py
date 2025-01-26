saat=int(input("lütfen saat dilimini girin"))

if (saat<0 or saat>24):
    print("hatalı saat dilimi")

else:

    if (saat>6 and saat<=10):
        print("günaydın")
    elif (saat>10 and saat<=17):
         print("iyi günler")
    elif (saat>17 and saat<=21):
        prin ("iyi akşamlar")
    else:
        print("iyi geceler")
