import random

Pelaaja = input("Valitse kivi sakset tai paperi: ")
while Pelaaja not in ["kivi","paperi","sakset"]:
    print("valitse uudestaan")
    Pelaaja = input("Valitse kivi sakset tai paperi: ")
else:
    print(Pelaaja)



Kone = random.choice (["kivi","paperi","sakset"])
print(Kone)

if Pelaaja == Kone:
    print("Tasuri")
elif (Pelaaja == "kivi" and Kone == "sakset") or (Pelaaja == "paperi" and Kone == "kivi") or (Pelaaja == "sakset" and Kone == "paperi"):
    print("Voitit")
else:
    print("Hävisit")