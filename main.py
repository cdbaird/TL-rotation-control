from PyQt5 import QtCore, QtGui, QtWidgets
from td_gui import Ui_TapeDriveWindow

import elliptec

class mainProgram(QtWidgets.QMainWindow, Ui_TapeDriveWindow):
	def __init__(self, port):
		super().__init__()
		self.setupUi(self)
		self.mot1 = elliptec.Motor(port)
		self.btnForward.clicked.connect(self.forward)
		self.btnBackward.clicked.connect(self.backward)
		self.btnHome_2.clicked.connect(self.home)
		self.verticalSlider.valueChanged.connect(self.on_slider_drag)
		self.verticalSlider.sliderReleased.connect(self.on_slider_release)

	def forward(self):
		cmd = Command('forward')
		self.mot1.do(cmd)

	def backward(self):
		cmd = Command('backward')
		self.mot1.do(cmd)

	def home(self):
		cmd = Command('home', data='0')
		self.mot1.do(cmd)

	def on_slider_drag(self):
		val = self.verticalSlider.value()
		self.spinBox.setValue(val)
		#self.mot1.set_('stepsize', self.mot1.deg_to_hex(val))

	def on_slider_release(self):
		val = self.verticalSlider.value()
		cmd_val = self.mot1.deg_to_hex(val)
		#print(cmd_val)
		self.mot1.set_('stepsize', self.mot1.deg_to_hex(val))
		self.mot1.get_('stepsize')



if __name__ == '__main__':
	import sys
	from elliptec.motor import Motor, Command
	app = QtWidgets.QApplication(sys.argv)
	ports = elliptec.find_ports()

	tdgui = mainProgram(ports[0])
	tdgui.show()
	sys.exit(app.exec_())



