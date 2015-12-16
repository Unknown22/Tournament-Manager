# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nowy_turniej.ui'
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

class Ui_nowyTurniejForm(object):
    def setupUi(self, nowyTurniejForm):
        nowyTurniejForm.setObjectName(_fromUtf8("nowyTurniejForm"))
        nowyTurniejForm.setEnabled(True)
        nowyTurniejForm.resize(242, 73)
        nowyTurniejForm.setMinimumSize(QtCore.QSize(242, 73))
        nowyTurniejForm.setMaximumSize(QtCore.QSize(242, 73))
        self.gridLayout = QtGui.QGridLayout(nowyTurniejForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtGui.QLabel(nowyTurniejForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(nowyTurniejForm)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(nowyTurniejForm)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.retranslateUi(nowyTurniejForm)
        QtCore.QMetaObject.connectSlotsByName(nowyTurniejForm)

    def retranslateUi(self, nowyTurniejForm):
        nowyTurniejForm.setWindowTitle(_translate("nowyTurniejForm", "Nowy turniej", None))
        self.label.setText(_translate("nowyTurniejForm", "Podaj liczbę drużyn:", None))
        self.pushButton.setText(_translate("nowyTurniejForm", "Zatwierdź", None))

