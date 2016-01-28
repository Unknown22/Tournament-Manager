# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nastepny_mecz.ui'
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

class Ui_nastepnyMeczForm(object):
    def setupUi(self, nastepnyMeczForm):
        nastepnyMeczForm.setObjectName(_fromUtf8("nastepnyMeczForm"))
        nastepnyMeczForm.resize(290, 95)
        self.gridLayout = QtGui.QGridLayout(nastepnyMeczForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(nastepnyMeczForm)
        self.lineEdit.setMaximumSize(QtCore.QSize(54, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(nastepnyMeczForm)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(54, 16777215))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(nastepnyMeczForm)
        self.label_4.setMaximumSize(QtCore.QSize(5, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(nastepnyMeczForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(nastepnyMeczForm)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 3)
        self.label = QtGui.QLabel(nastepnyMeczForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(nastepnyMeczForm)
        QtCore.QMetaObject.connectSlotsByName(nastepnyMeczForm)

    def retranslateUi(self, nastepnyMeczForm):
        nastepnyMeczForm.setWindowTitle(_translate("nastepnyMeczForm", "Następny mecz", None))
        self.label_4.setText(_translate("nastepnyMeczForm", ":", None))
        self.label_2.setText(_translate("nastepnyMeczForm", "Team2", None))
        self.pushButton.setText(_translate("nastepnyMeczForm", "OK", None))
        self.label.setText(_translate("nastepnyMeczForm", "Team1", None))

