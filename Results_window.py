from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from random import randint
from instr import *



class ResultWindow(QWidget):
    def __init__(self, winningNumber, result):
        super().__init__()

        self.winningNumber = winningNumber
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
        self.lbl_win_num = QLabel(str(self.winningNumber))
        self.lbl_result = QLabel("")
        self.btn_replay = QPushButton("Replay?")
        self.btn_quit = QPushButton("Quit")

        self.v_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.h_line.addWidget(self.btn_replay)
        self.h_line.addWidget(self.btn_quit)

        self.v_line.addWidget(self.lbl_win_num)
        self.v_line.addWidget(self.lbl_result)
        self.v_line.addWidget(self.h_line)
        self.setLayout(self.v_line)

    def connects(self):
        pass

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
