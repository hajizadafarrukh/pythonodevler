

def uygulama():
    print("")
    print("__________________________________________________________________ \n")
    print("Uygulamaya hoşgeldiniz Lütfen Giriş Yapmak İçin Bilgeleri Doldurun \n")
    print("__________________________________________________________________\n")   
    
def giris():    
    
    print ("Hoşgeldiniz," , "sisteme", username,"adiyla giriş yaptınız. Şifreniz: ",password)
    print("\n")
    print(" 1-Dersleri Gormek\n","2-Kendini Denemek\n","3-Cikis Yapmak\n")

uygulama()


username = input("Lütfen bir kullanıcı adı giriniz : ")
password = input("Lütfen şifrenizi giriniz : ")    



giris()  

  
command = input("Lutfen ne yapmak istediginizi secin :  \n")    
dersler=["Java","Python","C","C++","C#"]

if command == "3":
    print ("Hoşçakalın sayın ",username)

    

if command == "2":
    print("Aşağıdakilerden hangisi sayısal bir veri tipi değildir?")
    print(" A- int  \n","B- string  \n","C- float\n")
    cevap = input()
    if cevap =="B" or cevap=="b":
        print("Tebrikler !!! Dogru Cevabi buldunuz\n")
    else:
        print("Dogru Cevap B - string\n")
    
        
    print("Aşağıdakilerden hangisi ondalıklı sayı tutmamıza imkan sağlar?\n")
    print("A- int  ","B- string  ","C- float")
    cevap1 = input()
    if cevap1== "C" or cevap1== "c":
        print("Tebrikler !!! Dogru Cevabi buldunuz")
    else:
         print("Dogru Cevap C - float")
    

if command =="1":
    print(dersler)
   
   

    

    
