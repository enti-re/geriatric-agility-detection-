import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
# from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from test import *
# from gui2 import *

text=' '
x=0
class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        # self.layout.addWidget(self.label)
        # self.setLayout(layout)
        self.adjustSize()
        label = QLabel("Geriatric Agility Detection", self)
        self.setWindowTitle("My Own Title")
        self.setLayout(self.layout)
        print("pokemon")

# def show_new_window():
#         # app = QApplication(sys.argv)
#         w = AnotherWindow()
#         w.resize(700,450)
#         w.setFixedSize(700, 450)
#         w.show()
#         print("hill2")   
        

class MainWindow(QWidget):

    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.popup = AnotherWindow()
        self.popup.resize(700,450)
        self.popup.setFixedSize(700, 450)
        self.layout = QVBoxLayout()
        label = QLabel("Geriatric Agility Detection", self)
        label.setStyleSheet("color: #CFD8DC")
        label.move(105,105)

        label.setFont(QFont('Fredoka One', 29))
        self.setStyleSheet("""
        background-color: #5D6D7E;
        
        """)
        label.adjustSize()

        self.setWindowTitle("My Own Title")
        self.setLayout(self.layout)

        self.Button1()
        self.Button2()
        self.Button3()
        # self.ui()
    def getText(self):
        global text
        text, okPressed = QInputDialog.getText(self, "Get text","Your gender and age: \n eg:f24", QLineEdit.Normal, "")
        if okPressed and text != '':
            register_Background()
            
            self.popup.show()
            # def board():
            #     self.popup.show()
           
        # print("hill")
    

           
           


        
    # def ui(self)
    #     self.radioButton_male = QtWidgets.QRadioButton(self.centralwidget) 
    #     self.radioButton_female = QtWidgets.QRadioButton(self.centralwidget)

    #  def maleselected(self, selected): 
    #     if selected: 
    #         self.label.setText("You are male") 
              
    # def femaleselected(self, selected): 
    #     if selected: 
    #         self.label.setText("You are female")  

    def Button1(self): 

        button = QPushButton("Start", self)
        button.move(290,185)
        button.setFont(QFont("Fredoka One",13.5))
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        left: 100px;
        """)
        button.clicked.connect(self.getText)


    def Button2(self): 

        button = QPushButton("Guide", self) 
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,240)
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        

        button.clicked.connect(self.clickme)

    def Button3(self): 

        button = QPushButton("Exit", self) 
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,295)
        button.setStyleSheet("""
        background-color: #E57373;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        

        button.clicked.connect(self.clickme) 

    def clickme(self): 
        # printing pressed 
        print("pressed")

    def registerBackground(self): 
        # printing pressed 
        print("pressed")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(700,450)
    mw.setFixedSize(700, 450)
    mw.show()
    sys.exit(app.exec_())