#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

alkunro = 0
loppunro = 1000
while loppunro > alkunro:
    alkunro += 1
    if alkunro % 3 == 0:
        print(alkunro)