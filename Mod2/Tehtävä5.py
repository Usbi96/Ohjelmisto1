#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
#ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
import math
luot = (13.2)
naul = (luot * 32)
leivis = (naul * 20)

print(leivis, naul, luot)

leiviskastr = input("Anna leiviskät")
naulstr = input("Anna naulat")
luotstr = input("Anna luodit")

leiviskä = float(leiviskastr)
lp = float(leivis)
naula = float(naulstr)
np = float(naul)
luoti = float(luotstr)

Vastaus = ((leiviskä*lp)+(naula*np)+(luoti*luot))
print(Vastaus)
