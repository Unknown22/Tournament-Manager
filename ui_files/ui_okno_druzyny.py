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
        oknoDruzynyForm.resize(342, 211)
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
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.listWidget.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
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
        self.label_3.setText(_translate("oknoDruzynyForm", "Lista zawodników:", None))

