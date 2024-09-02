#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.



min =
max =

luku = (input("Anna numero: "))
while luku != "":

    if luku < min:
        min = (luku)
    elif luku > max:
        max = (luku)

luku = (input("Anna numero: "))
if luku == "":
    print("Ohjelma loppuu!")

print(f"Isoin luku on {max} ja pienin luku on {min}")
