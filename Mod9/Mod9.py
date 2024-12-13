class LuokanNimi:

# __init__ on funktio, erityinen sellainen, kutsutaan konstruktioksi.
# tätä funktiota kutsutaan aina automaattisesti kun luodaan luokasta olio / instanssi
# alustajan loppuun EI kirjoiteta return-lausetta

    def __init__(self, parametri1, parametri2):
        self.attribuutti1 = parametri1
        self.attribuutti2 = parametri2

# Metodi
    def metodi (self):
        return

    def metodi2 (self):
        return

'''Laajennetaan yllä olevaa koira esimerkkiä niin että se alustaa koirien ominaisuudet
'''

class Koira:

    def __init__(self, nimi, syntymävuosi, väri, koko):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.koko = koko
        self.väri = väri

    def printtaa_tiedot(self):
        print(f'Koiran nimi on {self.nimi} ja syntymävuosi {self.syntymävuosi}')

k1 = Koira('Lissu',2015, 'ruskea', 'iso')
k2 = Koira('Reko',2016, 'musta', 'keskikokoinen')
k3 = Koira('Rufus',2017, 'sininen', 'pieni')

print(k2.väri)

'''Laajennetaan yllä olevaa ohjelmaa niin että printataan koirien tiedot
'''
k2.printtaa_tiedot()