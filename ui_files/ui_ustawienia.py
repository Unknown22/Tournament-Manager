# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ustawienia.ui'
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

class Ui_ustawieniaForm(object):
    def setupUi(self, ustawieniaForm):
        ustawieniaForm.setObjectName(_fromUtf8("ustawieniaForm"))
        ustawieniaForm.resize(206, 76)
        self.gridLayout = QtGui.QGridLayout(ustawieniaForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(ustawieniaForm)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(ustawieniaForm)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.retranslateUi(ustawieniaForm)
        QtCore.QMetaObject.connectSlotsByName(ustawieniaForm)

    def retranslateUi(self, ustawieniaForm):
        ustawieniaForm.setWindowTitle(_translate("ustawieniaForm", "Ustawienia", None))
        self.pushButton.setText(_translate("ustawieniaForm", "Drużyny", None))
        self.pushButton_2.setText(_translate("ustawieniaForm", "Zawodnicy", None))

