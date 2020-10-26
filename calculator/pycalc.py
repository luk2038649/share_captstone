#! /usr/bin/env python3


"""PyCalc Tutorial Incoming boys!!!!"""

import sys #idk why we need system calls?
from functools import partial
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
ERROR_MSG = 'ERROR'


__version__ = "0.1"
__author__ = "Ledanis Pozo Ramos" # thanks pal!

class PyCalcUi(QMainWindow):
    """Shut up, pylint"""
    def _createDisplay(self):
        """Create the Display"""
        self.display = QLineEdit()
        #Set some displays properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        #Add the display to general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #Buttons text | position on the QgridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),  
        }
        #Create buttons and add them to grid layout
        for btnText , pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText] , pos[0] , pos[1])
        #Add buttonsLAyout to general layout
        self.generalLayout.addLayout(buttonsLayout)
    def setDisplayText(self, text):
        """Set displays text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display"""
        self.setDisplayText('')

    #"""PyCalc View GUI""" #is he using these as comments? IDK
    def __init__(self):
        #View Initializer
        super().__init__()
        #Set main window properties
        self.setWindowTitle("PyCalc!")
        self.setFixedSize(235,235)
        #Set central widget
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        #create the display and the buttons
        self._createDisplay()
        self._createButtons()

#Create a Controller class to connect the GUI and Model
class PyCalcCtrl:
    """PyCalc Controller class."""
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        #connect signals and slots??
        self._connectSignals()
    
    def _calculateResult(self):
        """Evaluate Expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=' , 'C'}:
                btn.clicked.connect(partial(self._buildExpression , btnText))
        
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
    
#our model?
def evaluateExpression(expression):
    """Evaluate an expression"""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result
#Client code
def main():
    """Main Function."""
    #Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    #Show calculator GUI
    view = PyCalcUi()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model , view=view)
    #Execute Calculators Main loop
    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()