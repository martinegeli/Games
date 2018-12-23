#Lager først terninger

import random

def kasteTerning(n):
    liste=[]
    for i in range(n):
        liste.append(random.randint(1,6))
    return liste

#gir poeng til angriper og forsvarer etter terningenes verdi
def vunnetBrikker(liste1, liste2):
    liste1.sort(reverse = True)
    liste2.sort(reverse = True)
    angriper, forsvarer = 0, 0

    if liste1[0] > liste2[0]:
        angriper += 1
    else:
        forsvarer += 1
    if len(liste2) > 1 and len(liste1) > 1:
        if liste1[1] > liste2[1]:
            angriper += 1
        else:
            forsvarer += 1
    return angriper, forsvarer

#finner antall terninger som kastes basert på lag og bataljoner igjen
def antallTerninger(bataljoner, lag):
    if lag == 'angriper':
        if bataljoner == 1:
            return 1
        elif bataljoner == 2:
            return 2
        else:
            return 3

    if lag=='forsvarer':
        if bataljoner > 2:
            return 2
        else:
            return 1

#main function for game
def main():
    b_ang = int(input('Hvor mange bataljoner har angriper? '))
    b_for = int(input('Hvor mange bataljoner har forsvarer? '))
    i = 1
    while b_ang > 0 and b_for > 0:
        terningerAngriper = antallTerninger(b_ang, 'angriper')
        terningerForsvarer = antallTerninger(b_for, 'forsvarer')
        kasteAngriper = kasteTerning(terningerAngriper)
        kasteForsvarer = kasteTerning(terningerForsvarer)

        angriper, forsvarer = vunnetBrikker(kasteAngriper,kasteForsvarer)

        b_ang -= forsvarer
        b_for -= angriper
        print('Slag {} ender med at angriper taper {} og forsvarer taper {} \nTropper igjen er da {} til angripende lag og {} til forsvarende lag'.format(i, forsvarer, angriper, b_ang, b_for))
        i+=1
    if b_ang>0:
        vinner = 'angriper'
        antall = b_ang
    else:
        vinner = 'forsvarer'
        antall = b_for
    print('Vinneren av slaget ble: {} med {} bataljoner igjen'.format(vinner, antall))


main()
