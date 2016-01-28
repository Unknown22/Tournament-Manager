from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *

from ui_files import Ui_BracketWidget, Ui_nowyTurniejForm, Ui_druzynyForm, Ui_ustawieniaForm, \
    Ui_oknoDruzynyForm, Ui_zawodnicyForm, Ui_nastepnyMeczForm, Ui_wczytajZBazyForm, Ui_najlepsiForm

class BracketWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(BracketWidget, self).__init__(*args)
        self.ui = Ui_BracketWidget()
        self.ui.setupUi(self)

class NowyTurniejWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(NowyTurniejWidget, self).__init__(*args)
        self.ui = Ui_nowyTurniejForm()
        self.ui.setupUi(self)

class UstawieniaWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(UstawieniaWidget, self).__init__(*args)
        self.ui = Ui_ustawieniaForm()
        self.ui.setupUi(self)

class DruzynyWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(DruzynyWidget, self).__init__(*args)
        self.ui = Ui_druzynyForm()
        self.ui.setupUi(self)

class OknoDruzyny(QtGui.QWidget):
    def __init__(self, *args):
        super(OknoDruzyny, self).__init__(*args)
        self.ui = Ui_oknoDruzynyForm()
        self.ui.setupUi(self)

class ZawodnicyWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(ZawodnicyWidget, self).__init__(*args)
        self.ui = Ui_zawodnicyForm()
        self.ui.setupUi(self)

class NastepnyMeczWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(NastepnyMeczWidget, self).__init__(*args)
        self.ui = Ui_nastepnyMeczForm()
        self.ui.setupUi(self)

class WczytajZBazyWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(WczytajZBazyWidget, self).__init__(*args)
        self.ui = Ui_wczytajZBazyForm()
        self.ui.setupUi(self)

class NajlepsiWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(NajlepsiWidget, self).__init__(*args)
        self.ui = Ui_najlepsiForm()
        self.ui.setupUi(self)