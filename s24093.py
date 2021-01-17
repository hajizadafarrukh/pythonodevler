def rank(test):

    dizi = test
    dizi2=[]

    for i in range(0,len(dizi)):
        for j in range(0,len(dizi)):
            if(dizi[i]+1==dizi[j]): 
                print("* ",dizi[i], " sayısı ",dizi.index(dizi[i]),". indiste ve kendisinden büyük ardışığı olan ", dizi[j]," sayısı ise ",dizi.index(dizi[j]),". indistedir. Dolayısıyla aralarındaki mesafe:", "|",dizi.index(dizi[i])," - ",dizi.index(dizi[j]),"|"," = ",abs(dizi.index(dizi[i])-dizi.index(dizi[j])),".")
                dizi2.append(abs(dizi.index(dizi[i])-dizi.index(dizi[j])))
    toplam=0
    for i in range(0, len(dizi2)):
        toplam = toplam + dizi2[i]
    print("")
    print("")
    print("Fonksiyonun dönmesi gereken toplam skor değeri ", toplam ," olmalıdır.")            
            

test=[]        
rank(test)