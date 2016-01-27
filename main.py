from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
import sys
import time

from ui_files import Ui_MainWindow
from bracket import Bracket
from druzyna import Druzyna
from zawodnik import Zawodnik
from elementsOfUi import *
from save import Save
from database import BazaMySQL



class TournamentManager(QtGui.QMainWindow):
    def __init__(self, *args):
        super(TournamentManager, self).__init__(*args)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bracket = Bracket()

        self.bracket_widget = BracketWidget()
        self.ui.horizontalLayout_2.addWidget(self.bracket_widget)

        self.connect_signals()
        self.ui.actionZapisz_screenshot_drzewa_turniejowego.setEnabled(False)
        self.ui.actionWczytaj_z_bazy_danych.setEnabled(False)
        self.ui.actionWczytaj_z_pliku.setEnabled(False)
        self.ui.actionZapisz_do_pliku.setEnabled(False)
        self.ui.actionZapisz_do_bazy_danych.setEnabled(False)

        self.typ_bazy = ""

        self.lista_druzyn = {}
        self.lista_zawodnikow = {}

    def connect_signals(self):
        QtCore.QObject.connect(self.ui.actionZapisz_screenshot_drzewa_turniejowego, QtCore.SIGNAL("triggered()"), self.zrob_screen)
        QtCore.QObject.connect(self.ui.actionNowy_turniej, QtCore.SIGNAL("triggered()"), self.nowy_turniej)
        QtCore.QObject.connect(self.ui.actionUstawienia, QtCore.SIGNAL("triggered()"), self.otworz_ustawienia)
        
    def nowy_turniej(self):
        self.nowy_turniej = NowyTurniejWidget()

        QtCore.QObject.connect(self.nowy_turniej.ui.pushButton, QtCore.SIGNAL("clicked()"), self.utworz_turniej)


        self.nowy_turniej.show()

    def utworz_turniej(self):
        self.ui.horizontalLayout_2.removeWidget(self.bracket_widget)
        del self.bracket_widget
        self.bracket_widget = BracketWidget()
        self.ui.horizontalLayout_2.addWidget(self.bracket_widget)
        self.number_of_teams = None
        number = self.nowy_turniej.ui.lineEdit.text()
        if number != "" :
            try:
                self.number_of_teams = int(number)
            except:
                error_window = QMessageBox.warning(self, "Error", "Niepoprawna liczba druzyn.")
        else:
            error_window = QMessageBox.warning(self, "Error", "Niepoprawna liczba druzyn.")

        if self.number_of_teams != None:
            self.create_bracket()
            self.nowy_turniej.close()
            self.ui.actionZapisz_screenshot_drzewa_turniejowego.setEnabled(True)

        #Baza

        if self.nowy_turniej.ui.radioButton_3.isChecked():
            adres = str(self.nowy_turniej.ui.lineEdit_2.text())
            nazwa_uzytkownika = str(self.nowy_turniej.ui.lineEdit_3.text())
            haslo = str(self.nowy_turniej.ui.lineEdit_4.text())
            nazwa_bazy = str(self.nowy_turniej.ui.lineEdit_5.text())
            self.baza = BazaMySQL(adres, nazwa_uzytkownika, haslo, nazwa_bazy, "tournament_manager_baza_init.sql", "procedury.sql")
            self.baza.connect()

            spis_turniejow_w_bazie = self.baza.szukaj_nastepne_id_turnieju()
            try:
                najwiekszy = spis_turniejow_w_bazie[0][0]
            except:
                najwiekszy = 0
            for row in spis_turniejow_w_bazie:
                if row[0] > najwiekszy:
                    najwiekszy = row[0]

            self.id_turnieju = najwiekszy + 1
            ilosc_druzyn = self.number_of_teams
            if self.nowy_turniej.ui.radioButton.isChecked():
                czy_posiada_faze_grupowa = 1
            if self.nowy_turniej.ui.radioButton_2.isChecked():
                czy_posiada_faze_grupowa = 0
            data_rozpoczecia = time.strftime("%Y-%m-%d")
            self.baza.dodaj_turniej(self.id_turnieju, ilosc_druzyn, czy_posiada_faze_grupowa, data_rozpoczecia)

        
        spis_uzytkownikow_w_bazie = self.baza.szukaj_nastepne_id_uzytkownika()
        try:
            najwiekszy = spis_uzytkownikow_w_bazie[0][0]
        except:
            najwiekszy = 0
        for row in spis_uzytkownikow_w_bazie:
            if row[0] > najwiekszy:
                najwiekszy = row[0]

        id = najwiekszy + 1
        nick = str(self.nowy_turniej.ui.lineEdit_6.text())
        haslo = str(self.nowy_turniej.ui.lineEdit_7.text())
        rodzaj = "administrator"
        self.baza.dodaj_uzytkownik(id, nick, haslo, rodzaj)

        self.baza.dodaj_uzytkownik_turniej(self.id_turnieju, id)

    def create_bracket(self):
        #self.ui_bracket_widget = self.bracket_widget.ui
        self.bracket.init_bracket(self.bracket_widget, self.number_of_teams, self.lista_druzyn)

    def zrob_screen(self):
        save = Save()
        save.take_screenshot(self.bracket_widget.ui)

    def otworz_ustawienia(self):
        self.ustawienia = UstawieniaWidget()
        
        QtCore.QObject.connect(self.ustawienia.ui.pushButton, QtCore.SIGNAL("clicked()"), self.otworz_druzyny)
        QtCore.QObject.connect(self.ustawienia.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.otworz_zawodnicy)

        self.ustawienia.show()

    def otworz_zawodnicy(self):
        self.zawodnicy = ZawodnicyWidget()

        QtCore.QObject.connect(self.zawodnicy.ui.pushButton_dodaj, QtCore.SIGNAL("clicked()"), self.dodaj_zawodnika)
        QtCore.QObject.connect(self.zawodnicy.ui.pushButton_usun, QtCore.SIGNAL("clicked()"), self.usun_zawodnika)


        self.odswiez_liste_zawodnikow()

        self.zawodnicy.show()

    def usun_zawodnika(self):
        zawodnik_do_usuniecia = str(self.zawodnicy.ui.listWidget.currentItem().text())
        id_zawodnika = self.lista_zawodnikow[zawodnik_do_usuniecia].getId_zawodnika()
        del self.lista_zawodnikow[zawodnik_do_usuniecia]

        self.baza.usun_zawodnik(id_zawodnika)

        self.odswiez_liste_zawodnikow()

    def odswiez_liste_zawodnikow(self):
        self.zawodnicy.ui.listWidget.clear()

        for nazwa_zawodnika, zawodnik in self.lista_zawodnikow.items():
            self.zawodnicy.ui.listWidget.addItem(zawodnik.getImie() + " " + zawodnik.getNazwisko() + " (" + zawodnik.getDruzyna() + ")")

        self.zawodnicy.ui.comboBox.clear()

        for nazwa_druzyny, druzyna in self.lista_druzyn.items():
            self.zawodnicy.ui.comboBox.addItem(nazwa_druzyny)

    def dodaj_zawodnika(self):
        imie = str(self.zawodnicy.ui.lineEdit.text())
        nazwisko = str(self.zawodnicy.ui.lineEdit_2.text())
        pozycja = str(self.zawodnicy.ui.lineEdit_3.text())
        do_druzyny = str(self.zawodnicy.ui.comboBox.currentText())
        if imie != "" and nazwisko != "" and pozycja != "" and do_druzyny != "":
            spis_zawodnikow_w_bazie = self.baza.szukaj_nastepne_id_zawodnik()
            try:
                najwiekszy = spis_zawodnikow_w_bazie[0][0]
            except:
                najwiekszy = 0

            for row in spis_zawodnikow_w_bazie:
                if row[0] > najwiekszy:
                    najwiekszy = row[0]

            id_zawodnika = najwiekszy + 1

            nowy_zawodnik = Zawodnik(imie, nazwisko, pozycja, do_druzyny, id_zawodnika)
            nazwa_do_slownika = imie +" "+ nazwisko +" ("+ do_druzyny +")"
            self.lista_zawodnikow[nazwa_do_slownika] = nowy_zawodnik
            self.odswiez_liste_zawodnikow()
            self.zawodnicy.ui.lineEdit.clear()
            self.zawodnicy.ui.lineEdit_2.clear()
            self.zawodnicy.ui.lineEdit_3.clear()
            
            id_turnieju = self.id_turnieju
            zdjecie = None

            id_druzyny = self.baza.znajdz_id_druzyny_po_nazwie(do_druzyny, id_turnieju)[0][0]

            self.baza.dodaj_zawodnik(id_zawodnika, imie, nazwisko, pozycja, id_druzyny, zdjecie)
        else:
            error_window = QMessageBox.warning(self, "Error", "Uzupelnij wszystkie dane")

    def otworz_druzyny(self):
        self.druzyny = DruzynyWidget()

        QtCore.QObject.connect(self.druzyny.ui.pushButton_dodaj, QtCore.SIGNAL("clicked()"), self.dodaj_druzyne)
        QtCore.QObject.connect(self.druzyny.ui.pushButton_usun, QtCore.SIGNAL("clicked()"), self.usun_druzyne)
        QtCore.QObject.connect(self.druzyny.ui.pushButton_losuj_drzewko, QtCore.SIGNAL("clicked()"), self.losuj_drzewko)

        self.odswiez_liste_druzyn()

        self.druzyny.show()

    def dodaj_druzyne(self):
        nazwa_druzyny = self.druzyny.ui.lineEdit.text()
        if nazwa_druzyny != "":
            nowa_druzyna = Druzyna(nazwa_druzyny)
            self.lista_druzyn[nazwa_druzyny] = nowa_druzyna
            self.odswiez_liste_druzyn()
            self.druzyny.ui.lineEdit.clear()
            ilosc_zawodnikow = self.druzyny.ui.lineEdit_2.text().toInt()[0]
            self.druzyny.ui.lineEdit_2.clear()

            spis_druzyn_w_bazie = self.baza.szukaj_nastepne_id_druzyna()
            try:
                najwiekszy = spis_druzyn_w_bazie[0][0]
            except:
                najwiekszy = 0
            for row in spis_druzyn_w_bazie:
                if row[0] > najwiekszy:
                    najwiekszy = row[0]

            id_druzyny = najwiekszy + 1
            
            id_turnieju = self.id_turnieju
            logo = None
            self.baza.dodaj_druzyna(id_druzyny, nazwa_druzyny, ilosc_zawodnikow, id_turnieju, logo)
        else:
            error_window = QMessageBox.warning(self, "Error", "Nazwa druzyny nie moze byc pusta.")

    def usun_druzyne(self):
        druzyna_do_usuniecia = self.druzyny.ui.listWidget.currentItem().text()
        del self.lista_druzyn[druzyna_do_usuniecia]

        self.baza.usun_druzyna(druzyna_do_usuniecia, self.id_turnieju)

        self.odswiez_liste_druzyn()

    def odswiez_liste_druzyn(self):
        self.druzyny.ui.listWidget.clear()

        for nazwa_druzyny, druzyna in self.lista_druzyn.items():
            self.druzyny.ui.listWidget.addItem(nazwa_druzyny)

    def losuj_drzewko(self):
        try:
            if bool(self.lista_druzyn):
                self.bracket.losuj_drzewko()
        except:
            error_window = QMessageBox.warning(self, "Brak drzewka", "Najpierw stworz nowe drzewko turniejowe.")

def main():
    app = QtGui.QApplication(sys.argv)
    tournament_manager = TournamentManager()
    if (len(sys.argv) > 1):
        tournament_manager.number_of_teams = int(sys.argv[1])
        tournament_manager.create_bracket()
        tournament_manager.ui.actionZapisz_screenshot_drzewa_turniejowego.setEnabled(True)
    tournament_manager.show()
    app.exec_()

if __name__ == '__main__':
    main()
