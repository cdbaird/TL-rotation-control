import threading
import os
import sys
from configparser import ConfigParser
from rotation import Motor

class Tapedrive():
	def __init__(self, motor1=None, motor2=None, cfg='config.ini'):
		if (motor1 is None) or (motor2 is None):
			try:
				self.get_config(cfg)
				self.connect_motors()
			except FileNotFoundError:
				print('No configuration file found!')

		else:
			assert isinstance(motor1, elliptec.Motor)
			assert isinstance(motor2, elliptec.Motor)
	
	def get_config(self, cfg):
		if not os.path.isfile(cfg):
			raise FileNotFoundError
		self.config = ConfigParser()
		self.config.read(cfg)

	def connect_motors(self):





		


