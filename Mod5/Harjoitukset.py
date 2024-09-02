"""name1 = "Ville"
name2 = "Liisa"
name3 = "Ulla"
age1 = 3
age2 = 5
age3 = 22

print(f"Hei, {name1} ikäsi on {age1}")
print(f"Hei, {name2} ikäsi on {age2}")
print(f"Hei, {name3} ikäsi on {age3}")


names = ["Ville", "Liisa", "Ulla", "Anna", "Matti"]
ages = [age1, age2, age3, 35, 50]
print(names)
print(ages)

#Listan pituus voidaan tarkistaa len() funktiolla!
length = len(names)
print(f"Listan pituus on: {length}")

#Alkioon viitataan indeksinumerolla
print(names[3])

print(f"Hei, {names[2]} ikäsi on {ages[2]}")

# Viittaus listan ulkopuolelle tuottaa virheen
#print(names[8]) tuottaa virheen

#Listan läpikäynti while silmukan avulla
iterator = 0
while iterator < len(names):
    print(f"Hei {names[iterator]} ikäsi on {ages[iterator]}")
    iterator = iterator + 1
"""

# Tapoja viitata listaan
"""lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti","Ahmed", "Neo", "Viivi"]
print(lista[2:5])
print(lista[2:])
print(lista[-1])
print(lista[2:6:2]) # indeksistä 2 indeksiin 6 joka toinen.
"""
"""
# Listaan voi yhdistää ja siellä voi olla erilaisia tietorakenteita
lista1 = ("Ulla", "Matti", "Ikka")
yhdistetty_lista = (23,45,66,67, lista1)
print(yhdistetty_lista[4][0]) #5.listasta ensimmäinen indeksi
"""

#lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti","Ahmed", "Neo", "Viivi"]
lista = ["Ville", "Liisa", "Ulla", "Anna", "Matti","Ahmed", "Neo", "Viivi"]

lista.append("Uusi nimi") #Uusi alkio listan loppuun
print(lista)
if "Ulla" in lista:
    print("Ulla löytyi")
lista.remove("Ulla") #Poistetaan alkio mikäli se löytyy
print(lista)
lista.insert(0, "Ulla") #Pistetään ULLA takaisin listan ekaksi
print(lista)
monesko = lista.index("Anna") #Monesko alkio listalla
print(monesko)

#Listojen yhdistäminen
lisää_nimiä = ["Ines", "Aku", "Tupu", "Hupu"]
lista.extend(lisää_nimiä)
print(lista)
#TAI
uusi_lista = lista + lisää_nimiä
print(uusi_lista)

lista[2]= "Lisa" #Muokataan olemassa olevaa alkiota
print(lista)

numerot = [1,4,7,0,6]
numerot.sort()
print(numerot)