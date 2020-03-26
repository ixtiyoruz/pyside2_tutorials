# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QDesktopWidget, QMainWindow, QStatusBar, QProgressBar,QLabel
from PySide2.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
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
        hbox = QHBoxLayout()
        
        button = QPushButton("CSS", self)
        button.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        button.setMinimumHeight(40)
        hbox.addWidget(button)
        
        button1 = QPushButton("C++", self)
        button1.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        button1.setMinimumHeight(40)
        hbox.addWidget(button1)
        
        button2 = QPushButton("Python", self)
        button2.setIcon(QIcon("Screenshot from 2019-10-15 09-33-25.png"))
        button2.setMinimumHeight(40)
        hbox.addWidget(button2)
        self.groupBox.setLayout(hbox)
        
myapp = QApplication(sys.argv)
window = Window()
#window.show()
myapp.exec_()
sys.exit(0)