adres=input("Lütfen internet adresinizi girin...")

nokta=adres.count(".")
if (adres.startswith("www") and adres.endswith("edu.tr") and nokta>=3):
    print("adres doğrudur...")
else:
    print("adres yanlıştır...")
