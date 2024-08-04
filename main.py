from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Number Guesser")
        self.setFixedSize(QSize(500,500))

        button = QPushButton("Click to play!")

        self.setCentralWidget(button)
#creates and shows window
window = MainWindow()
window.show()

#runs loop
app.exec()