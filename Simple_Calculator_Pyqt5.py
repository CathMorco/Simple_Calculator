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

    def initUI(self):
        # Create QLabel for the operation selection
        self.operationLabel = QLabel('Choose an operation:')
        self.operationLabel.setAlignment(Qt.AlignCenter)

        # Create QPushButton for addition operation
        self.addButton = QPushButton('+')

        # Create QPushButton for subtraction operation
        self.subButton = QPushButton('-')

        # Create QPushButton for multiplication operation
        self.mulButton = QPushButton('*')

        # Create QPushButton for division operation
        self.divButton = QPushButton('/')

        # Create QLabel and QLineEdit for the first number input
        self.num1Label = QLabel('Enter the first number:')
        self.num1Label.setAlignment(Qt.AlignCenter)
        self.num1LineEdit = QLineEdit()

        # Create QLabel and QLineEdit for the second number input
        self.num2Label = QLabel('Enter the second number:')
        self.num2Label.setAlignment(Qt.AlignCenter)
        self.num2LineEdit = QLineEdit()

        # Create QPushButton for calculating the result
        self.calculateButton = QPushButton('Calculate')

        # Create QLabel for displaying the result
        self.resultLabel = QLabel()

        # Create QVBoxLayout and add widgets to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.operationLabel)
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.subButton)
        vbox.addWidget(self.mulButton)
        vbox.addWidget(self.divButton)
        vbox.addWidget(self.num1Label)
        vbox.addWidget(self.num1LineEdit)
        vbox.addWidget(self.num2Label)
        vbox.addWidget(self.num2LineEdit)
        vbox.addWidget(self.calculateButton)
        vbox.addWidget(self.resultLabel)

        # Set layout for the window
        self.setLayout(vbox)

        # Connect signals and slots
        self.addButton.clicked.connect(lambda: self.setOperation(1))
        self.subButton.clicked.connect(lambda: self.setOperation(2))
        self.mulButton.clicked.connect(lambda: self.setOperation(3))
        self.divButton.clicked.connect(lambda: self.setOperation(4))
        self.calculateButton.clicked.connect(self.calculateResult)

        self.screenDisplay = QLabel(self)

        self.screenDisplay.setGeometry(5, 5, 480, 50)

        self.screenDisplay.setWordWrap(True)

        self.screenDisplay.setAlignment(Qt.AlignRight)

        self.screenDisplay.setFont(QFont('Times', 20))
        self.screenDisplay.setStyleSheet("QLabel"
                                 "{"
                                 "border : 1px solid grey;"
                                 "background : grey;"
                                 "}")
# Set window properties
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 500, 400)
        self.show()
#Create a function for the selected operation
    def setOperation(self, operation):
        self.operation = operation
#create function for calculate button
    def calculateResult(self):
        # Get user inputs from QLineEdits
        num1 = self.num1LineEdit.text()
        num2 = self.num2LineEdit.text()

        #If input is not float, displays error message and clears initial input
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Value Error', 'Invalid Input, Please Input Numbers Only', QMessageBox.Ok)
        
#if operator is not selected, prompts user to choose an operator
        if not hasattr(self, 'operation'):
            return QMessageBox.information(self, 'Operation Error', 'Please choose an operation', QMessageBox.Ok)
# Calculate result based on selected operation
        #For addition
        if self.operation == 1:
            result = num1 + num2
        #For subtraction
        elif self.operation == 2:
            result = num1 - num2
        #For multiplication
        elif self.operation == 3:
            result = num1 * num2
        #for division
        elif self.operation == 4:
            try:
                #Does not allow zero division
                result = num1 / num2
                self.resultLabel.setText('Zero Division not allowed')
            except ZeroDivisionError:
                #clears initial input and displays error message
                self.num2LineEdit.clear()
                return QMessageBox.information(self, 'Syntax Error', 'Zero Division not allowed', QMessageBox.Ok)

# Display result
        self.screenDisplay.setText(str(result))
#Asks user if they want to try again
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Do you want to try again?")
        messageBox.setWindowTitle("Confirmation")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        response = messageBox.exec_()
        #If yes, repeats process
        if response == QMessageBox.Yes:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
        #If no, displays thank you message and closes program
        else:
            Tymsg = QMessageBox()
            Tymsg.setWindowTitle("Message")
            Tymsg.setText("Thank you!")
            x = Tymsg.exec_()
            sys.exit(app.exec_())
#runs the main program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Calculator()
    sys.exit(app.exec_())