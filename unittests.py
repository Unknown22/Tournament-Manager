import unittest
from zawodnik import Zawodnik
from druzyna import Druzyna
from bracket import Bracket
from elementsOfUi import BracketWidget
from ui_files import ui_nowy_turniej
from random import randint
from database import BazaMySQL

class TestZawodnik(unittest.TestCase):

    def testuj_tworzenie_nowego_zawodnika(self):
        zawodnik = Zawodnik("Imie", "Nazwisko", "Pozycja", "Druzyna", "1")
        expected_result = 'Imie'
        result = zawodnik.getImie()
        self.assertEqual(result, expected_result)
        
        expected_result = 'Nazwisko'
        result = zawodnik.getNazwisko()
        self.assertEqual(result, expected_result)

        expected_result = 'Pozycja'
        result = zawodnik.getPozycja()
        self.assertEqual(result, expected_result)

        expected_result = 'Druzyna'
        result = zawodnik.getDruzyna()
        self.assertEqual(result, expected_result)

        expected_result = '1'
        result = zawodnik.getId_zawodnika()
        self.assertEqual(result, expected_result)

    def testuj_tworzenie_nowego_zawodnika_o_dowolnych_danych(self):
        zawodnik = Zawodnik("dowolne imie", "dowolne_nazwisko", "dowolna_pozycja", "dowolna_druzyna", "12345")
        expected_regexp = ".+"
        result = zawodnik.getImie()
        self.assertRegexpMatches(result, expected_regexp)

        result = zawodnik.getNazwisko()
        self.assertRegexpMatches(result, expected_regexp)

        result = zawodnik.getPozycja()
        self.assertRegexpMatches(result, expected_regexp)

        result = zawodnik.getDruzyna()
        self.assertRegexpMatches(result, expected_regexp)

        result = zawodnik.getId_zawodnika()
        self.assertRegexpMatches(result, expected_regexp)

    def testuj_tworzenie_nowego_zawodnika_bez_danych(self):
        with self.assertRaises(AssertionError) as context:
            zawodnik = Zawodnik("","", "", "", "")
            expected_regexp = '.+'
            result = zawodnik.getImie()
            self.assertRegexpMatches(result, expected_regexp)
        expected_message = "AssertRaisesContext"
        self.assertIn(expected_message, str(context))

        with self.assertRaises(AssertionError) as context:
            zawodnik = Zawodnik("","", "", "", "")
            expected_regexp = '.+'
            result = zawodnik.getNazwisko()
            self.assertRegexpMatches(result, expected_regexp)
        expected_message = "AssertRaisesContext"
        self.assertIn(expected_message, str(context))

class TestDruzyna(unittest.TestCase):

    def testuj_tworzenie_nowej_druzyny(self):
        druzyna = Druzyna("Nazwa")
        expected_result = 'Nazwa'
        result = druzyna.getNazwa()
        self.assertEqual(result, expected_result)

    def testuj_tworzenie_nowej_druzyny_z_dowolna_nazwa(self):
        druzyna = Druzyna("dowolna nazwa")
        expected_regexp = '.+'
        result = druzyna.getNazwa()
        self.assertRegexpMatches(result, expected_regexp)

    def testu_tworzenie_nowej_druzyny_bez_nazwy(self):
        with self.assertRaises(AssertionError) as context:
            druzyna = Druzyna("")
            expected_regexp = '.+'
            result = druzyna.getNazwa()
            self.assertRegexpMatches(result, expected_regexp)
        expected_message = "AssertRaisesContext"
        self.assertIn(expected_message, str(context))

class TestBazaDanych(unittest.TestCase):

    def testuj_dodawanie_turnieju(self):
        dbMySQL = BazaMySQL('127.0.0.1', 'root', '', 'tournamentmanager', "tournament_manager_baza_init.sql", "procedury.sql")
        dbMySQL.connect()
        dbMySQL.dodaj_turniej('15', '2', '1', '2016-02-15')
        expected_result = '[[15L, 2L, True, datetime.date(2016, 2, 15)]]'
        result = str(dbMySQL.pokaz_turniej('15'))
        self.assertEqual(result, expected_result)

    def testuj_usuwanie_turnieju(self):
        dbMySQL = BazaMySQL('127.0.0.1', 'root', '', 'tournamentmanager', "tournament_manager_baza_init.sql", "procedury.sql")
        dbMySQL.connect()
        dbMySQL.usun_turniej('15')
        expected_result = '[]'
        result = str(dbMySQL.pokaz_turniej('15'))
        self.assertEqual(result, expected_result)

    def testuj_dodawanie_meczu(self):
        dbMySQL = BazaMySQL('127.0.0.1', 'root', '', 'tournamentmanager', "tournament_manager_baza_init.sql", "procedury.sql")
        dbMySQL.connect()
        dbMySQL.dodaj_mecz('15', '1:2', '2016-01-27', '1', '1', '2')
        expected_result = "((15L, '1:2', datetime.date(2016, 1, 27), 1L, 1L, 2L),)"
        result = str(dbMySQL.pokaz_mecz('15'))
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()