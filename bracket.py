from PyQt4.QtGui import QGroupBox

class Bracket(object):

    def init_bracket(self, ui, team_number):

        result = 0
        number_of_groupbox = 0

        if team_number != 0:
            while (result != 1):
                if team_number % 2 != 0:
                    team_number = team_number + 1
                number_of_groupbox += 1
                print number_of_groupbox
                result = team_number / 2
                team_number = result
                print result

        for x in range(number_of_groupbox):
            groupBox = QGroupBox()
            ui.horizontalLayout.addWidget(groupBox)