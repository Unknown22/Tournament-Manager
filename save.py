from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *

class Save(object):

    @staticmethod
    def take_screenshot(ui):
        filename = 'Screenshot.png'
        p = QPixmap.grabWidget(ui.scrollAreaWidgetContents)
        p.save(filename, 'png')