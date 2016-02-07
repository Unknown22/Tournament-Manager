# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'druzyny.ui'
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

class Ui_druzynyForm(object):
    def setupUi(self, druzynyForm):
        druzynyForm.setObjectName(_fromUtf8("druzynyForm"))
        druzynyForm.resize(367, 218)
        self.gridLayout = QtGui.QGridLayout(druzynyForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_usun = QtGui.QPushButton(druzynyForm)
        self.pushButton_usun.setObjectName(_fromUtf8("pushButton_usun"))
        self.gridLayout.addWidget(self.pushButton_usun, 7, 0, 1, 1)
        self.label = QtGui.QLabel(druzynyForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.listWidget = QtGui.QListWidget(druzynyForm)
        self.listWidget.setMinimumSize(QtCore.QSize(175, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 7, 1)
        self.lineEdit = QtGui.QLineEdit(druzynyForm)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(druzynyForm)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.pushButton_dodaj = QtGui.QPushButton(druzynyForm)
        self.pushButton_dodaj.setObjectName(_fromUtf8("pushButton_dodaj"))
        self.gridLayout.addWidget(self.pushButton_dodaj, 4, 1, 1, 2)
        self.pushButton_losuj_drzewko = QtGui.QPushButton(druzynyForm)
        self.pushButton_losuj_drzewko.setObjectName(_fromUtf8("pushButton_losuj_drzewko"))
        self.gridLayout.addWidget(self.pushButton_losuj_drzewko, 6, 1, 1, 2)
        self.label_2 = QtGui.QLabel(druzynyForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(druzynyForm)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.pushButton_logo = QtGui.QPushButton(druzynyForm)
        self.pushButton_logo.setObjectName(_fromUtf8("pushButton_logo"))
        self.gridLayout.addWidget(self.pushButton_logo, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(druzynyForm)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 2)

        self.retranslateUi(druzynyForm)
        QtCore.QMetaObject.connectSlotsByName(druzynyForm)

    def retranslateUi(self, druzynyForm):
        druzynyForm.setWindowTitle(_translate("druzynyForm", "Drużyny", None))
        self.pushButton_usun.setText(_translate("druzynyForm", "Usuń", None))
        self.label.setText(_translate("druzynyForm", "Nazwa drużyny:", None))
        self.pushButton_dodaj.setText(_translate("druzynyForm", "Dodaj", None))
        self.pushButton_losuj_drzewko.setText(_translate("druzynyForm", "Losuj drzewko", None))
        self.label_2.setText(_translate("druzynyForm", "Ilość zawodników:", None))
        self.label_3.setText(_translate("druzynyForm", "Logo:", None))
        self.pushButton_logo.setText(_translate("druzynyForm", "...", None))
        self.label_4.setText(_translate("druzynyForm", "...", None))

