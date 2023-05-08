#Imports necessary elements
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#creates class for widgets
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
#creates function for GUI
# Set window properties
#Create a function for the selected operation
#create function for calculate button
# Get user inputs from QLineEdits
#If input is not float, displays error message and clears initial input
#if operator is not selected, prompts user to choose an operator
# Calculate result based on selected operation
# Display result
#Asks user if they want to try again
#If yes, repeats process
#If no, displays thank you message and closes program
#runs the main program