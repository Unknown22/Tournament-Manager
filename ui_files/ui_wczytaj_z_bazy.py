# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wczytaj_z_bazy.ui'
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

class Ui_wczytajZBazyForm(object):
    def setupUi(self, wczytajZBazyForm):
        wczytajZBazyForm.setObjectName(_fromUtf8("wczytajZBazyForm"))
        wczytajZBazyForm.resize(253, 256)
        self.gridLayout = QtGui.QGridLayout(wczytajZBazyForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(wczytajZBazyForm)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 7, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_3.addWidget(self.lineEdit_6, 7, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_3.addWidget(self.lineEdit_7, 8, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 9, 0, 1, 2)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_3.addWidget(self.lineEdit_5, 5, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.retranslateUi(wczytajZBazyForm)
        QtCore.QMetaObject.connectSlotsByName(wczytajZBazyForm)

    def retranslateUi(self, wczytajZBazyForm):
        wczytajZBazyForm.setWindowTitle(_translate("wczytajZBazyForm", "Wczytaj z bazy", None))
        self.groupBox_3.setTitle(_translate("wczytajZBazyForm", "Baza MySQL", None))
        self.label_3.setText(_translate("wczytajZBazyForm", "Hasło:", None))
        self.label_2.setText(_translate("wczytajZBazyForm", "Nick:", None))
        self.pushButton.setText(_translate("wczytajZBazyForm", "Wczytaj", None))
        self.label_4.setText(_translate("wczytajZBazyForm", "Adres:", None))
        self.label_5.setText(_translate("wczytajZBazyForm", "Nazwa użytkownika:", None))
        self.label_6.setText(_translate("wczytajZBazyForm", "Hasło:", None))
        self.label_7.setText(_translate("wczytajZBazyForm", "Nazwa bazy:", None))
        self.label.setText(_translate("wczytajZBazyForm", "ID Turnieju:", None))

