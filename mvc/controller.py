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
class ControllerClass:
    def __init__(self, model , view):
        self._model = model
        self._view = view
        self._connectSignals() #Wire up the STUFFS


    def _handleTimesTwo(self):
        #Theres definitely no error handling here lol
        text = self._view.getNumberText() # get the current text in box
        #might need to cast to int if we want maths, we will see
        textInt = int(text)
        out = self._model.timesTwo(textInt);
        self._view.outText.setText(out)

    def _handlePlusTwo(self):
        text = self._view.getNumberText()
        textInt = int(text)
        out = self._model.plusTwo(textInt);
        self._view.outText.setText(out)

    def _handleMinusTwo(self):
        text = self._view.getNumberText()
        textInt = int(text)
        out = self._model.minusTwo(textInt);
        self._view.outText.setText(out)
    def _setSpecial(self , newVal):
        self._view._lblx._myVal = newVal # set the data attribute

    def _printSpecial(self):
        out = self._view._lblx._myVal
        print(f"The Value of Special Label ==> {out}")

    def _connectSignals(self):
        """connect all our buttons"""
        ### Connect the buttons to our math functions
        self._view.buttons[1].clicked.connect(self._handleTimesTwo)     
        self._view.buttons[0].clicked.connect(self._handlePlusTwo)     
        self._view.buttons[2].clicked.connect(self._handleMinusTwo)
        ###Connect special data set function
        self._view.buttons[1].clicked.connect(lambda : self._setSpecial(111))     
        self._view.buttons[0].clicked.connect(lambda: self._setSpecial(222))     
        self._view.buttons[2].clicked.connect(lambda: self._setSpecial(333))
        #Connect our Show Special Button
        self._view.buttons[3].clicked.connect(self._printSpecial)

        print("End connecting signals")
    # def garb2(self):
    #     print("THIS BETTER WORK!!!!")