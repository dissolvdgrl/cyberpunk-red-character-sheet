import sys
from cp_char_sheet import *

class CPCharSheet(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        # Setup
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        
        # Member variables
        #
        #        
        roles = {'Rockerboy': 'Charismatic Impact', 'Solo': 'Combat Awareness', 'Netrunner': 'Interface', 'Tech':  'Maker', 'Medtech': 'Medicine', 'Media': 'Credibility', 'Exec': 'Teamwork', 'Lawman': 'Backup', 'Fixer':'Operator', 'Nomad': 'Moto'} 

        # Member variables for making working with the UI easier
        # Avoids having to type self.ui every time
        #
        #
        char_handle_input = self.ui.HandleInput
        char_role = self.ui.RoleSelect
        char_role_ability = self.ui.RoleAbilityDisplay
        role_ability_rank = self.ui.RoleAbilityRankInput

        # Member Functions
        #
        #

        # Sets the role ability based on the role chosen
        def updateRoleAbility(self):
            char_role_ability.setText(roles.get(char_role.currentText()))

        # Connect buttons
        #
        #
        char_role.currentIndexChanged.connect(updateRoleAbility)    

        # Operations on init
        #
        #
        char_role.addItems(roles.keys())
        role_ability_rank.setText("4")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    char_sheet = CPCharSheet()
    char_sheet.show()
    sys.exit(app.exec_())