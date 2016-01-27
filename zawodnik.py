class Zawodnik(object):

    def __init__(self, imie, nazwisko, pozycja, druzyna, id_zawodnika):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pozycja = pozycja
        self.druzyna = druzyna
        self.id_zawodnika = id_zawodnika

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko

    def getPozycja(self):
        return self.pozycja

    def getDruzyna(self):
        return self.druzyna

    def getId_zawodnika(self):
        return self.id_zawodnika