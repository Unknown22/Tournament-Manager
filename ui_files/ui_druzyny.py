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
        druzynyForm.resize(385, 194)
        self.gridLayout = QtGui.QGridLayout(druzynyForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(druzynyForm)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 1)
        self.pushButton_usun = QtGui.QPushButton(druzynyForm)
        self.pushButton_usun.setObjectName(_fromUtf8("pushButton_usun"))
        self.gridLayout.addWidget(self.pushButton_usun, 4, 0, 1, 1)
        self.label = QtGui.QLabel(druzynyForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(druzynyForm)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.pushButton_dodaj = QtGui.QPushButton(druzynyForm)
        self.pushButton_dodaj.setObjectName(_fromUtf8("pushButton_dodaj"))
        self.gridLayout.addWidget(self.pushButton_dodaj, 1, 1, 1, 2)

        self.retranslateUi(druzynyForm)
        QtCore.QMetaObject.connectSlotsByName(druzynyForm)

    def retranslateUi(self, druzynyForm):
        druzynyForm.setWindowTitle(_translate("druzynyForm", "Drużyny", None))
        self.pushButton_usun.setText(_translate("druzynyForm", "Usuń", None))
        self.label.setText(_translate("druzynyForm", "Nazwa drużyny:", None))
        self.pushButton_dodaj.setText(_translate("druzynyForm", "Dodaj", None))

