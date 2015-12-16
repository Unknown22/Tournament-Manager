from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *

class Save(QWidget):

    def take_screenshot(self, ui):
        filename = QFileDialog.getSaveFileName(self, 'Zapisz drzewo turniejowe', 'tournament', selectedFilter='*.png')
        p = QPixmap.grabWidget(ui.scrollAreaWidgetContents)
        p.save(filename, 'png')