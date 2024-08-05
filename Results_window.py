from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from instr import *
from Game_window import *

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

    #creates Labels and buttons, adds them to layout and sets layout
    def initUI(self):
        self.lbl_win_num = QLabel(str(self.winningNumber))
        self.lbl_result = QLabel(self.result)
        self.btn_replay = QPushButton("Replay?")
        self.btn_quit = QPushButton("Quit")

        self.v_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.h_line.addWidget(self.btn_replay)
        self.h_line.addWidget(self.btn_quit)

        self.v_line.addWidget(self.lbl_win_num, alignment= Qt.AlignmentFlag.AlignCenter)
        self.v_line.addWidget(self.lbl_result, alignment= Qt.AlignmentFlag.AlignCenter)
        self.v_line.addLayout(self.h_line)
        self.setLayout(self.v_line)

    # conntects buttons to functions
    def connects(self):
        self.btn_quit.clicked.connect(self.quit_click)
        self.btn_replay.clicked.connect(self.replay_click)

    #replays the game
    def replay_click(self):
        self.gameWindow = GameWindow()
        self.hide()

    #closes the application
    def quit_click(self):
        self.close()

    #setups window appearance
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
