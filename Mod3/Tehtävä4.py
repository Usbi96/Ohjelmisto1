#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko
# annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos
# ne ovat jaollisia myös neljälläsadalla.

vuosiluku = int(input("Anna vuosiluku"))
if vuosiluku % 4 == 0 or vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
    print("Karkausvuosi")