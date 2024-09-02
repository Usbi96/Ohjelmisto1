#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

user_sx = input("Mikä on sukupuolesi? Mies vai Nainen: ")
user_hg = int(input("Hemoglobiini arvosi?:"))
if user_sx.lower() == "mies" and user_hg > 195:
    print("Hemoglobiiniarvosi ovat korkealla!")
if user_sx.lower() == "mies" and user_hg < 134:
    print("Hemoglobiiniarvosi ovat alhaalla!")
if user_sx.lower() == "mies" and 134 < user_hg < 195:
    print("Hemoglobiiniarvosi ovat normaalit!")

if user_sx.lower() == "nainen" and user_hg > 175:
    print("Hemoglobiiniarvosi ovat korkealla!")
if user_sx.lower() == "nainen" and user_hg < 117:
    print("Hemoglobiiniarvosi ovat alhaalla!")
if user_sx.lower() == "nainen" and 117 < user_hg < 175:
    print("Hemoglobiiniarvosi ovat normaalit!")
else:
    print("Olet syöttänyt virheellistä tietoa!")