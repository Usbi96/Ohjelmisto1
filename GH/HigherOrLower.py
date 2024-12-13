import random

Pelaaja = random.randint (1,6)
Kone = random.randint (1,6)

print("Pelaaja:",Pelaaja)
print("Kone:",Kone)

if Pelaaja == Kone:
    print("Tasuri")
elif Pelaaja > Kone:
    print("Voitit")
else:
    print("Hävisit")