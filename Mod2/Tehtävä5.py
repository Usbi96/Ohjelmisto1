#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
#ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
import math
luot = (13.3)
naul = (luot * 32)
leivis = (naul * 20)

print(leivis, naul, luot)

leiviskastr = input("Anna leiviskät: ")
naulstr = input("Anna naulat: ")
luotstr = input("Anna luodit: ")

leiviskä = float(leiviskastr)
lp = float(leivis)
naula = float(naulstr)
np = float(naul)
luoti = float(luotstr)

Vastaus = ((leiviskä*lp)+(naula*np)+(luoti*luot))
print(Vastaus)

kg = int(Vastaus / 1000)
print("kokonais kg määrä: " + str(kg))
g = float( Vastaus % 1000 )
print(f"kokonais grammat {g:.2f}")