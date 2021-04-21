# Luokka ja olioharjoituksia

# Luokka Lintujen tietojen tallennukseen

class Lintu:
    def __init__(self, nimi, tieteellinen_nimi, ravinto):
        self.nimi = nimi
        self.tieteellinen_nimi = tieteellinen_nimi
        self.ravinto = ravinto

    def aani(self, aani):
        print('Sanoo', aani)

lintu = Lintu('korppi', 'corvus corax', 'raadot')

print(lintu.nimi, 'on tieteelliseltä nimeltään', lintu.tieteellinen_nimi)
lintu.aani('kraak, kraak')

class Kahlaaja(Lintu):
    def __init__(self, nimi, tieteellinen_nimi, ravinto):
        super().__init__(nimi, tieteellinen_nimi, ravinto)
        
        self.laji = 'kahlaaja'

kahlaaja = Kahlaaja('Kurki', 'grus grus', 'sammakot')

print(kahlaaja.nimi, 'on', kahlaaja.laji, 'ja se syö', kahlaaja.ravinto)