#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


lista = []

while True:
    syöte = (input("Anna numero: "))
    lista.append(syöte)
    if syöte == "":
        lista.sort(reverse=True)
        for i in range(0,5):
            print(lista[i])
        break
