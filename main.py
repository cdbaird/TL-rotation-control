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
		self.verticalSlider.valueChanged.connect(self.on_slider_drag)

	def forward(self):
		self.mot1.do_('forward')

	def backward(self):
		self.mot1.do_('backward')

	def on_slider_drag(self):
		val = self.verticalSlider.value()
		self.spinBox.setValue(val)

	def on_slider_release(self):
		val = self.verticalSlider.value()
		self.mot1.set_('stepsize', str(hex(val*262144//360)))



if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ports = elliptec.find_ports()

	tdgui = mainProgram(ports[0])
	tdgui.show()
	sys.exit(app.exec_())



