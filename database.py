import MySQLdb as mdb
import sys

class BazaMySQL(object):
    def __init__(self, adres, nazwa_uzytkownika, haslo, nazwa_bazy, plik_init, plik_procedury):
        self.adres = adres
        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.haslo = haslo
        self.nazwa_bazy = nazwa_bazy
        self.plik_init = plik_init
        self.plik_procedury = plik_procedury

    def connect(self):
        self.con = mdb.connect(self.adres, self.nazwa_uzytkownika, self.haslo, self.nazwa_bazy)
        self.c = self.con.cursor()
        self.executeScriptsFromFile(self.plik_init, self.plik_procedury)

    def disconnect(self):
        self.con.close()

    def wykonaj_rozkaz(self, rozkaz):
        try:
            self.c.execute(rozkaz)
            self.con.commit()
        except:
            #print rozkaz
            self.con.rollback()
    
    def executeScriptsFromFile(self, filename, plik_procedury):
        
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                self.c.execute(command)
            except:
                pass

        fd = open(plik_procedury, 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split('#')

        for command in sqlCommands:
            try:
                self.c.execute(command)  
            except:
                pass
    
    def dodaj_turniej(self, id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia):
        rozkaz = "INSERT INTO `turniej` VALUES (%s, %s, %s, '%s');"  % (id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia)
        self.wykonaj_rozkaz(rozkaz)

    def usun_turniej(self, id_turnieju):
        rozkaz = "DELETE FROM `turniej` WHERE `turniej`.`Id_turnieju` = %s;" % (id_turnieju)
        self.wykonaj_rozkaz(rozkaz)

    def dodaj_konto(self, rodzaj, uprawnienia):
        rozkaz = "INSERT INTO `konto` (`Rodzaj_konta`, `Uprawnienia_organizatora`) VALUES ('%s', b'%s');" % (rodzaj, uprawnienia)
        self.wykonaj_rozkaz(rozkaz)

    def usun_konto(self, rodzaj):
        rozkaz = "DELETE FROM `konto` WHERE `konto`.`Rodzaj_konta` = '%s';" % (rodzaj)
        self.wykonaj_rozkaz(rozkaz)

    def dodaj_uzytkownik(self, id, nick, haslo, rodzaj):
        rozkaz = "INSERT INTO `uzytkownik` (`Id_uzytkownika`, `Nick`, `Haslo`, `Rodzaj_konta`) VALUES ('%s', '%s', '%s', '%s');" % (id, nick, haslo, rodzaj)
        self.wykonaj_rozkaz(rozkaz)

    def usun_uzytkownik(self, id):
        rozkaz = "DELETE FROM `uzytkownik` WHERE `uzytkownik`.`Id_uzytkownika` = %s;" % (id)
        self.wykonaj_rozkaz(rozkaz)

    def dodaj_uzytkownik_turniej(self, id_turnieju, id_uzytkownika):
        rozkaz = "INSERT INTO `uzytkownik-turniej` (`Id_turnieju`, `Id_uzytkownika`) VALUES ('%s', '%s');" % (id_turnieju, id_uzytkownika)
        self.wykonaj_rozkaz(rozkaz)

    def dodaj_druzyna(self, id_druzyny, nazwa, ilosc_zawodnikow, id_turnieju, logo = None):
        if logo == None:
            rozkaz = "INSERT INTO `druzyna` (`Id_druzyny`, `Nazwa`, `Ilosc_zawodnikow`, `Id_turnieju`, `Logo`) VALUES ('%s', '%s', '%s', '%s', '');" % (id_druzyny, nazwa, ilosc_zawodnikow, id_turnieju) 
        else:
            rozkaz = "INSERT INTO `druzyna` (`Id_druzyny`, `Nazwa`, `Ilosc_zawodnikow`, `Id_turnieju`, `Logo`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (id_druzyny, nazwa, ilosc_zawodnikow, id_turnieju, logo)
        self.wykonaj_rozkaz(rozkaz)

    def usun_druzyna(self, id):
        rozkaz = "DELETE FROM `druzyna` WHERE `druzyna`.`Id_druzyny` = %s;" % (id)
        self.wykonaj_rozkaz(rozkaz)

    def dodaj_zawodnik(self, id_zawodnika, imie, nazwisko, pozycja, id_druzyny, zdjecie = None):
        if zdjecie == None:
            rozkaz = "INSERT INTO `zawodnik` (`Id_zawodnika`, `Imie`, `Nazwisko`, `Pozycja`, `Id_druzyny`, `Zdjecie`) VALUES ('%s', '%s', '%s', '%s', '%s', '');" % (id_zawodnika, imie, nazwisko, pozycja, id_druzyny)
        else:
            rozkaz = "INSERT INTO `zawodnik` (`Id_zawodnika`, `Imie`, `Nazwisko`, `Pozycja`, `Id_druzyny`, `Zdjecie`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (id_zawodnika, imie, nazwisko, pozycja, id_druzyny, zdjecie)
        self.wykonaj_rozkaz(rozkaz)

    def usun_zawodnik(self, id):
        rozkaz = "DELETE FROM `zawodnik` WHERE `zawodnik`.`Id_zawodnika` = %s;" % (id)
        self.wykonaj_rozkaz(rozkaz)