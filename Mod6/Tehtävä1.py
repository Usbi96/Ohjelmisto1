#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
lista = []
def noppapeli():
    noppa1 = random.randint(1,6)
    print(noppa1)
    return noppa1

while  noppapeli() != 6:
    print ("Nopan silmäluku:")

else:
    print("Stopattu")

