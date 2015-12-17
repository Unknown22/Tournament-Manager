from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from random import randint

from elementsOfUi import *

class Bracket(QtGui.QWidget):

    def init_bracket(self, ui, team_number, druzyny):
        self.team_number = team_number
        self.ui = ui
        self.lista_druzyn = druzyny

        self.number_of_groupbox = 0
        self.list_of_groupbox = []
        self.list_of_layouts_in_groupbox = []
        self.list_of_teams_in_groupbox = []
        self.list_of_buttons = {}
        self.lista_druzyn_przypisana_do_przyciskow = {}

        if team_number != 0:
            result = team_number
            self.list_of_teams_in_groupbox.append(result)
            while (result != 1):
                if team_number % 2 != 0:
                    team_number = team_number + 1
                self.number_of_groupbox += 1
                result = team_number / 2
                self.list_of_teams_in_groupbox.append(result)
                team_number = result
            self.number_of_groupbox += 1

        for x in range(self.number_of_groupbox):
            groupBox = QGroupBox()
            layout = QtGui.QGridLayout()
            self.list_of_layouts_in_groupbox.append(layout)
            groupBox.setLayout(layout)
            self.list_of_groupbox.append(groupBox)
            self.ui.ui.gridLayout_2.addWidget(groupBox, 0, x)

        self.add_teams_button()
        self.connect_signals()

    def add_teams_button(self):
        self.liczba_przyciskow_na_starcie = 0
        button_number = 0;
        for number_of_groupbox in range(self.number_of_groupbox):
            for team_number in range(self.list_of_teams_in_groupbox[number_of_groupbox]):
                button = QPushButton("...")
                self.list_of_layouts_in_groupbox[number_of_groupbox].addWidget(button, team_number, 0)
                self.list_of_buttons[button_number] = button
                if(number_of_groupbox != 0):
                    button.setEnabled(False)
                if(number_of_groupbox == 0):
                    self.liczba_przyciskow_na_starcie += 1
                button_number += 1

    def connect_signals(self):
        for button_number, button in self.list_of_buttons.items():
            QtCore.QObject.connect(self.list_of_buttons[button_number], QtCore.SIGNAL("clicked()"), lambda button_number = button_number: self.otworz_okno_druzyny(button_number))

    def otworz_okno_druzyny(self, numer):
        self.okno_druzyny = OknoDruzyny()
        if numer in self.lista_druzyn_przypisana_do_przyciskow:
            self.odswiez_okno(numer)
        for team_name, team in self.lista_druzyn.items():
            self.okno_druzyny.ui.comboBox.addItem(team_name)

        QtCore.QObject.connect(self.okno_druzyny.ui.pushButton, QtCore.SIGNAL("clicked()"), lambda numer = numer: self.przypisz_druzyne(numer))

        self.okno_druzyny.show()

    def przypisz_druzyne(self, numer, nazwa=None):
        if nazwa == None:
            nazwa_druzyny_do_przypisania = self.okno_druzyny.ui.comboBox.currentText()
        else:
            nazwa_druzyny_do_przypisania = nazwa
        if nazwa_druzyny_do_przypisania != "":
            self.lista_druzyn_przypisana_do_przyciskow[numer] = self.lista_druzyn[nazwa_druzyny_do_przypisania]
            if nazwa == None:
                self.odswiez_okno(numer)
        else:
            error_window = QMessageBox.warning(self, "Brak druzyn", "Najpierw dodaj jakies druzyny.")     

    def odswiez_okno(self, numer):
        druzyna = self.lista_druzyn_przypisana_do_przyciskow[numer]
        self.okno_druzyny.ui.label_2.setText(druzyna.getNazwa())
        
        self.okno_druzyny.ui.listWidget.clear()
        for member in druzyna.zawodnicy:
            self.okno_druzyny.ui.listWidget.addItem(member)

        self.odswiez_przyciski_na_drzewku(numer, druzyna)

    def odswiez_przyciski_na_drzewku(self, numer, druzyna):
        self.list_of_buttons[numer].setText(druzyna.getNazwa())

    def losuj_drzewko(self):
        random = randint(0, self.liczba_przyciskow_na_starcie-1)

        for nazwa, druzyna in self.lista_druzyn.items():
            while self.list_of_buttons[random].text() != "...":
                random = randint(0, self.liczba_przyciskow_na_starcie-1)
            self.przypisz_druzyne(random, nazwa)
            self.odswiez_przyciski_na_drzewku(random, druzyna)