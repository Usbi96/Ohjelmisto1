#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

from os import remove


def erottelu(lista):
    for numero in lista:
        if numero % 2 != 0:
            lista.remove(numero)
    return lista


lista = []
numerot = int(input("Lisää listaan nro: "))
lista.append(numerot)
while numerot != 0:
    numerot = int(input("Lisää listaan nro: "))
    lista.append(numerot)


print(lista)
print(erottelu(lista))





