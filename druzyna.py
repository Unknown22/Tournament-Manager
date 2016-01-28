class Druzyna(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.iloscZawodnikow = 0
        self.zawodnicy = []

    def getNazwa(self):
        return self.nazwa

    def dodajZawodnika(self, zawodnik):
        self.zawodnicy.append(zawodnik)

    def usunZawodnika(self, id_zawodnika):
        for x in self.zawodnicy:
            if x.getId_zawodnika() == id_zawodnika:
                self.zawodnicy.remove(x)