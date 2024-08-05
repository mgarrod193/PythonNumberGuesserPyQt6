from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

from instr import *
from Game_window import *


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        #window which contains introduction
        self.initUI()

        #establishes connections between elements
        self.connects()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # start:
        self.show()

    def initUI(self):
        #creates graphical elements
        self.btn_next = QPushButton(txt_next, self)
        self.lbl_greet = QLabel(txt_hello)
        self.lbl_instr = QLabel(txt_instruction)
        self.lbl_instr.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #creates layout and adds widgets to layout
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.lbl_greet, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout_line.addWidget(self.lbl_instr, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout_line)

    #called when play button is clicked
    def play_click(self):
        self.gameWindow = GameWindow()
        self.close()

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
if __name__ == "__main__":
    app.exec()