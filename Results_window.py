from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QSpinBox)

from instr import *
from main import *

class ResultWindow(QWidget):
    def __init__(self, winningNumber, result, gameWindow):
        super().__init__()

        self.winningNumber = winningNumber
        self.result = result
        self.gameWindow = gameWindow

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
        self.lbl_win_num_title =  QLabel("Winning Number:")
        self.lbl_win_num = QLabel(str(self.winningNumber))
        self.lbl_result = QLabel(self.result)
        self.btn_replay = QPushButton("Replay?")
        self.btn_quit = QPushButton("Quit")

        self.layout_line = QVBoxLayout()
        self.layout_line.setContentsMargins(0,0,0,0)
        self.layout_line.setSpacing(50)
        self.win_h_line = QHBoxLayout()
        self.win_h_line.setContentsMargins(0,0,0,0)
        self.win_h_line.setSpacing(10)
        self.win_h_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_h_line = QHBoxLayout()


        self.win_h_line.addWidget(self.lbl_win_num_title, alignment= Qt.AlignmentFlag.AlignCenter)
        self.win_h_line.addWidget(self.lbl_win_num, alignment= Qt.AlignmentFlag.AlignLeft)

        self.btn_h_line.addWidget(self.btn_replay)
        self.btn_h_line.addWidget(self.btn_quit)

        self.layout_line.addLayout(self.win_h_line)
        self.layout_line.addWidget(self.lbl_result, alignment= Qt.AlignmentFlag.AlignCenter)
        self.layout_line.addLayout(self.btn_h_line)
        self.layout_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout_line)

    # conntects buttons to functions
    def connects(self):
        self.btn_quit.clicked.connect(self.quit_click)
        self.btn_replay.clicked.connect(self.replay_click)

    #replays the game
    def replay_click(self):
       self.gameWindow.replay()
       self.hide()
    
    #closes the application
    def quit_click(self):
        app.exit()

    #setups window appearance
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
