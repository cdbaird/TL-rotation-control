import threading
import os
import sys
from configparser import ConfigParser
from rotation import Motor
from helper import find_ports

class Tapedrive():
	def __init__(self, motor1=None, motor2=None, cfg='config.ini'):
		if (motor1 is None) or (motor2 is None):
			try:
				self.get_config(cfg)
				self.connect_motors()
			except FileNotFoundError:
				print('No configuration file found!')
				print('Unable to initialise motors. Check configuration.')
				print('Exiting...')
				sys.exit()
			except IOError as e:
				print(e)
				sys.exit()
	
		assert isinstance(motor1, elliptec.Motor)
		assert isinstance(motor2, elliptec.Motor)
	
	def get_config(self, cfg):
		if not os.path.isfile(cfg):
			raise FileNotFoundError
		self.config = ConfigParser()
		self.config.read(cfg)
		if (not self.config.has_option('motors', 'motor1')) 
			or (not self.config.has_option('motors', 'motor2')):
			raise IOError('One or more motor configurations not found in %s' % cfg)

	def connect_motors(self):
		ports = find_ports()
		if (len(ports) < 2):
			raise IOError('Tapedrive needs 2 motors, %s found' % str(len(ports)))








		


