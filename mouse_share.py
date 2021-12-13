from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from PyQt5 import uic
import pyautogui
import keyboard
from ctypes import *

so_file = "libraw_mouse.dll"
my_functions = CDLL(so_file)
print(type(my_functions))
class MouseShare(QMainWindow):
	def __init__(self, ):
		super(MouseShare, self).__init__()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		uic.loadUi("Mouse_Keyboard_share.ui", self)
		self.start = self.findChild(QAction, "actionStart")
		self.start.triggered.connect(self.started)
		self.delta = self.findChild(QLabel, "delta")
		self.coords = self.findChild(QLabel, "coords")
		self.keys = self.findChild(QLabel, "keys")
		self.keyraw = self.findChild(QLabel, "keyraw")
		my_functions.init_raw_mouse(True, False, True)

	def started(self):
		while True:
			x = my_functions.get_raw_mouse_x_delta(0)
			y = my_functions.get_raw_mouse_y_delta(0)
			print("x = "+str(x))
			print("y = "+str(y))
			self.delta.setText("X : "+str(x)+" "+"Y : "+str(y))
			cur_x, cur_y = pyautogui.position()
			pyautogui.FAILSAFE = True
			QCoreApplication.processEvents()
			self.coords.setText("X :"+str(cur_x)+ " Y : "+str(cur_y))
			if keyboard.is_pressed('q'):  # if key 'q' is pressed 
				self.keys.setText('q')#
				print("exiting!")
				break
			if keyboard.is_pressed('a'):
				self.keys.setText("a")

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_a:
			Print("a")

	def closeEvent(self, event):
		print("closing")
		my_functions.WM_DESTROY()
		#so_file = "raw_mouse.so"
		#my_functions = CDLL(so_file)
		#print(type(my_functions))
		#mouses= my_functions.raw_mouse_count()
		#x = my_functions.get_raw_mouse_x_delta(mouses)
		#y = my_functions.get_raw_mouse_y_delta(mouses)
		#print("x = "+str(x))
		#print("y = "+str(y))
		#self.delta.setText("X : "+str(x)+" "+"Y : "+str(y))

app = QApplication(sys.argv)
UIWindow = MouseShare()
UIWindow.show()
app.exec_()