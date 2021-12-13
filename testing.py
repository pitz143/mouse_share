from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ExampleWindow(QMainWindow):
    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        #self.p = self.frameGeometry().width()
        self.setWindowTitle("testing")
        self.setWindowIcon(QIcon('logo.png'))
        #print(self.frameGeometry().width())
        self.initUI()

    def initUI(self):
        self.showMaximized()
        #self.setFixedSize(self.windowsize)
        #self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        widget = QWidget()
        self.setCentralWidget(widget)
        pixmap1 = QPixmap('picture_1.jpg')
        pixmap1 = pixmap1.scaledToWidth(self.windowsize.width())
        self.image = QLabel()
        self.image.setPixmap(pixmap1)

        layout_box = QHBoxLayout(widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.image)

        pixmap2 = QPixmap('picture_2.jpg')
        self.image2 = QLabel(widget)
        self.image2.setPixmap(pixmap2)
        screen = app.primaryScreen()
        size = screen.size()
        x = int(size.width()-700)
        y = int(size.height()-500-80)
        #print("this is it :"+ str(size.width()), str(size.height()))
        self.image2.setGeometry(x,y,700, 500)
        self.image2.setAlignment(Qt.AlignRight)
        #self.image2.setFixedSize(pixmap2.size())
        #self.image2.move(p)
        #image2 = self.image2.geometry().width()
        #print(image2)
        #p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        #self.image2.move(p)#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())