# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QDesktopWidget, QMainWindow, QStatusBar, QProgressBar,QLabel
from PySide2.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QGridLayout
from PySide2.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sttting icon")
        self.setGeometry(300, 300, 500, 400)
        self.setIcon()
        # showing a hint, or tooltip
        self.setToolTip("this is window")
        
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    def setIcon(self):
        appIcon = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        self.setWindowIcon(appIcon)
   
    def createLayout(self):
        self.groupBox = QGroupBox("please choose ine languages")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridlayout = QGridLayout()
        
        button = QPushButton("CSS", self)
        button.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button, 0, 0)
        
        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button1, 0, 1)
        
        button2 = QPushButton("Python", self)
        button2.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button2, 1, 0)
        
        
        button3 = QPushButton("javascript", self)
        button3.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button3, 1, 1)
        
        
        button4 = QPushButton("c#", self)
        button4.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button4, 2, 0)
        
        
        button5 = QPushButton("java", self)
        button5.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        gridlayout.addWidget(button5, 2, 1)
         
        self.groupBox.setLayout(gridlayout)
        
myapp = QApplication(sys.argv)
window = Window()
#window.show()
myapp.exec_()
sys.exit(0)