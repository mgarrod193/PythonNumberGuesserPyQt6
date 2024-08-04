from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from random import randint
from instr import *



while input("Do you want to play? (no to quit):").lower() != "no":
    winning_number = randint(0, 10)

    player_number = int(input("Guess a number from 1 to 10:"))
    while player_number != winning_number:
        if player_number < winning_number:
            print("try a larger number")
        else:
            print("try a smaller number")
        player_number = int(input("Guess a number from 1 to 10:")) 
    
    print("You Win!")