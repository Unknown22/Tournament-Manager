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
        MainWindow.resize(739, 587)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/cup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(40, 40))
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
        self.actionZapisz = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/save2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZapisz.setIcon(icon3)
        self.actionZapisz.setObjectName(_fromUtf8("actionZapisz"))
        self.actionWczytaj = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWczytaj.setIcon(icon4)
        self.actionWczytaj.setObjectName(_fromUtf8("actionWczytaj"))
        self.actionPomoc = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("ui_files/icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPomoc.setIcon(icon5)
        self.actionPomoc.setObjectName(_fromUtf8("actionPomoc"))
        self.toolBar.addAction(self.actionNowy_turniej)
        self.toolBar.addAction(self.actionWczytaj)
        self.toolBar.addAction(self.actionZapisz)
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
        self.actionZapisz.setText(_translate("MainWindow", "Zapisz", None))
        self.actionWczytaj.setText(_translate("MainWindow", "Wczytaj", None))
        self.actionPomoc.setText(_translate("MainWindow", "Pomoc", None))

