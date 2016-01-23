import sqlite3 as lite
import sys

class BazaSQLite(object):
    def __init__(self, nazwa_pliku, plik_init, plik_procedury):
        self.nazwa_pliku = nazwa_pliku
        self.plik_init = plik_init
        self.plik_procedury = plik_procedury

    def connect(self):
        self.con = lite.connect(self.nazwa_pliku)
        self.c = self.con.cursor()
        self.executeScriptsFromFile(self.plik_init, self.plik_procedury)

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
                #print command
        self.con.commit()

    def dodaj_turniej(self, id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia):
        rozkaz = "INSERT INTO `turniej` VALUES (%s, %s, %s, '%s');"  % (id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia)
        print rozkaz
        try:
            self.c.execute(rozkaz)
        except:
            self.con.rollback()
        self.con.commit()