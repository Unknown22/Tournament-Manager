# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno_druzyny.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_oknoDruzynyForm(object):
    def setupUi(self, oknoDruzynyForm):
        oknoDruzynyForm.setObjectName(_fromUtf8("oknoDruzynyForm"))
        oknoDruzynyForm.resize(300, 377)
        self.gridLayout_3 = QtGui.QGridLayout(oknoDruzynyForm)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(oknoDruzynyForm)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 56))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(oknoDruzynyForm)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_liczba_wygranych = QtGui.QLabel(self.groupBox_2)
        self.label_liczba_wygranych.setObjectName(_fromUtf8("label_liczba_wygranych"))
        self.gridLayout_4.addWidget(self.label_liczba_wygranych, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_liczba_przegranych = QtGui.QLabel(self.groupBox_2)
        self.label_liczba_przegranych.setObjectName(_fromUtf8("label_liczba_przegranych"))
        self.gridLayout_4.addWidget(self.label_liczba_przegranych, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_zdobyte_punkty = QtGui.QLabel(self.groupBox_2)
        self.label_zdobyte_punkty.setObjectName(_fromUtf8("label_zdobyte_punkty"))
        self.gridLayout_4.addWidget(self.label_zdobyte_punkty, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_stracone_punkty = QtGui.QLabel(self.groupBox_2)
        self.label_stracone_punkty.setObjectName(_fromUtf8("label_stracone_punkty"))
        self.gridLayout_4.addWidget(self.label_stracone_punkty, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 5, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_4.addWidget(self.listWidget, 5, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_stracone_punkty_zawodnik = QtGui.QLabel(self.groupBox_3)
        self.label_stracone_punkty_zawodnik.setText(_fromUtf8(""))
        self.label_stracone_punkty_zawodnik.setObjectName(_fromUtf8("label_stracone_punkty_zawodnik"))
        self.gridLayout.addWidget(self.label_stracone_punkty_zawodnik, 1, 1, 1, 1)
        self.label_rozegrane_mecze = QtGui.QLabel(self.groupBox_3)
        self.label_rozegrane_mecze.setText(_fromUtf8(""))
        self.label_rozegrane_mecze.setObjectName(_fromUtf8("label_rozegrane_mecze"))
        self.gridLayout.addWidget(self.label_rozegrane_mecze, 2, 1, 1, 1)
        self.label_zdobyte_punkty_zawodnik = QtGui.QLabel(self.groupBox_3)
        self.label_zdobyte_punkty_zawodnik.setText(_fromUtf8(""))
        self.label_zdobyte_punkty_zawodnik.setObjectName(_fromUtf8("label_zdobyte_punkty_zawodnik"))
        self.gridLayout.addWidget(self.label_zdobyte_punkty_zawodnik, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 6, 0, 1, 2)
        self.listWidget.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_liczba_wygranych.raise_()
        self.label_5.raise_()
        self.label_liczba_przegranych.raise_()
        self.label_6.raise_()
        self.label_zdobyte_punkty.raise_()
        self.label_7.raise_()
        self.label_stracone_punkty.raise_()
        self.groupBox_3.raise_()
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(oknoDruzynyForm)
        QtCore.QMetaObject.connectSlotsByName(oknoDruzynyForm)

    def retranslateUi(self, oknoDruzynyForm):
        oknoDruzynyForm.setWindowTitle(_translate("oknoDruzynyForm", "Okno drużyny", None))
        self.groupBox.setTitle(_translate("oknoDruzynyForm", "Przypisz drużynę", None))
        self.pushButton.setText(_translate("oknoDruzynyForm", "OK", None))
        self.groupBox_2.setTitle(_translate("oknoDruzynyForm", "Dane drużyny", None))
        self.label.setText(_translate("oknoDruzynyForm", "Nazwa drużyny:", None))
        self.label_2.setText(_translate("oknoDruzynyForm", "...", None))
        self.label_4.setText(_translate("oknoDruzynyForm", "Liczba wygranych:", None))
        self.label_liczba_wygranych.setText(_translate("oknoDruzynyForm", "wygrane", None))
        self.label_5.setText(_translate("oknoDruzynyForm", "Liczba przegranych:", None))
        self.label_liczba_przegranych.setText(_translate("oknoDruzynyForm", "przegrane", None))
        self.label_6.setText(_translate("oknoDruzynyForm", "Zdobyte punkty:", None))
        self.label_zdobyte_punkty.setText(_translate("oknoDruzynyForm", "zdobyte_punkty", None))
        self.label_7.setText(_translate("oknoDruzynyForm", "Stracone punkty:", None))
        self.label_stracone_punkty.setText(_translate("oknoDruzynyForm", "stracone_punkty", None))
        self.label_3.setText(_translate("oknoDruzynyForm", "Lista zawodników:", None))
        self.groupBox_3.setTitle(_translate("oknoDruzynyForm", "Statystyki zawodnika:", None))
        self.label_8.setText(_translate("oknoDruzynyForm", "Zdobyte punkty:", None))
        self.label_9.setText(_translate("oknoDruzynyForm", "Stracone punkty:", None))
        self.label_10.setText(_translate("oknoDruzynyForm", "Rozegrane mecze:", None))

