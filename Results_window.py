from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from random import randint
from instr import *



class ResultWindow(QWidget):
    def __init__(self, result):
        super().__init__()

        self.result = result

        #window which contains introduction
        self.initUI()

        #establishes connections between elements
        self.connects()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start:
        self.show()

    def initUI(self):
        pass

    def connects(self):
        pass

    def set_appear(self):
        pass