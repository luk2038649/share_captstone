from PyQt5.QtWidgets import * #boi thats alotta widgets.
from PyQt5.QtGui import *



class ViewClass(QMainWindow):
    """This class controls the view!"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lukes Great Example!!!")
        self.generalLayout = QHBoxLayout() # split left to right
        #self.generalLayout.addChildLayout(QVBoxLayout())  # left panel for our menu
        self._centralWidget = QWidget(self) # make our magic central widget?
        self.setCentralWidget(self._centralWidget) # add central widget
        self._centralWidget.setLayout(self.generalLayout) # add our main layour to our magic widget
        
        
        self.resize(600,300)
        self.createLeftMenu()
        self.createSpecial()
        self.createRightArea()
        #do view things

    def createSpecial(self):
        self._lblx = DataLabel(val=23)
        self._lblx.setText("Special")
        self.generalLayout.addWidget(self._lblx) # not a button, uh oh

    def createLeftMenu(self): # will create a VBoxLayout of button widgets
        buttonsLayout = QVBoxLayout()
        numberInputLabel = QLabel()
        numberInputLabel.setText("Enter a number for your button!")
        self.numberInput = QLineEdit()
        self.buttons = [ #buttons ?
            QPushButton("Add two"),
            QPushButton("Times two"),
            QPushButton("Subtract two"),
            QPushButton("Show Value of Special Label")
        ]
        for btn in self.buttons:
            buttonsLayout.addWidget(btn) # add all buttons from list
            #btn.clicked.connect(self.garb)
        buttonsLayout.addWidget(numberInputLabel)
        buttonsLayout.addWidget(self.numberInput)
        ##Add a special Label###
        self.generalLayout.addLayout(buttonsLayout)

    def getNumberText(self): # return the current number (AS STR)
        return self.numberInput.text()
    def garb(self):
        print("THIS BETTER NOT WORK LUKE")
    
    def createRightArea(self):
        self.generalLayout.addStretch(1) #IDK about all this?
        self.outText = QLineEdit()
        self.outText.setReadOnly(True)
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(Color('red'))
        rightLayout.addWidget(Color('green'))
        rightLayout.addWidget(Color('purple'))
        rightLayout.addWidget(self.outText)
        self.generalLayout.addLayout(rightLayout)
class Color(QWidget): # I ripped this off for quick colors 

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window , QColor(color))
        self.setPalette(palette)
class DataLabel(QLabel): # we are going to subclass a widget to add data to it
    def __init__(self , val):
        super().__init__()
        self._myVal = val;
        #try and add a subclass with a data slot
    

