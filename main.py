from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import QMessageBox
import sys

from ui_files import Ui_MainWindow, Ui_BracketWidget
from bracket import Bracket

class BracketWidget(QtGui.QWidget):
    def __init__(self, *args):
        super(BracketWidget, self).__init__(*args)
        self.ui = Ui_BracketWidget()
        self.ui.setupUi(self)

class TournamentManager(QtGui.QMainWindow):
    def __init__(self, *args):
        super(TournamentManager, self).__init__(*args)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bracket_widget = BracketWidget()
        self.ui.horizontalLayout_2.addWidget(self.bracket_widget)

        self.init_vars()

        self.bracket = Bracket()
        self.create_bracket()

    def init_vars(self):
        self.number_of_teams = 16

        
    def create_bracket(self):
        ui = self.bracket_widget
        self.bracket.init_bracket(ui, self.number_of_teams)

def main():
    app = QtGui.QApplication(sys.argv)
    tournament_manager = TournamentManager()
    tournament_manager.show()
    app.exec_()

if __name__ == '__main__':
    main()