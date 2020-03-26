# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
import sys
from PySide2.QtGui import QIcon
from PySide2.QtCore import  QTimer, SIGNAL,QTime
 
class DigitalClock(QLCDNumber):
    def __init__(self):
        super(DigitalClock, self).__init__()
        self.setWindowTitle("sttting icon")
#        self.setGeometry(300, 300, 500, 400)
        self.setIcon()
        # showing a hint, or tooltip
        self.setToolTip("this is window")
        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(1000)
        self.showTime()
        self.resize(400, 200)
        
    def setIcon(self):
        appIcon = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        self.setWindowIcon(appIcon)
    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm")
#        print(text)
        if(time.second() % 2 ==0):
            text = text[:2]  +' ' + text[3:]
        self.display(text)
        
myapp = QApplication(sys.argv)
window = DigitalClock()
window.show()
myapp.exec_()
sys.exit(0)