from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5 import uic

class Toolbox(QMainWindow):
	def __init__(self):
		super(Toolbox, self).__init__()
		uic.loadUi("main.ui", self)
		self.tool1 = self.findChild(QToolButton, "screenrecord")
		self.tool1.pressed.connect(self.openscreenrecord)
		self.tool2 = self.findChild(QToolButton, "remote")
		self.tool3 = self.findChild(QToolButton, "screenextend")
		self.tool3.pressed.connect(self.openscreenextend)
		self.tool4 = self.findChild(QToolButton, "hidshare")
		self.tool4.triggered.connect(self.openmouse)
		self.tool5 = self.findChild(QToolButton, "classroom")
		self.tool6 = self.findChild(QToolButton, "meeting")
		self.shadow1 = QGraphicsDropShadowEffect()
		self.shadow1.setColor(QColor(138, 145, 140))
		self.shadow1.setBlurRadius(50)
		self.shadow2 = QGraphicsDropShadowEffect()
		self.shadow2.setColor(QColor(138, 145, 140))
		self.shadow2.setBlurRadius(50)
		self.shadow3 = QGraphicsDropShadowEffect()
		self.shadow3.setColor(QColor(138, 145, 140))
		self.shadow3.setBlurRadius(50)
		self.shadow4 = QGraphicsDropShadowEffect()
		self.shadow4.setColor(QColor(138, 145, 140))
		self.shadow4.setBlurRadius(50)
		self.shadow5 = QGraphicsDropShadowEffect()
		self.shadow5.setColor(QColor(138, 145, 140))
		self.shadow5.setBlurRadius(50)
		self.shadow6 = QGraphicsDropShadowEffect()
		self.shadow6.setColor(QColor(138, 145, 140))
		self.shadow6.setBlurRadius(50)
		self.tool1.setGraphicsEffect(self.shadow1)
		self.tool2.setGraphicsEffect(self.shadow2)
		self.tool3.setGraphicsEffect(self.shadow3)
		self.tool4.setGraphicsEffect(self.shadow4)
		self.tool5.setGraphicsEffect(self.shadow5)
		self.tool6.setGraphicsEffect(self.shadow6)
		self.show()
		
	def openscreenrecord(self):
		from screen_recorder_gui import ScreenRecorder
		self.ui = ScreenRecorder()
		#self.ui.close()
		self.ui.show()

	def openscreenextend(self):
		from screen_extender_gui import ScreenExtender
		self.ui = ScreenExtender()
		self.ui.show()

	def openmouse(self):
		from mouse_share import MouseShare
		self.ui = MouseShare()
		self.ui.show()


app = QApplication(sys.argv)
UIWindow = Toolbox()
app.exec_()