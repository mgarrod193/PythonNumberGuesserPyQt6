from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

from instr import *



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        #window which contains introduction
        self.introduction()

        #establishes connections between elements
        self.connects()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start:
        self.show()

    def introduction(self):
        #creates graphical elements
        self.btn_next = QPushButton(txt_next, self)
        self.lbl_greet = QLabel(txt_hello)
        self.lbl_instr = QLabel(txt_instruction)

        #creates layout and adds widgets to layout
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.lbl_greet, alignment=Qt.center)
        self.layout_line.addWidget(self.lbl_instr, alignment=Qt.center)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.center)
        self.setLayout(self.layout_line)

    #called when play button is clicked
    def play_click(self):
        pass

    #links button to functions
    def connects(self):
        self.btn_next.clicked.connect(self.play_click)

    #sets window's appearance
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])

#creates and shows window
mainWindow = MainWindow()

#runs loop
app.exec()