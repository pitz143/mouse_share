from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5 import uic 

class ScreenExtender(QMainWindow):
	def __init__(self):
		super(ScreenExtender, self).__init__()
		uic.loadUi("Screen_extender.ui", self)
		self.preview = self.findChild(QLabel, "preview")
		self.actioncontains = self.findChild(QWidget, "widget_2")
		pixmap1 = QPixmap('picture_2.jpg')
		pixmap1 = pixmap1.scaled(self.width(), self.height())
		self.show()

	def resizeEvent(self, event):
		self.preview.resize(self.width(), self.height())

	def changeEvent(self, event):
		screen = app.primaryScreen()
		size = screen.size()
		x = size.width()
		y = size.height()
		x1 = x / 2 - 470
		if event.type() == QtCore.QEvent.WindowStateChange:
			if self.windowState() & QtCore.Qt.WindowMaximized:
				self.actioncontains.move(x/2-190, 0)
			elif event.oldState() & QtCore.Qt.WindowMaximized:
				self.actioncontains.move(470, 0)


app = QApplication(sys.argv)
UIWindow = ScreenExtender()
app.exec_()