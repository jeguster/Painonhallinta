# Auto-luokkien määritykset

class Auto():
    # Olionmuodostin eli konstruktori yliluokalle Auto
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot):
        """Auto-luokka malline auto-olioille yliluokka eri autotyypeille

        Args:
            rek (string): Auton rekisterinumero esim. CPM-186
            merkki (string): Auton valmistaja
            malli (string): Tyyppimerkintä
            vm (integer): Vuosimalli
            km (integer): Ajetut kilometrit
            kvoima (string): Käyttövoima; diesel, bensiini, hybridi, sähkö, kaasu, vety
            vaihteisto (string): Vaihteiston tyyppi; manuaali, automaatti
            vari (string): Auton pääväri
            paastot (integer): Hiilidioksidipäästöt g/KM
        """        
        self.rek = rek
        self.merkki = merkki
        self.malli = malli
        self.vm = vm
        self.km = km
        self.kvoima = kvoima
        self.vaihteisto = vaihteisto
        self.vari = vari
        self.paastot = paastot

    # Henkilöauton aliluokka, yliluokkana Auto, perii kaikki Auto-luokan ominaisuudet
class Henkiloauto(Auto):
        # Henkiloauto-objektien konstruktori
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot, istuimet, ovet, korimalli, tavaratila, lisavarusteet):
        super().__init__(rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot)
        """Henkilöautoluokka, yliluokkana Auto-luokka
            
        Args:
            istuimet (integer): Penkkien lukumäärä
            ovet (integer): Ovien lukumäärä
            korimalli (string): Korimallit; porrasperä, viistoperä, farmari, tila-auto
            tavaratila (integer): Tavaratilan vetoisuus litroina
            lisavarusteet (list): Lista lisävarusteista
        """
        self.istuimet = istuimet
        self.ovet = ovet
        self.korimalli = korimalli
        self.tavaratila = tavaratila
        self.lisavarusteet = lisavarusteet


if __name__ == "__main__":
    henkiloauto1 = Henkiloauto('HNZ-343', 'Renault', 'Grand Scenic', 2010, 189000, 'diesel', 'manuaali', 'hopea', 149, 7, 5, 'tila-auto', 1300, ['vakionopeuden säädin', 'automaatti-ilmastointi'])
    print('Rekisterinumero:', henkiloauto1.rek, 'istumapaikkoja:', henkiloauto1.istuimet)

# TODO: Lasketaan jäljelläolevien kilometrien hinta