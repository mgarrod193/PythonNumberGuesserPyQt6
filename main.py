from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Number Guesser")

        button = QPushButton("Press Me!")

        self.setCentralWidget(button)
#creates and shows window
window = MainWindow()
window.show()

#runs loop
app.exec()