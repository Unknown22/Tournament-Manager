from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
import sys

from ui_files import Ui_MainWindow
from bracket import Bracket
from druzyna import Druzyna
from elementsOfUi import *
from save import Save



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

        self.lista_druzyn = {}

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

    def create_bracket(self):
        #self.ui_bracket_widget = self.bracket_widget.ui
        self.bracket.init_bracket(self.bracket_widget, self.number_of_teams, self.lista_druzyn)

    def zrob_screen(self):
        save = Save()
        save.take_screenshot(self.bracket_widget.ui)

    def otworz_ustawienia(self):
        self.ustawienia = UstawieniaWidget()
        
        QtCore.QObject.connect(self.ustawienia.ui.pushButton, QtCore.SIGNAL("clicked()"), self.otworz_druzyny)

        self.ustawienia.show()

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
        else:
            error_window = QMessageBox.warning(self, "Error", "Nazwa druzyny nie moze byc pusta.")

    def usun_druzyne(self):
        druzyna_do_usuniecia = self.druzyny.ui.listWidget.currentItem().text()
        del self.lista_druzyn[druzyna_do_usuniecia]
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
    tournament_manager.show()
    app.exec_()

if __name__ == '__main__':
    main()
