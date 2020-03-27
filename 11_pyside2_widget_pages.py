
from PySide2.QtWidgets import QWidget, QDesktopWidget, QMainWindow, QStatusBar, QProgressBar,QLabel,QVBoxLayout,QAction,QMenu
from PySide2.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import  QTimer
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFileDialog, QApplication, QWizard ,QWizardPage,QLineEdit, QHBoxLayout
import sys

# CREATE WIZARD, WATERMARK, LOGO, BANNER
app = QApplication(sys.argv)
wizard = QWizard()
wizard.setWizardStyle(QWizard.ModernStyle)
 
try: # PYSIDE
    wizard.setPixmap(QWizard.WatermarkPixmap,
        'Watermark.png')
    wizard.setPixmap(QWizard.LogoPixmap,
        'Logo.png')
    wizard.setPixmap(QWizard.BannerPixmap,
        'Banner.png')
except TypeError: # PYQT5
    wizard.setPixmap(QWizard.WatermarkPixmap,
        QPixmap('Watermark.png'))
    wizard.setPixmap(QWizard.LogoPixmap,
        QPixmap('Logo.png'))
    wizard.setPixmap(QWizard.BannerPixmap,
        QPixmap('Banner.png'))
 
# CREATE PAGE 1, LINE EDIT, TITLES
page1 = QWizardPage()
page1.setTitle('Page 1 is best!')
page1.setSubTitle('1111111111')
lineEdit = QLineEdit()
hLayout1 = QHBoxLayout(page1)
hLayout1.addWidget(lineEdit)
 
try: # PYSIDE
    page1.registerField('myField*',
        lineEdit,
        lineEdit.text(),
        'textChanged')
except TypeError: # PYQT5
    page1.registerField('myField*',
        lineEdit,
        lineEdit.text(),
        lineEdit.textChanged)
 
# CREATE PAGE 2, LABEL, TITLES
page2 = QWizardPage()
page2.setFinalPage(True)
page2.setTitle('Page 2 is better!')
page2.setSubTitle('Lies!')
label = QLabel()
hLayout2 = QHBoxLayout(page2)
hLayout2.addWidget(label)
 
# CONNECT SIGNALS AND PAGES
# lineEdit.textChanged.connect(lambda:label.setText(lineEdit.text()))
nxt = wizard.button(QWizard.NextButton)
func = lambda:label.setText(page1.field('myField'))
nxt.clicked.connect(func)
wizard.addPage(page1)
wizard.addPage(page2)
 
wizard.show()
sys.exit(app.exec_())
