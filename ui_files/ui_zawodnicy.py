# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zawodnicy.ui'
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

class Ui_zawodnicyForm(object):
    def setupUi(self, zawodnicyForm):
        zawodnicyForm.setObjectName(_fromUtf8("zawodnicyForm"))
        zawodnicyForm.resize(402, 248)
        self.gridLayout = QtGui.QGridLayout(zawodnicyForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(zawodnicyForm)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label = QtGui.QLabel(zawodnicyForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(zawodnicyForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(zawodnicyForm)
        self.listWidget.setMinimumSize(QtCore.QSize(182, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(182, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 7, 1)
        self.lineEdit_2 = QtGui.QLineEdit(zawodnicyForm)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(zawodnicyForm)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(zawodnicyForm)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.pushButton_dodaj = QtGui.QPushButton(zawodnicyForm)
        self.pushButton_dodaj.setObjectName(_fromUtf8("pushButton_dodaj"))
        self.gridLayout.addWidget(self.pushButton_dodaj, 6, 1, 1, 2)
        self.label_4 = QtGui.QLabel(zawodnicyForm)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(zawodnicyForm)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 2)
        self.pushButton_usun = QtGui.QPushButton(zawodnicyForm)
        self.pushButton_usun.setObjectName(_fromUtf8("pushButton_usun"))
        self.gridLayout.addWidget(self.pushButton_usun, 7, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)

        self.retranslateUi(zawodnicyForm)
        QtCore.QMetaObject.connectSlotsByName(zawodnicyForm)

    def retranslateUi(self, zawodnicyForm):
        zawodnicyForm.setWindowTitle(_translate("zawodnicyForm", "Zawodnicy", None))
        self.label.setText(_translate("zawodnicyForm", "Imię:", None))
        self.label_2.setText(_translate("zawodnicyForm", "Nazwisko:", None))
        self.label_3.setText(_translate("zawodnicyForm", "Pozycja:", None))
        self.pushButton_dodaj.setText(_translate("zawodnicyForm", "Dodaj", None))
        self.label_4.setText(_translate("zawodnicyForm", "Drużyna:", None))
        self.pushButton_usun.setText(_translate("zawodnicyForm", "Usuń", None))

