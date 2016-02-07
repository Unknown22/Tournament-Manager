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
        self.port = 3306

    def connect(self):
        self.con = mdb.connect(self.adres, self.nazwa_uzytkownika, self.haslo, self.nazwa_bazy, self.port)
        self.c = self.con.cursor()
        self.executeScriptsFromFile(self.plik_init, self.plik_procedury)
        self.dodaj_konto('administrator', '1')
        self.dodaj_konto('user', '0')

    def disconnect(self):
        self.con.close()

    def wykonaj_rozkaz(self, rozkaz):
        try:
            self.c.execute(rozkaz)
            self.con.commit()
        except:
            #print rozkaz
            self.con.rollback()

    def wykonaj_rozkaz_i_zwroc(self, rozkaz):
        try:
            self.c.execute(rozkaz)
            results = self.c.fetchall()
            return results
        except:
            return None
    
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
    
    def dodaj_mecz(self, id_meczu, wynik, data, id_turnieju, id_druzyny_1, id_druzyny_2):
        rozkaz = "INSERT INTO `mecz` VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (id_meczu, wynik, data, id_turnieju, id_druzyny_1, id_druzyny_2)
        self.wykonaj_rozkaz(rozkaz)

    def pokaz_mecz(self, id_meczu):
        rozkaz = "SELECT * FROM mecz WHERE Id_meczu='%s';" % (id_meczu)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def dodaj_turniej(self, id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia):
        rozkaz = "INSERT INTO `turniej` VALUES (%s, %s, %s, '%s');"  % (id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia)
        self.wykonaj_rozkaz(rozkaz)

    def usun_turniej(self, id_turnieju):
        rozkaz = "DELETE FROM `turniej` WHERE `turniej`.`Id_turnieju` = %s;" % (id_turnieju)
        self.wykonaj_rozkaz(rozkaz)

    def pokaz_turniej(self, id_turnieju):
        rozkaz = "SELECT * FROM turniej WHERE Id_turnieju = '%s'" % (id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        wynik = []
        for row in results:
            id = row[0]
            ilosc_druzyn = row[1]
            czy_posiada_faze_grupowa = str(row[2])
            data_rozpoczecia = row[3]
            if czy_posiada_faze_grupowa == '\x00':
                czy_posiada_faze_grupowa = False
            if czy_posiada_faze_grupowa == '\x01':
                czy_posiada_faze_grupowa = True
            do_dodania = [id, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia]
            wynik.append(do_dodania)
        return wynik

    def szukaj_nastepne_id_turnieju(self):
        rozkaz = "SELECT * FROM turniej"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results
    
    def szukaj_nastepne_id_meczu(self):
        rozkaz = "SELECT * FROM mecz"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def zwroc_druzyny_w_turnieju(self, id_turnieju):
        rozkaz = "SELECT * FROM druzyna WHERE Id_turnieju = '%s';" % (id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def zwroc_zawodnikow_w_turnieju(self, id_druzyny):
        rozkaz = "SELECT * FROM zawodnik WHERE Id_druzyny = '%s';" % (id_druzyny)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results
            
    def liczba_druzyn(self, id_turnieju):
        rozkaz = "SELECT Ilosc_druzyn FROM turniej WHERE Id_turnieju = '%s';" % (id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def pokaz_uzytkownik(self, id_turnieju):
        rozkaz = "SELECT uzytkownik.Id_uzytkownika, Nick, Haslo, uzytkownik.Rodzaj_konta, Uprawnienia_organizatora FROM uzytkownik JOIN konto ON uzytkownik.Rodzaj_konta = konto.Rodzaj_konta JOIN `uzytkownik-turniej` ON uzytkownik.Id_uzytkownika = `uzytkownik-turniej`.`Id_uzytkownika` WHERE `uzytkownik-turniej`.Id_turnieju = %s " % (id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        wynik = []
        for row in results:
            id = row[0]
            nick = row[1]
            haslo = row[2]
            rodzaj_konta = row[3]
            uprawnienia = row[4]
            if uprawnienia == '\x00':
                uprawnienia = False
            if uprawnienia == '\x01':
                uprawnienia = True
            do_dodania = [id, nick, haslo, rodzaj_konta, uprawnienia]
            wynik.append(do_dodania)
        return wynik

    def szukaj_nastepne_id_uzytkownika(self):
        rozkaz = "SELECT * FROM uzytkownik"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

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
            rozkaz = "INSERT INTO `druzyna` (`Id_druzyny`, `Nazwa`, `Ilosc_zawodnikow`, `Id_turnieju`, `Logo`) VALUES ('%s', '%s', '%s', '%s', '%s');" % (id_druzyny, nazwa, ilosc_zawodnikow, id_turnieju, mdb.escape_string(logo))
        self.wykonaj_rozkaz(rozkaz)

    def usun_druzyna(self, nazwa, id_turnieju):
        rozkaz = "DELETE FROM `druzyna` WHERE `druzyna`.`Nazwa` = '%s' AND `druzyna`.`Id_turnieju`=%s;" % (nazwa, id_turnieju)
        self.wykonaj_rozkaz(rozkaz)

    def szukaj_nastepne_id_druzyna(self):
        rozkaz = "SELECT * FROM druzyna"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def dodaj_zawodnik(self, id_zawodnika, imie, nazwisko, pozycja, id_druzyny, zdjecie = None):
        if zdjecie == None:
            rozkaz = "INSERT INTO `zawodnik` (`Id_zawodnika`, `Imie`, `Nazwisko`, `Pozycja`, `Id_druzyny`, `Zdjecie`) VALUES ('%s', '%s', '%s', '%s', '%s', '');" % (id_zawodnika, imie, nazwisko, pozycja, id_druzyny)
        else:
            rozkaz = "INSERT INTO `zawodnik` (`Id_zawodnika`, `Imie`, `Nazwisko`, `Pozycja`, `Id_druzyny`, `Zdjecie`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (id_zawodnika, imie, nazwisko, pozycja, id_druzyny, zdjecie)
        self.wykonaj_rozkaz(rozkaz)

    def usun_zawodnik(self, id_zawodnika):
        rozkaz = "DELETE FROM `zawodnik` WHERE `zawodnik`.`Id_zawodnika` = '%s';" % (id_zawodnika)
        self.wykonaj_rozkaz(rozkaz)

    def szukaj_nastepne_id_zawodnik(self):
        rozkaz = "SELECT * FROM zawodnik"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def znajdz_id_druzyny_po_nazwie(self, nazwa, id_turnieju):
        rozkaz = "SELECT Id_druzyny FROM druzyna WHERE Nazwa = '%s' AND Id_turnieju = '%s';" % (nazwa, id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def aktualizuj_statystyki_zawodnika(self, id_zawodnika, zdobyte, stracone):
        rozkaz = "CALL `update_player_statistics`('%s', '%s', '%s');" % (id_zawodnika, zdobyte, stracone)
        self.wykonaj_rozkaz(rozkaz)

    def aktualizuj_statystyki_druzyny(self, id_druzyny, czy_wygrana, zdobyte, stracone):
        rozkaz = "CALL `update_team_statistics`('%s', '%s', '%s', '%s');" % (id_druzyny, czy_wygrana, zdobyte, stracone)
        self.wykonaj_rozkaz(rozkaz)

    def pobierz_logo_druzyny(self, nazwa_druzyny, id_turnieju):
        rozkaz = "SELECT Logo FROM druzyna WHERE Nazwa = '%s' AND Id_turnieju = '%s';" % (nazwa_druzyny, id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def pobierz_statystyki_druzyny(self, nazwa_druzyny, id_turnieju):
        rozkaz = "SELECT * FROM statystyki_druzyny JOIN druzyna ON statystyki_druzyny.Id_druzyny = druzyna.Id_druzyny WHERE druzyna.Nazwa = '%s' AND druzyna.Id_turnieju = '%s';" % (nazwa_druzyny, id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def pobierz_statystyki_zawodnika(self, id_zawodnika):
        rozkaz = "SELECT * FROM statystyki_zawodnika WHERE Id_zawodnika = '%s';" % (id_zawodnika)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def sprawdz_admina(self, id_turnieju, nick, haslo):
        rozkaz = "SELECT uzytkownik.Nick, uzytkownik.haslo FROM uzytkownik JOIN `uzytkownik-turniej` ON `uzytkownik`.`Id_uzytkownika`=`uzytkownik-turniej`.`Id_uzytkownika` JOIN turniej ON turniej.Id_turnieju = `uzytkownik-turniej`.`Id_turnieju` WHERE turniej.Id_turnieju = '%s';" % (id_turnieju)
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        if results[0][0] == nick and results[0][1] == haslo:
            return True
        else:
            return False

    def najwiecej_wygranych(self):
        rozkaz = "SELECT druzyna.Nazwa, statystyki_druzyny.Ilosc_wygranych FROM druzyna JOIN statystyki_druzyny ON statystyki_druzyny.Id_druzyny=druzyna.Id_druzyny WHERE Ilosc_wygranych= (SELECT MAX(Ilosc_wygranych) FROM statystyki_druzyny);"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def najwiecej_zdobytych_punktow(self):
        rozkaz = "SELECT druzyna.Nazwa, statystyki_druzyny.Zdobyte_gole_pkt_kille FROM druzyna JOIN statystyki_druzyny ON statystyki_druzyny.Id_druzyny=druzyna.Id_druzyny WHERE Zdobyte_gole_pkt_kille= (SELECT MAX(Zdobyte_gole_pkt_kille) FROM statystyki_druzyny);"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results

    def najwiecej_straconych_punktow(self):
        rozkaz = "SELECT druzyna.Nazwa, statystyki_druzyny.Stracone_gole_pkt_ilosc_zginiec FROM druzyna JOIN statystyki_druzyny ON statystyki_druzyny.Id_druzyny=druzyna.Id_druzyny WHERE Stracone_gole_pkt_ilosc_zginiec= (SELECT MAX(Stracone_gole_pkt_ilosc_zginiec) FROM statystyki_druzyny);"
        results = self.wykonaj_rozkaz_i_zwroc(rozkaz)
        return results