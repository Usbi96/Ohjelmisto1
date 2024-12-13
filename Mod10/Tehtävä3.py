class Hissi:
    def __init__(self, alimman_kerroksen_numero, ylimman_kerroksen_numero):
        self.alimman_kerroksen_numero = alimman_kerroksen_numero
        self.ylimman_kerroksen_numero = ylimman_kerroksen_numero
        self.kerros = alimman_kerroksen_numero

    def kerros_ylös(self):
        if self.kerros < self.ylimman_kerroksen_numero:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alimman_kerroksen_numero:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alimman_kerroksen_numero, ylimman_kerroksen_numero, hissien_lukumaara):
        self.hissit = [Hissi(alimman_kerroksen_numero, ylimman_kerroksen_numero) for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alimman_kerroksen_numero)


talo = Talo(1, 5, 3)
talo.aja_hissiä(0, 4)
talo.aja_hissiä(1, 2)
talo.aja_hissiä(2, 5)
talo.palohälytys()
