# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(380, 380)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/cup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUstawienia = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/settings3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUstawienia.setIcon(icon1)
        self.actionUstawienia.setObjectName(_fromUtf8("actionUstawienia"))
        self.actionNowy_turniej = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/newfile.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNowy_turniej.setIcon(icon2)
        self.actionNowy_turniej.setObjectName(_fromUtf8("actionNowy_turniej"))
        self.actionPomoc = QtGui.QAction(MainWindow)
        self.actionPomoc.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPomoc.setIcon(icon3)
        self.actionPomoc.setObjectName(_fromUtf8("actionPomoc"))
        self.actionWczytaj_z_pliku = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWczytaj_z_pliku.setIcon(icon4)
        self.actionWczytaj_z_pliku.setObjectName(_fromUtf8("actionWczytaj_z_pliku"))
        self.actionWczytaj_z_bazy_danych = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWczytaj_z_bazy_danych.setIcon(icon5)
        self.actionWczytaj_z_bazy_danych.setObjectName(_fromUtf8("actionWczytaj_z_bazy_danych"))
        self.actionZapisz_screenshot_drzewa_turniejowego = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/camera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZapisz_screenshot_drzewa_turniejowego.setIcon(icon6)
        self.actionZapisz_screenshot_drzewa_turniejowego.setObjectName(_fromUtf8("actionZapisz_screenshot_drzewa_turniejowego"))
        self.actionZapisz_do_pliku = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/save2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZapisz_do_pliku.setIcon(icon7)
        self.actionZapisz_do_pliku.setObjectName(_fromUtf8("actionZapisz_do_pliku"))
        self.actionZapisz_do_bazy_danych = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/databaseupload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZapisz_do_bazy_danych.setIcon(icon8)
        self.actionZapisz_do_bazy_danych.setObjectName(_fromUtf8("actionZapisz_do_bazy_danych"))
        self.toolBar.addAction(self.actionNowy_turniej)
        self.toolBar.addAction(self.actionWczytaj_z_bazy_danych)
        self.toolBar.addAction(self.actionZapisz_do_bazy_danych)
        self.toolBar.addAction(self.actionWczytaj_z_pliku)
        self.toolBar.addAction(self.actionZapisz_do_pliku)
        self.toolBar.addAction(self.actionZapisz_screenshot_drzewa_turniejowego)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUstawienia)
        self.toolBar.addAction(self.actionPomoc)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tournament Manager", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionUstawienia.setText(_translate("MainWindow", "Ustawienia", None))
        self.actionNowy_turniej.setText(_translate("MainWindow", "Nowy turniej", None))
        self.actionPomoc.setText(_translate("MainWindow", "Pomoc", None))
        self.actionWczytaj_z_pliku.setText(_translate("MainWindow", "Wczytaj z pliku", None))
        self.actionWczytaj_z_bazy_danych.setText(_translate("MainWindow", "Wczytaj z bazy danych", None))
        self.actionZapisz_screenshot_drzewa_turniejowego.setText(_translate("MainWindow", "Zapisz screenshot drzewa turniejowego", None))
        self.actionZapisz_do_pliku.setText(_translate("MainWindow", "Zapisz do pliku", None))
        self.actionZapisz_do_bazy_danych.setText(_translate("MainWindow", "Zapisz do bazy danych", None))
        self.actionZapisz_do_bazy_danych.setToolTip(_translate("MainWindow", "Zapisz do bazy danych", None))

