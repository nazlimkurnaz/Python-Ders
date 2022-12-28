while (True):
    sicaklikDegeri = int(input('Sicaklik Degerini Giriniz'))

    if sicaklikDegeri <0:
        print ('Ürün katidir')
    elif (sicaklikDegeri>0 and sicaklikDegeri<100):
        print ('ürün sividir')
    else:
        print ('ürün gazdir')
