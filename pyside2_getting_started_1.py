#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:03:58 2020

@author: ixtiyor
"""

# So the main modules of pyside 2 
#1. Qt core
#it provides core properties, like serialization , time, date and so on
#2. Qt Gui
# it provides guis for qt cores
#3. Qt Widgets
#it will provide ready widgets , this is the main part which you use ofen
#4. Qt qml
#it provides environmenmt that you can design your project gui
#5. Qt Quick
#it will provides classes for qt quick and qt applications
#6. Qt Quck Widgets
# it provides puish buttons, progress bars edittexts and so on 
#7 Qt barCharts 
#8 Qt barcharts
#9 Qt multimedia
#10 Qt  Multimedia
#11 Qt WebEngine WIdgets
# widgets can handle web contents
#12 Qt Webchannels
# enables peer to peer comunication


#pip install pyside2

from PySide2.QtWidgets import QApplication , QWidget
import sys
import time

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyside 2 simple application")
        self.setGeometry(300, 300, 300, 300)
#        self.setMinimumWidth(250)
#        self.setMinimumHeight(100)
#        self.setMaximumWidth(800)
#        self.setMaximumHeight(200)


myapp = QApplication(sys.argv)
window = Window()
window.show()

time.sleep(5)
window.resize(640, 400)
myapp.exec_()
sys.exit(0)