#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
import math
AA= input("Anna kokonaisluku:")
A = float(AA)
BB= input("Anna kokonaisluku:")
B = float(BB)
CC= input("Anna kokonaisluku:")
C = float(CC)

print("Summa on: " + str(A+B+C))
print("Tulo on: " + str(A*B*C))
print("Keskiarvo on: " + str((A+B+C)/3))