from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import QMessageBox
import sys

from ui_files import Ui_MainWindow

class TournamentManager(QtGui.QMainWindow):
    def __init__(self, *args):
        super(TournamentManager, self).__init__(*args)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    tournament_manager = TournamentManager()
    tournament_manager.show()
    app.exec_()

if __name__ == '__main__':
    main()