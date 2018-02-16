import threading
import os
import sys
from configparser import ConfigParser
from elliptec import Motor, find_ports

class Tapedrive():
	def __init__(self, motor1=None, motor2=None, cfg='./elliptec/tapedrive/config.ini'):
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
		else:
			assert isinstance(motor1, Motor)
			assert isinstance(motor2, Motor)
			self.motor1 = motor1
			self.motor2 = motor2
	
	def get_config(self, cfg):
		if not os.path.isfile(cfg):
			raise FileNotFoundError
		self.config = ConfigParser()
		self.config.read(cfg)
		if ((not self.config.has_option('motors', 'motor1')) 
			or (not self.config.has_option('motors', 'motor2'))):
			raise IOError('Motor configurations not found in %s' % cfg)
		self.sn_mot1 = self.config['motors']['motor1']
		self.sn_mot2 = self.config['motors']['motor2']

	def connect_motors(self):
		ports = find_ports()
		if (len(ports) < 2):
			raise IOError('Tapedrive needs 2 motors, %s found' % str(len(ports)))
		for port in ports:
			if port.serial_number == self.sn_mot1:
				self.motor1 = Motor(port.device)
			elif port.serial_number == self.sn_mot2:
				self.motor2 = Motor(port.device)
		
		







		


