import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä


auto_lista = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto_lista.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_ohi = False
while not kilpailu_ohi:
    for auto in auto_lista:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_ohi = True
            break

for auto in auto_lista:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus} km/h, "
          f"Nopeus: {auto.nopeus} km/h, Kuljettu matka: {auto.kuljettu_matka} km")
