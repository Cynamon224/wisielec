import random

owoce={1:"apple",2:"banana"}
warzywa={1:"potato",2:"tomato"}
przedmioty={1:"ball",2:"poster"}
meble={1:"chair",2:"bed"}
kategoria=[owoce,warzywa,przedmioty,meble]

liczba=random.randint(1,2)
liczba2=random.randint(0,3)
slowo0=kategoria[liczba2]
slowo=slowo0[liczba]
slowoTab=[]
for i in slowo:
    slowoTab.append("_")

wisielec0=["|_______"]
wisielec1=["|","|","|","|","|_______"]
wisielec2=["______","|","|","|","|","|_______"]
wisielec3=["______","|  |","|","|","|","|_______"]
wisielec4=["______","|  |","|  O","|","|","|_______"]
wisielec5=["______","|  |","|  O","| /|\ ","|","|_______"]
wisielec6=["______","|  |","|  O","| /|\ ","| / \ ","|_______"]
wisielce=[wisielec0,wisielec1,wisielec2,wisielec3,wisielec4,wisielec5,wisielec6]

wynik=True
iloscProb=0
while wynik:
    litera=input("Podaj litere:")
    
    wystapienia=0
    for i in range (len(slowo)):
        
        if slowo[i]==litera:
            slowoTab[i]=litera
            wystapienia+=1
    print(slowoTab)
    print("ilosc wystapien litery:",wystapienia)
    
    if "_" not in slowoTab :
        print("Gratulacje!")
        wynik=False
    
    if wystapienia==0:
        for i in wisielce[iloscProb]:
            print(i)
        iloscProb+=1
        if iloscProb>6:
            print("Koniec gry :(")
            wynik=False
        
           

        


        

