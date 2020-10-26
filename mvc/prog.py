#! /usr/bin/env python3
import sys
from PyQt5.QtWidgets import *

from view import ViewClass # it doesnt like this but it works idk
from model import ModelClass
from controller import ControllerClass

def main():
    """Main Function"""
    program = QApplication(sys.argv)
    view = ViewClass() # make our view
    view.show() # dispaly our view
    model = ModelClass() # get model instance
    controller = ControllerClass(model=model , view=view)
    sys.exit(program.exec())

if __name__ == '__main__':
    main()