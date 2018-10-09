#Lager først terninger

import random

def kasteTerning(n):
    liste=[]
    for i in range(n):
        liste.append(random.randint(1,6))
    return liste

def vunnetBrikker(liste1, liste2):
    liste1.sort()
    liste2.sort()
    liste1=liste1[::-1]
    liste2=liste2[::-1]
    angriper=0
    forsvarer=0
    if liste1[0]>liste2[0]:
        angriper+=1
    else:
        forsvarer+=1
    if len(liste2)>1 and len(liste1)>1:
        if liste1[1]>liste2[1]:
            angriper+=1
        else:
            forsvarer+=1
    return angriper, forsvarer


def antallTerninger(bataljoner, lag):
    if lag=='angriper':
        if bataljoner==1:
            return 1
        if bataljoner==2:
            return 2
        if bataljoner>2:
            return 3
    if lag=='forsvarer':
        if bataljoner<=2:
            return 1
        if bataljoner>2:
            return 2

def main():
    bataljonerAngriper=int(input('Hvor mange bataljoner har angriper? '))
    bataljonerForsvarer=int(input('Hvor mange bataljoner har forsvarer? '))
    i=1
    while bataljonerAngriper > 0 and bataljonerForsvarer >0:
        terningerAngriper = antallTerninger(bataljonerAngriper, 'angriper')
        terningerForsvarer = antallTerninger(bataljonerForsvarer, 'forsvarer')
        kasteAngriper=kasteTerning(terningerAngriper)
        kasteForsvarer=kasteTerning(terningerForsvarer)
        print(kasteAngriper)
        print(kasteForsvarer)
        angriper, forsvarer=vunnetBrikker(kasteAngriper,kasteForsvarer)
        bataljonerAngriper-=forsvarer
        bataljonerForsvarer-=angriper
        print('Slag', i, 'ender med at angriper taper', forsvarer, 'og forsvarer taper', angriper,'\nTropper igjen er da', bataljonerAngriper, 'til angripende lag og', bataljonerForsvarer, 'til forsvarende lag')
        i+=1
    if bataljonerAngriper>0:
        vinner='angriper'
        antall=bataljonerAngriper
    else:
        vinner='forsvarer'
        antall=bataljonerForsvarer

    print('Vinneren av slaget ble:', vinner, 'med', antall, 'bataljoner igjen')
main()