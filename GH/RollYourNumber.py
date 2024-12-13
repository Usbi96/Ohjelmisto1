import random

Pelaaja = int(input("Valitse numero:"))

heitto1 = input("Heitä noppaa 1.kerran ENTER")
if heitto1 == "":
    heitto1 = random.randint(1, 6)
    print("Heitit",heitto1)
    if Pelaaja == heitto1:
        print("Voitit")
        exit(0)

heitto2 = input("Heitä noppaa 2.kerran ENTER")
if heitto2 == "":
    heitto2 = random.randint(1, 6)
    print("Heitit",heitto2)
    if Pelaaja == heitto2:
        print("Voitit")
        exit(0)

heitto3 = input("Heitä noppaa 3.kerran ENTER")
if heitto3 == "":
    heitto3 = random.randint(1, 6)
    print("Heitit",heitto3)
    if Pelaaja == heitto3:
        print("Voitit")
        exit(0)


print("Hävisit")