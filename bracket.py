from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
            ui.ui.gridLayout_2.addWidget(groupBox, 0, x)

        self.add_teams_button()
        self.connect_signals()

    def add_teams_button(self):
        button_number = 0;
        for number_of_groupbox in range(self.number_of_groupbox):
            for team_number in range(self.list_of_teams_in_groupbox[number_of_groupbox]):
                button = QPushButton("...")
                self.list_of_layouts_in_groupbox[number_of_groupbox].addWidget(button, team_number, 0)
                self.list_of_buttons[button_number] = button
                button_number += 1

    def connect_signals(self):
        for button_number, button in self.list_of_buttons.items():
            QtCore.QObject.connect(self.list_of_buttons[button_number], QtCore.SIGNAL("clicked()"), lambda button_number = button_number: self.otworz_okno_druzyny(button_number))

    def otworz_okno_druzyny(self, numer):
        if numer in self.lista_druzyn_przypisana_do_przyciskow:
            print self.lista_druzyn_przypisana_do_przyciskow[numer].getNazwa()
        self.okno_druzyny = OknoDruzyny()
        for team_name, team in self.lista_druzyn.items():
            self.okno_druzyny.ui.comboBox.addItem(team_name)

        QtCore.QObject.connect(self.okno_druzyny.ui.pushButton, QtCore.SIGNAL("clicked()"), lambda number = numer: self.przypisz_druzyne(numer))

        self.okno_druzyny.show()

    def przypisz_druzyne(self, numer):
        nazwa_druzyny_do_przypisania = self.okno_druzyny.ui.comboBox.currentText()
        if nazwa_druzyny_do_przypisania != "":
            self.lista_druzyn_przypisana_do_przyciskow[numer] = self.lista_druzyn[nazwa_druzyny_do_przypisania]
        else:
            error_window = QMessageBox.warning(self, "Brak druzyn", "Najpierw dodaj jakies druzyny.")

        print self.lista_druzyn_przypisana_do_przyciskow[numer]