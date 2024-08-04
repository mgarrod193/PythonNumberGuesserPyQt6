from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from random import randint
from instr import *

lives = 3

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.winningNumber = randint(0,10)

        #window which contains introduction
        self.initUI()

        #establishes connections between elements
        self.connects()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start:
        self.show()


    def initUI(self):
        
        self.lbl_guess= QLabel(txt_guess)
        self.lbl_result=QLabel("")
        self.line_guess = QLineEdit()
        self.line_guess.setValidator(QIntValidator())
        self.btn_guess = QPushButton(txt_btnguess)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.lbl_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.line_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.lbl_result, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.btn_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_line)

    def guess_click(self):
        print(self.btn_guess.text())
        guessNumber = float(self.btn_guess.text())
        if guessNumber == self.winningNumber:
            self.lbl_result.setText("You Win!")
        elif guessNumber > self.winningNumber:
            self.lbl_result.setText("Lower")
            lives -= 1
            print(lives)
        else:
            lives -= 1
            print(lives)
            self.lbl_result.setText('Higher')

    def connects(self):
        self.btn_guess.clicked.connect(self.guess_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

#When player is dead show lose screen
if lives == 0:
    pass
