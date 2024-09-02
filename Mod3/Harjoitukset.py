# Alustus ehtolauseelle

'''rahat = float(input("Paljonko on rahaa?: "))
if rahat >= 5.0:
    print("Voit ostaa laten")
else: print("Rahat ei riitä!")

numero = float(input("Anna numero: "))
if numero == 0:
    print ("Nolla")
if numero < 0:
    print ("Negatiivinen numero")
if numero > 0:
    print("Positiivinen numero")
'''
from operator import truediv

# Monta vaihtoehtoa

'''user_imput = input("Valitse a, b tai c : ")
if user_imput == "a":
    print("Valitsit a")
elif user_imput == "b":
    print("Valitsit b")
elif user_imput == "c":
    print("Valitsit c")
    a = 4 + 4
    print(f'Saat bonuksena {a} euroa')
else:
    print("Et valinnut oikeaa vaihtoehtoa")


# Loogiset operaattorit
ika = 5
nimi = "Matti"
print(ika < 10 and nimi == "Matti")

ika = 5
nimi = "Matti"
print(ika < 10 or nimi == "ulla")

ika = 5
nimi = "Matti"
print(ika < 10 not nimi == "Matti")
'''
print(False or False)