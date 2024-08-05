from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from random import randint
from instr import *

from Results_window import *

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.winningNumber = randint(0,10)
        self.lives = 3

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
        print(self.line_guess.text())
        guessNumber = float(self.line_guess.text())
        if guessNumber == self.winningNumber:
            self.ResultWindow = ResultWindow(self.winningNumber, True)
            self.hide()
            self.lbl_result.setText("You Win!")
        elif guessNumber > self.winningNumber:
            self.lbl_result.setText("Lower")
            self.lives -= 1
            print(self.lives)
        else:
            self.lives -= 1
            print(self.lives)
            self.lbl_result.setText('Higher')


        if self.lives == 0:
            #display results screen
            self.ResultWindow = ResultWindow(self.winningNumber, True)
            self.hide()

    def connects(self):
        self.btn_guess.clicked.connect(self.guess_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


