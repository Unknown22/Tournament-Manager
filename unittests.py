import unittest
from zawodnik import Zawodnik
from druzyna import Druzyna
from bracket import Bracket
from elementsOfUi import BracketWidget
from ui_files import ui_nowy_turniej
from random import randint

class TestZawodnik(unittest.TestCase):

    def testuj_tworzenie_nowego_zawodnika(self):
        zawodnik = Zawodnik("Imie", "Nazwisko")
        expected_result = 'Imie'
        result = zawodnik.getImie()
        self.assertEqual(result, expected_result)
        
        expected_result = 'Nazwisko'
        result = zawodnik.getNazwisko()
        self.assertEqual(result, expected_result)

    def testuj_tworzenie_nowego_zawodnika_o_dowolnych_danych(self):
        zawodnik = Zawodnik("dowolne imie", "dowolne_nazwisko")
        expected_regexp = ".+"
        result = zawodnik.getImie()
        self.assertRegexpMatches(result, expected_regexp)

        result = zawodnik.getNazwisko()
        self.assertRegexpMatches(result, expected_regexp)

    def testuj_tworzenie_nowego_zawodnika_bez_danych(self):
        with self.assertRaises(AssertionError) as context:
            zawodnik = Zawodnik("","")
            expected_regexp = '.+'
            result = zawodnik.getImie()
            self.assertRegexpMatches(result, expected_regexp)
        expected_message = "AssertRaisesContext"
        self.assertIn(expected_message, str(context))

        with self.assertRaises(AssertionError) as context:
            zawodnik = Zawodnik("","")
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

if __name__ == '__main__':
    unittest.main()