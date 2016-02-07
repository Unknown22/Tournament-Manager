import database
#import sqlitedatabase
import sys

def main():
    dbMySQL = database.BazaMySQL('127.0.0.1', 'root', '', 'tournamentmanager', "tournament_manager_baza_init.sql", "procedury.sql")
    dbMySQL.connect()

    dbMySQL.dodaj_turniej('1', '2', '1', '2016-02-15')
    #dbMySQL.usun_turniej('1')

    #dbMySQL.dodaj_konto('administrator', '1')
    #dbMySQL.dodaj_konto('user', '0')

    #dbMySQL.usun_konto('administrator')
    #dbMySQL.usun_konto('user')

    #dbMySQL.dodaj_uzytkownik('1', 'Marcin', 'pass', 'administrator')
    #dbMySQL.usun_uzytkownik('1')

    #dbMySQL.dodaj_uzytkownik_turniej('1', '1')
    
    #dbMySQL.usun_druzyna('1')
    #dbMySQL.dodaj_druzyna('1', 'Team1', '5', '1')

    fin = open("logo.jpg", 'rb')
    img = fin.read()
    fin.close()

    dbMySQL.dodaj_druzyna('4', 'TeamLOGO5', '5', '1', img)

    #dbMySQL.usun_zawodnik('1')
    #dbMySQL.dodaj_zawodnik('1', 'Imie', 'Nazwisko', 'Mid', '1')

    #dbMySQL.aktualizuj_statystyki_zawodnika('1', '2', '1')
    #dbMySQL.aktualizuj_statystyki_druzyny('1', '1', '6', '1')

    #dbMySQL.pokaz_turniej(2)

    #dbMySQL.disconnect()

    #dbSQLite = sqlitedatabase.BazaSQLite('tournament.db', "tournament_manager_baza_init_lite.sql", "procedury_wyzwalacze_lite.sql")
    #dbSQLite.connect()
    #dbSQLite.dodaj_turniej('5', '2', '1', '2016-02-15')

if __name__ == "__main__":
    main()