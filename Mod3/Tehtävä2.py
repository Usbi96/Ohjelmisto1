#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

user_imput = input("Valitse hyttiluokka Lux, A, B tai C!: ")
if user_imput.lower() == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif user_imput.lower() == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_imput.lower() == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_imput.lower() == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")