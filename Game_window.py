from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QIntValidator, QPixmap
from PyQt6.QtWidgets import (QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

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

    #creates Labels and buttons, adds them to layout and sets layout
    def initUI(self):
        # Load the background image
        background_image = QPixmap('test.png')  # Path to your image file

        # Set the palette
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)
        
        self.lbl_lives = QLabel("Lives: 3", alignment= Qt.AlignmentFlag.AlignTop)
        self.lbl_guess= QLabel(txt_guess)
        self.lbl_result=QLabel("")
        self.line_guess = QLineEdit()
        self.line_guess.setValidator(QIntValidator())
        self.line_guess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_guess = QPushButton(txt_btnguess)

        self.layout_line = QVBoxLayout()
        self.layout_line.setContentsMargins(0,0,0,0)
        self.layout_line.setSpacing(50)
        self.layout_line.addWidget(self.lbl_lives, alignment= Qt.AlignmentFlag.AlignTop)
        self.layout_line.addWidget(self.lbl_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.line_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.lbl_result, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addWidget(self.btn_guess, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_line)

    #called when guess button clicked, checks guessed number against the winning number and provides a hint to player
    def guess_click(self):
        try:
            float(self.line_guess.text())
        except:
            self.lbl_result.setText("Error: No number inputted.")
            return
        guessNumber = float(self.line_guess.text())
        if guessNumber == self.winningNumber:
            self.ResultWindow = ResultWindow(self.winningNumber, "You Win!", self)
            self.hide()
            self.lbl_result.setText("You Win!")
        elif guessNumber > self.winningNumber:
            self.lbl_result.setText("Lower")
        else:
            self.lbl_result.setText('Higher')
        self.lives -= 1    

        lives_string = "Lives: " + str(self.lives)
        self.lbl_lives.setText(lives_string)
        #if player loses all 3 lives displays result window of "you lose!"
        if self.lives == 0:
            #display results screen
            self.ResultWindow = ResultWindow(self.winningNumber, "you Lose!", self)
            self.hide()

    #connects buttons to functions
    def connects(self):
        self.btn_guess.clicked.connect(self.guess_click)

    #setup window appearance
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)


    def replay(self):
        self.winningNumber = randint(0, 10)
        self.lives = 3
        self.lbl_result.setText("")
        self.show()