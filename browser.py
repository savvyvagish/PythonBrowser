import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setIcon(QIcon('leftarrow.png'))
        navbar.addAction(back_btn)


        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setIcon(QIcon('rightarrow'))
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setIcon(QIcon('reload.png'))
        navbar.addAction(reload_btn)

    
app = QApplication(sys.argv)
QApplication.setApplicationDisplayName('Savvy Browser')
window = MainWindow()
app.exec_()