# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta
import math

kanta = float(input("Mikä om kanta?:"))
korkeus = float(input("Mikä on korkeus?:"))
piiri = kanta*2 + korkeus*2
area = kanta*korkeus
print("Piiri on: " + str(piiri))
print("Ala on: " + str(area))