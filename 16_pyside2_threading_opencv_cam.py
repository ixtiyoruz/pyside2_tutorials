# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout, QMainWindow
import sys
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import Signal, Slot, QThread
import cv2
import numpy as np

class WorkerCam(QThread):
    onImageRetreived = Signal(bool, np.ndarray)
    def __init__(self, cap):
        self.cap = cap
        self.counter = 0
        QThread.__init__(self)
        
    def run(self):
        while(True):
            ret, img = self.cap.read()
            print(self.counter)
            self.counter =self.counter + 1
            self.onImageRetreived.emit(ret, img)

class WorkerDraw(QThread):
    onImageDrawed = Signal(np.ndarray)

    def __init__(self):
        self.counter = 0
        self.img_new = None
        QThread.__init__(self)
    
    @Slot(bool, np.ndarray)
    def onImageReceived(self, ret, img):
        self.img_new= img        
        if(self.img_new is not None):
            self.draw()
            self.counter = self.counter +1
        self.onImageDrawed.emit(self.img_new)

    def draw(self):
        h, w, _ = self.img_new.shape
        x = int(w / 2)
        y = int(h / 2)
        cv2.putText(self.img_new,"HI" + str(self.counter), (x,y), 0, 2, 255)
                
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("open video")
        self.setGeometry(300, 300, 800, 600)
        self.create_main_frame()
        self.setImageView()        
        self.cap = cv2.VideoCapture(0)
        self.thread = WorkerCam(self.cap)
        self.drawer = WorkerDraw()
        self.thread.onImageRetreived.connect(self.drawer.onImageReceived)
        self.drawer.onImageDrawed.connect(self.displayFrame)
        self.thread.start()
        self.drawer.start()
    def create_main_frame(self):
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)    
    
    @Slot(np.ndarray)   
    def displayFrame(self, img):
#        ret, frame = self.cap.read()
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.imageView.setPixmap(QPixmap(qImg)) 
        
    def setImageView(self):
        layout = QVBoxLayout()
        self.imageView = QLabel("no video input")
        layout.addWidget(self.imageView)
        self.mainWidget.setLayout(layout)
        
myapp = QApplication(sys.argv)
window = MainWindow()
window.show()
myapp.exec_()
sys.exit(0)