# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

#import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QDesktopWidget, QMainWindow, QStatusBar, QProgressBar,QLabel,QVBoxLayout,QAction,QMenu,QToolBar
import sys
from PySide2.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from PySide2.QtWidgets import QFileDialog
import cv2
import qimage2ndarray
#sys.modules['PyQt5.QtGui'] = PySide2.QtGui
# or if you have PyQt5 installed, you might need this
# sys.modules['PyQt5.QtGui'] = QtGui
from PIL import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("open video")
        self.setGeometry(300, 300, 800, 600)
        self.setIcon()
        # showing a hint, or tooltip
#        self.setToolTip("this is window")
#        self.center()
#        self.centralwidget = QWidget(self)
#        self.setCentralWidget(self.centralwidget)
        
        self.add_menu()
        self.create_main_frame()
        
        self.setImageView()
        
        self.statusLabel = QLabel("showing progress")
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.createStatusBar()
        self.init()
    
    def init(self):
        self.file_name = ""
        self.timer = QTimer()
        self.timer.timeout.connect(self.displayFrame)

    def create_main_frame(self):
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)    
    def open_video(self):
        self.fname = QFileDialog.getOpenFileName()
        
        print(self.fname[0])
        
        self.cap = cv2.VideoCapture(self.fname[0])
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        
        self.timer.start()

    def add_menu(self):
        menubar = self.menuBar()
        menu = QMenu('File', self) # title and parent
        file_action = QAction("Open file", self) # title and parent
        file_action.setStatusTip("Select a file to play")
        file_action.triggered.connect(self.open_video)
        
        menu.addAction(file_action)
        menubar.addMenu(menu)
        menubar.setNativeMenuBar(False)
        self.statusBar().showMessage("Ready")
        
    def displayFrame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.imageView.setPixmap(QPixmap(qImg)) 
        
    def setImageView(self):
        layout = QVBoxLayout()
        self.imageView = QLabel("no video input")
        layout.addWidget(self.imageView)
        self.mainWidget.setLayout(layout)
    def setIcon(self):
        appIcon = QIcon("Screenshot from 2019-10-15 09-33-25.png")
        self.setWindowIcon(appIcon)
 
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    def createStatusBar(self):
        self.myStatus = QStatusBar()
#        self.myStatus.showMessage("status bar is ready", 3000)
        self.progressbar.setValue(10)
        self.myStatus.addWidget(self.statusLabel, 1)
        self.myStatus.addWidget(self.progressbar, 2)
        self.setStatusBar(self.myStatus)
        
myapp = QApplication(sys.argv)
window = MainWindow()
window.show()
myapp.exec_()
sys.exit(0)