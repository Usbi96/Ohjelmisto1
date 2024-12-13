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
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<15}{'Nopeus':<10}{'Kuljettu matka':<15}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


def luo_autot():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))
    return autot


def main():
    autot = luo_autot()
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        tunti += 1
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()


if __name__ == "__main__":
    main()
