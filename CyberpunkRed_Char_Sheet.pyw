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
        MAX_STAT_VALUE = 10 

        # Member variables for making working with the UI easier
        # Avoids having to type self.ui every time
        #
        #
        char_handle_input = self.ui.HandleInput
        char_role = self.ui.RoleSelect
        char_role_ability = self.ui.RoleAbilityDisplay
        role_ability_rank = self.ui.RoleAbilityRankInput
        intelligence_input = self.ui.IntelligenceInput
        reflex_input = self.ui.ReflexInput
        dexterity_input = self.ui.DexterityInput
        tech_input = self.ui.TechInput
        cool_input = self.ui.CoolInput
        will_input = self.ui.WillInput
        move_input = self.ui.MoveInput
        body_input = self.ui.BodyInput
        luck_max = self.ui.LuckMaxInput
        luck_current = self.ui.LuckCurrentInput
        empathy_max = self.ui.EmpathyMaxInput
        empathy_current = self.ui.EmpathyCurrentInput
        humanity_max = self.ui.HumanityMax # QLabel
        humanity_current = self.ui.HumanityCurrent # QLabel

        # Member Functions
        #
        #
        def setMaxHumanity(self):
            if(empathy_max.text() != ''):
                totalHumanity = str(int(empathy_max.text()) * 10)
                humanity_max.setText(totalHumanity)
                humanity_current.setText(totalHumanity)   

        def setMaxEmpathy(self):
            empathy_current.setText(empathy_max.text())

        # Sets the role ability based on the role chosen
        def updateRoleAbility(self):
            char_role_ability.setText(roles.get(char_role.currentText()))

        def reduceHumanity(self, humanity_loss):
            reducedHumanity = int(humanity_current.text()) - int(humanity_loss)
            # to do: check for cyberware, because some of them have a humanity_loss modifier
            # to do: add humanity reduction field & button somewhere to reduce in case of in-game event
        
        def reduceMaxEmpathy(self, humanity_loss):
            # to do: if you're adding cyberware, your humanity drops as well as Empathy
            #           E.g.    empathy_max == 8
            #                   add a Neural Link (7 hl) and Kerenzikov (14 hl), humanity_loss == 21
            #                   humanity_current = humanity_max - humanity_loss
            #                   59 = 80 - 21
            #                   Therefore empathy_current will be 5

        # Connect buttons & fields
        #
        #
        char_role.currentIndexChanged.connect(updateRoleAbility)    
        empathy_max.textChanged.connect(setMaxHumanity)
        empathy_max.textChanged.connect(setMaxEmpathy)

        # Operations on init
        #
        #
        char_role.addItems(roles.keys())
        role_ability_rank.setText("4")
        setMaxHumanity(self)
        setMaxEmpathy(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    char_sheet = CPCharSheet()
    char_sheet.show()
    sys.exit(app.exec_())