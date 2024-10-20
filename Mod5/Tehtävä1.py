### Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
from sys import excepthook

# Kysy käyttäjältä arpakuutioiden lukumäärä
lkm = int(input("Kuinka monta arpakuutiota heitetään? "))

if lkm <= 0:
    print("Arpakuutioiden lukumäärän täytyy olla positiivinen kokonaisluku.")
else:
    summa = 0

        # Heitä arpakuutioita ja laske silmälukujen summa
    for _ in range(lkm):
        silmaluku = random.randint(1, 6)
        summa += silmaluku

        # Tulosta silmälukujen summa
        print(f"Arpakuutioiden silmälukujen summa on: {summa}")


    (print("Virheellinen syöte. Syötä positiivinen kokonaisluku."))