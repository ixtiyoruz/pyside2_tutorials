# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QDesktopWidget, QMainWindow, QStatusBar, QProgressBar,QLabel
import sys
from PySide2.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sttting icon")
        self.setGeometry(300, 300, 500, 400)
        self.setIcon()
        # showing a hint, or tooltip
        self.setToolTip("this is window")
#        self.setButton()
        self.center()
        self.pushButton()
        
        self.statusLabel = QLabel("showing progress")
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.createStatusBar()
    def setIcon(self):
        appIcon = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        self.setWindowIcon(appIcon)
   
    def setButton(self):
        btn1 = QPushButton("Quit", self)
        btn1.move(50,100)
        btn1.clicked.connect(self.quitApp)
        
    def quitApp(self):
        userInfo = QMessageBox.question(self, "Confirmation", "Do you want to quit the application ?", QMessageBox.Yes|QMessageBox.No)
        if(userInfo == QMessageBox.Yes):
            myapp.quit()
        elif(userInfo == QMessageBox.No):
            pass
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
        
    def pushButton(self):
        self.aboutButton = QPushButton("About box", self)
        self.aboutButton.move(50, 100)
#        self.move(50, 100)
        self.aboutButton.clicked.connect(self.aboutBox)
    def aboutBox(self):
        QMessageBox.about(self.aboutButton, "About pyside 2", "Pyside 2 is cross platfirmn gui")
    def createStatusBar(self):
        self.myStatus = QStatusBar()
#        self.myStatus.showMessage("status bar is ready", 3000)
        self.progressbar.setValue(10)
        self.myStatus.addWidget(self.statusLabel, 1)
        self.myStatus.addWidget(self.progressbar, 2)
        self.setStatusBar(self.myStatus)
        
myapp = QApplication(sys.argv)
window = Window()
window.show()
myapp.exec_()
sys.exit(0)