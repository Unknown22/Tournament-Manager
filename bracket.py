from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from random import randint
import time

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

        self.nastepny_mecz_numer = 0
        self.nastepny_numer_groupboxa = 0

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

        self.suma_przyciskow = self.list_of_teams_in_groupbox[self.nastepny_numer_groupboxa]

        self.connect_signals()

    def add_teams_button(self):
        self.liczba_przyciskow_na_starcie = 0
        button_number = 0;
        for number_of_groupbox in range(self.number_of_groupbox):
            for team_number in range(self.list_of_teams_in_groupbox[number_of_groupbox]):
                button = QPushButton("...")
                self.list_of_layouts_in_groupbox[number_of_groupbox].addWidget(button, team_number, 0)
                self.list_of_buttons[button_number] = button
                #if(number_of_groupbox != 0):
                #    button.setEnabled(False)
                if(number_of_groupbox == 0):
                    self.liczba_przyciskow_na_starcie += 1
                button_number += 1

    def connect_signals(self):
        QtCore.QObject.connect(self.ui.ui.pushButton, QtCore.SIGNAL("clicked()"), self.otworz_nastepny_mecz)
        for button_number, button in self.list_of_buttons.items():
            QtCore.QObject.connect(self.list_of_buttons[button_number], QtCore.SIGNAL("clicked()"), lambda button_number = button_number: self.otworz_okno_druzyny(button_number))

    def otworz_nastepny_mecz(self):
        liczba_przyciskow = len(self.list_of_buttons)
        try:
            self.nastepny_mecz = NastepnyMeczWidget()
            QtCore.QObject.connect(self.nastepny_mecz.ui.pushButton, QtCore.SIGNAL("clicked()"), self.aktualizuj_staty_teamu)
            if self.nastepny_mecz_numer + 1 < liczba_przyciskow:
                self.team1 = self.lista_druzyn_przypisana_do_przyciskow[self.nastepny_mecz_numer].getNazwa()
                self.team2 = self.lista_druzyn_przypisana_do_przyciskow[self.nastepny_mecz_numer+1].getNazwa()
                self.nastepny_mecz.ui.label.setText(self.team1)
                self.nastepny_mecz.ui.label_2.setText(self.team2)
                self.nastepny_mecz.show()

            else:
                info_window = QMessageBox.information(self, "Info", "Wygrywa: " + str(self.lista_druzyn_przypisana_do_przyciskow[self.nastepny_mecz_numer].getNazwa())) 

            if self.nastepny_mecz_numer + 1 < self.suma_przyciskow:
                self.nastepny_mecz_numer = self.nastepny_mecz_numer + 2
                if self.nastepny_mecz_numer >= self.suma_przyciskow:
                    self.nastepny_numer_groupboxa = self.nastepny_numer_groupboxa + 1
                    self.suma_przyciskow = self.suma_przyciskow + self.list_of_teams_in_groupbox[self.nastepny_numer_groupboxa]
            else:
                self.nastepny_mecz_numer = self.nastepny_mecz_numer + 1
                self.nastepny_numer_groupboxa = self.nastepny_numer_groupboxa + 1
                self.suma_przyciskow = self.suma_przyciskow + self.list_of_teams_in_groupbox[self.nastepny_numer_groupboxa]
        except:
            pass

    def aktualizuj_staty_teamu(self):
        id_druzyny1 = self.baza.znajdz_id_druzyny_po_nazwie(self.team1, self.id_turnieju)
        zdobyte = int(str(self.nastepny_mecz.ui.lineEdit.text()))
        stracone = int(str(self.nastepny_mecz.ui.lineEdit_2.text()))
        if zdobyte > stracone:
            czy_wygrana = 1
        else:
            czy_wygrana = 0

        self.baza.aktualizuj_statystyki_druzyny(id_druzyny1[0][0], czy_wygrana, zdobyte, stracone)

        id_druzyny2 = self.baza.znajdz_id_druzyny_po_nazwie(self.team2, self.id_turnieju)
        zdobyte = int(str(self.nastepny_mecz.ui.lineEdit_2.text()))
        stracone = int(str(self.nastepny_mecz.ui.lineEdit.text()))
        if zdobyte > stracone:
            czy_wygrana = 1
        else:
            czy_wygrana = 0
        self.baza.aktualizuj_statystyki_druzyny(id_druzyny2[0][0], czy_wygrana, zdobyte, stracone)


        spis_meczy_w_bazie = self.baza.szukaj_nastepne_id_meczu()
        try:
            najwiekszy = spis_meczy_w_bazie[0][0]
        except:
            najwiekszy = 0
        for row in spis_meczy_w_bazie:
            if row[0] > najwiekszy:
                najwiekszy = row[0]

        id_meczu = najwiekszy + 1
        wynik = str(stracone) + ":" + str(zdobyte)
        data = time.strftime("%Y-%m-%d")
        self.baza.dodaj_mecz(id_meczu, wynik, data, self.id_turnieju, id_druzyny1[0][0], id_druzyny2[0][0])
        
        self.nastepny_mecz.close()

    def przekaz_id_turnieju(self, id):
        self.id_turnieju = id

    def otworz_okno_druzyny(self, numer):
        self.okno_druzyny = OknoDruzyny()
        if numer in self.lista_druzyn_przypisana_do_przyciskow:
            self.odswiez_okno(numer)
        else:
            self.okno_druzyny.ui.label_liczba_wygranych.setText("")
            self.okno_druzyny.ui.label_liczba_przegranych.setText("")
            self.okno_druzyny.ui.label_zdobyte_punkty.setText("")
            self.okno_druzyny.ui.label_stracone_punkty.setText("")
            self.okno_druzyny.ui.label_zdobyte_punkty_zawodnik.setText("")
            self.okno_druzyny.ui.label_stracone_punkty_zawodnik.setText("")
            self.okno_druzyny.ui.label_rozegrane_mecze.setText("")

        for team_name, team in self.lista_druzyn.items():
            self.okno_druzyny.ui.comboBox.addItem(team_name)

        QtCore.QObject.connect(self.okno_druzyny.ui.pushButton, QtCore.SIGNAL("clicked()"), lambda numer = numer: self.przypisz_druzyne(numer))
        self.okno_druzyny.ui.listWidget.currentItemChanged.connect(self.odswiez_staty_zawodnika)
        
        self.okno_druzyny.ui.groupBox_3.setVisible(False)
        self.okno_druzyny.resize(250,330)

        self.okno_druzyny.show()

    def odswiez_staty_zawodnika(self):
        zawodnik = self.okno_druzyny.ui.listWidget.currentItem().text()

        for member in self.druzyna_do_odswiezania_statow_zawodnikow.zawodnicy:
            do_sprawdzenia = member.getImie() + " " + member.getNazwisko()
            if do_sprawdzenia == zawodnik:
                id_zawodnika_do_odswiezenia_statow = member.getId_zawodnika()

        statystyki_zawodnika = self.baza.pobierz_statystyki_zawodnika(id_zawodnika_do_odswiezenia_statow)

        self.okno_druzyny.ui.label_zdobyte_punkty_zawodnik.setText(str(statystyki_zawodnika[0][1]))
        self.okno_druzyny.ui.label_stracone_punkty_zawodnik.setText(str(statystyki_zawodnika[0][2]))
        self.okno_druzyny.ui.label_rozegrane_mecze.setText(str(statystyki_zawodnika[0][3]))
        self.okno_druzyny.ui.groupBox_3.setVisible(False)

    def przypisz_druzyne(self, numer, nazwa=None):
        if nazwa == None:
            nazwa_druzyny_do_przypisania = self.okno_druzyny.ui.comboBox.currentText()
        else:
            nazwa_druzyny_do_przypisania = nazwa
        if nazwa_druzyny_do_przypisania != "":
            self.lista_druzyn_przypisana_do_przyciskow[numer] = self.lista_druzyn[str(nazwa_druzyny_do_przypisania)]
            if nazwa == None:
                self.odswiez_okno(numer)
        else:
            error_window = QMessageBox.warning(self, "Brak druzyn", "Najpierw dodaj jakies druzyny.")     

    def odswiez_okno(self, numer):
        druzyna = self.lista_druzyn_przypisana_do_przyciskow[numer]
        self.druzyna_do_odswiezania_statow_zawodnikow = druzyna
        self.okno_druzyny.ui.label_2.setText(druzyna.getNazwa())
        
        self.okno_druzyny.ui.listWidget.clear()
        for member in druzyna.zawodnicy:
            do_dodania = member.getImie() + " " + member.getNazwisko()
            self.okno_druzyny.ui.listWidget.addItem(do_dodania)

        ##
        statystyki_druzyny = self.baza.pobierz_statystyki_druzyny(druzyna.getNazwa(), self.id_turnieju)
        self.okno_druzyny.ui.label_liczba_wygranych.setText(str(statystyki_druzyny[0][1]))
        self.okno_druzyny.ui.label_liczba_przegranych.setText(str(statystyki_druzyny[0][2]))
        self.okno_druzyny.ui.label_zdobyte_punkty.setText(str(statystyki_druzyny[0][3]))
        self.okno_druzyny.ui.label_stracone_punkty.setText(str(statystyki_druzyny[0][4]))
        ##

        self.odswiez_przyciski_na_drzewku(numer, druzyna)



    def przekaz_baze(self, baza):
        self.baza = baza

    def odswiez_przyciski_na_drzewku(self, numer, druzyna):
        self.list_of_buttons[numer].setText(druzyna.getNazwa())

    def losuj_drzewko(self):
        random = randint(0, self.liczba_przyciskow_na_starcie-1)

        for nazwa, druzyna in self.lista_druzyn.items():
            while self.list_of_buttons[random].text() != "...":
                random = randint(0, self.liczba_przyciskow_na_starcie-1)
            self.przypisz_druzyne(random, nazwa)
            self.odswiez_przyciski_na_drzewku(random, druzyna)