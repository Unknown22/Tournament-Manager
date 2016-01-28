# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'najlepsi.ui'
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

class Ui_najlepsiForm(object):
    def setupUi(self, najlepsiForm):
        najlepsiForm.setObjectName(_fromUtf8("najlepsiForm"))
        najlepsiForm.resize(367, 86)
        self.gridLayout = QtGui.QGridLayout(najlepsiForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(najlepsiForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_10 = QtGui.QLabel(najlepsiForm)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(najlepsiForm)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(najlepsiForm)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(najlepsiForm)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(najlepsiForm)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(najlepsiForm)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(najlepsiForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(najlepsiForm)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.retranslateUi(najlepsiForm)
        QtCore.QMetaObject.connectSlotsByName(najlepsiForm)

    def retranslateUi(self, najlepsiForm):
        najlepsiForm.setWindowTitle(_translate("najlepsiForm", "Najlepsi", None))
        self.label.setText(_translate("najlepsiForm", "Najwięcej zdobytych punktów:", None))
        self.label_10.setText(_translate("najlepsiForm", "Najwięcej wygranych:", None))
        self.label_11.setText(_translate("najlepsiForm", "TextLabel", None))
        self.label_12.setText(_translate("najlepsiForm", "TextLabel", None))
        self.label_7.setText(_translate("najlepsiForm", "TextLabel", None))
        self.label_4.setText(_translate("najlepsiForm", "TextLabel", None))
        self.label_5.setText(_translate("najlepsiForm", "TextLabel", None))
        self.label_2.setText(_translate("najlepsiForm", "Najwięcej straconych punktów:", None))
        self.label_6.setText(_translate("najlepsiForm", "TextLabel", None))

