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


hissi = Hissi(1, 5)
hissi.siirry_kerrokseen(3)
hissi.siirry_kerrokseen(1)
