from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QObject#
import sys
from PyQt5 import uic
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

class ScreenRecorder(QMainWindow):
	def __init__(self):
		super(ScreenRecorder, self).__init__()
		uic.loadUi("Screen_recoder.ui", self)
		self.play = self.findChild(QAction, "actionplay")
		self.play.triggered.connect(self.start)
		self.stop = self.findChild(QAction, "actionstop")
		self.stop.triggered.connect(self.cancelFeed)
		self.preview = self.findChild(QLabel, "preview")
		#self.preview.setPixmap(img_np)

	def start(self):
		self.worker1 = worker1()
		self.worker1.start()
		self.worker1.ImageUpdate.connect(self.ImageUpdateSlot)

	def ImageUpdateSlot(self, Image):
		self.preview.setPixmap(QPixmap.fromImage(Image))

	def cancelFeed(self):
		self.worker1.stop()

class worker1(QThread):
	ImageUpdate = pyqtSignal(QImage)
	def run(self):
		self.ThreadActive = True
		Capture = cv2.VideoCapture(0)
		while self.ThreadActive:
			ret, frame = Capture.read()
			if ret:
				Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				FlippedImage = cv2.flip(Image, 1)
				ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
				Pic = ConvertToQtFormat.scaled(980, 580)# Qt.KeepAspectRatio
				self.ImageUpdate.emit(Pic)

	def stop(self):
		self.ThreadActive = False
		self.quit()

		


	
app = QApplication(sys.argv)
UIWindow = ScreenRecorder()
UIWindow.show()
app.exec_()