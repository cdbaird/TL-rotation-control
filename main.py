from PyQt5 import QtCore, QtGui, QtWidgets
from td_gui import Ui_TapeDriveWindow

import elliptec.tapedrive as td
import elliptec

class mainProgram(QtWidgets.QMainWindow, Ui_TapeDriveWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.tapedrive = td.Tapedrive()
		# Set default stepsize
		self.tapedrive.motor1.set_('stepsize', 
			self.tapedrive.motor1.deg_to_hex(self.verticalSlider.value()))
		self.tapedrive.motor2.set_('stepsize', 
			self.tapedrive.motor2.deg_to_hex(self.verticalSlider.value()))

		self.btnForward.clicked.connect(self.forward)
		self.btnBackward.clicked.connect(self.backward)
		self.btnHome.clicked.connect(self.home)
		self.btnM2bw.clicked.connect(self.mot2_bw)
		self.btnM2fw.clicked.connect(self.mot2_fw)
		self.btnM1bw.clicked.connect(self.mot1_bw)
		self.btnM1fw.clicked.connect(self.mot1_fw)
		self.btnIsolate.clicked.connect(self.isolate)

		self.verticalSlider.valueChanged.connect(self.on_slider_drag)
		self.verticalSlider.sliderReleased.connect(self.on_slider_release)
		self.homeEnable.toggled.connect(self.home_button_toggle)
		self.IsolateEnable.toggled.connect(self.isolate_button_toggle)

	def mot2_bw(self):
		self.tapedrive.motor2.do_('backward')

	def mot2_fw(self):
		self.tapedrive.motor2.do_('forward')

	def mot1_bw(self):
		self.tapedrive.motor1.do_('backward')

	def mot1_fw(self):
		self.tapedrive.motor1.do_('forward')

	def forward(self):
		self.tapedrive.motor1.do_('forward')
		self.tapedrive.motor2.do_('forward')

	def backward(self):
		self.tapedrive.motor2.do_('backward')
		self.tapedrive.motor1.do_('backward')

	def home(self):
		self.tapedrive.motor1.do_('home')
		self.tapedrive.motor2.do_('home')

	def isolate(self):
		self.tapedrive.motor1.set_('isolate', '01')
		self.tapedrive.motor2.set_('isolate', '01')

	def on_slider_drag(self):
		val = self.verticalSlider.value()
		self.spinBox.setValue(val)
		#self.mot1.set_('stepsize', self.mot1.deg_to_hex(val))

	def on_slider_release(self):
		val = self.verticalSlider.value()
		cmd_val = self.tapedrive.motor1.deg_to_hex(val)
		#print(cmd_val)
		self.tapedrive.motor1.set_('stepsize', self.tapedrive.motor1.deg_to_hex(val))
		self.tapedrive.motor1.get_('stepsize')
		self.tapedrive.motor2.set_('stepsize', self.tapedrive.motor1.deg_to_hex(val))
		self.tapedrive.motor2.get_('stepsize')

	def home_button_toggle(self):
		self.btnHome.setEnabled(self.homeEnable.isChecked())

	def isolate_button_toggle(self):
		self.btnIsolate.setEnabled(self.IsolateEnable.isChecked())
		


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	tdgui = mainProgram()
	tdgui.show()
	sys.exit(app.exec_())



