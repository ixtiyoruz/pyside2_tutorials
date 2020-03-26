# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys
from PySide2.QtGui import QIcon, QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sttting icon")
        self.setGeometry(300, 300, 500, 400)
        self.setIcon()
        self.setIconModes()
        # showing a hint, or tooltip
        self.setToolTip("this is window")
    def setIcon(self):
        appIcon = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        self.setWindowIcon(appIcon)
        
    def setIconModes(self):
        # inabled icon
        icon1 = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        label1 = QLabel("Sample", self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        
        # this one is disabled icon
        icon2 = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        label2 = QLabel("sample", self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)
        

        # third
        icon3 = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        label3 = QLabel("sample", self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit(0)