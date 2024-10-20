#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def muuttaja(luku):
    ns = luku * 3.785
    return ns

l = float(input("Anna luku: "))

while l >= 0:
    tulos = muuttaja(l)
    print(tulos)
    l = float(input("Anna luku: "))
else:
    exit(0)