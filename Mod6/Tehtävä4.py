#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.



def summalista(lista):
    total = 0
    for i in lista:
        total = total + i
    return total

lista = []
numerot = int(input("Lisää listaan nro: "))
lista.append(numerot)
while numerot != 0:
    numerot = int(input("Lisää listaan nro: "))
    lista.append(numerot)
else:
    print(summalista(lista))



