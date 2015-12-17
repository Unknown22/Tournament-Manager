class Zawodnik(object):

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko