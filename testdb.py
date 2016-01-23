import database
import sqlitedatabase

def main():
    dbMySQL = database.BazaMySQL('db4free.net', 'tournament', 'manager', 'tournamentmanage', "tournament_manager_baza_init.sql", "procedury.sql")
    dbMySQL.connect()

    dbMySQL.dodaj_turniej('1', '2', '1', '2016-02-15')
    #dbMySQL.usun_turniej('1')

    dbMySQL.dodaj_konto('administrator', '1')
    dbMySQL.dodaj_konto('user', '0')

    #dbMySQL.usun_konto('administrator')
    #dbMySQL.usun_konto('user')

    dbMySQL.dodaj_uzytkownik('1', 'Marcin', 'pass', 'administrator')
    #dbMySQL.usun_uzytkownik('1')

    #dbMySQL.dodaj_uzytkownik_turniej('1', '1')
    
    #dbMySQL.usun_druzyna('1')
    dbMySQL.dodaj_druzyna('1', 'Team1', '5', '1')

    dbMySQL.usun_zawodnik('1')
    dbMySQL.dodaj_zawodnik('1', 'Imie', 'Nazwisko', 'Mid', '1')

    #dbMySQL.disconnect()

    #dbSQLite = sqlitedatabase.BazaSQLite('tournament.db', "tournament_manager_baza_init_lite.sql", "procedury_wyzwalacze_lite.sql")
    #dbSQLite.connect()
    #dbSQLite.dodaj_turniej('5', '2', '1', '2016-02-15')

if __name__ == "__main__":
    main()