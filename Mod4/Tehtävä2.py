#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input("Anna tuumat: "))
while tuumat > 0:
    print(tuumat * 2.54 )
    tuumat = float(input("Anna tuumat: "))
if tuumat < 0:
    print("Ohjelma lopetettu!")



