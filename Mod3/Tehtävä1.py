#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhanp = float(input("Kuhan pituus senttimetreinä? "))
if kuhanp < 37:
    print(f"Kuha on alamittainen", 37 - kuhanp,"senttimetrillä.")
    print("Laske se takaisin veteen!")