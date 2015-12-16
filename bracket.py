from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtGui import *

class Bracket(object):

    def init_bracket(self, ui, team_number):
        self.team_number = team_number
        self.ui = ui

        self.number_of_groupbox = 0
        self.list_of_groupbox = []
        self.list_of_layouts_in_groupbox = []
        self.list_of_teams_in_groupbox = []
        self.list_of_buttons = []

        if team_number != 0:
            result = team_number
            self.list_of_teams_in_groupbox.append(result)
            while (result != 1):
                if team_number % 2 != 0:
                    team_number = team_number + 1
                self.number_of_groupbox += 1
                result = team_number / 2
                self.list_of_teams_in_groupbox.append(result)
                team_number = result
            self.number_of_groupbox += 1

        for x in range(self.number_of_groupbox):
            groupBox = QGroupBox()
            layout = QtGui.QGridLayout()
            self.list_of_layouts_in_groupbox.append(layout)
            groupBox.setLayout(layout)
            self.list_of_groupbox.append(groupBox)
            ui.ui.gridLayout_2.addWidget(groupBox, 0, x)
            

        self.add_teams_button()

    def add_teams_button(self):
        for number_of_groupbox in range(self.number_of_groupbox):
            for team_number in range(self.list_of_teams_in_groupbox[number_of_groupbox]):
                button = QPushButton("...")
                self.list_of_layouts_in_groupbox[number_of_groupbox].addWidget(button, team_number, 0)
