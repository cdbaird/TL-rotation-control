import serial
from .cmd import get_, set_, mov_
from .helper import parse, error_check, move_check
import sys
from . import status


class Motor(serial.Serial):

	def __init__(self, port, baudrate=9600, bytesize=8, parity='N', timeout=2):
		try:
			#self.motor = s.Serial(port, baud, bytesize, parity)
			super().__init__(port, baudrate=9600, bytesize=8, parity='N', timeout=2)
		except serial.SerialException:
			print('Could not open port %s' % port)
			sys.exit()

		if self.is_open:
			print('Connection established!')
			#self.port = port
			self._get_motor_info()
			self.conv_factor = float(self.info['Range'])/float(self.info['Pulse/Rev'])
			self.range = self.info['Range']
			self.counts_per_rev = self.info['Pulse/Rev']
			#self.get_('status')
			#self.get_('position')

	def do_(self, req='home', data='0', addr='0'):
		try:
			instruction = mov_[req]
		except KeyError:
			print('Invalid Command: %s' % req)
		else:
			command = addr.encode('utf-8') + instruction
			if data:
				command += data.encode('utf-8')

			self.request = command
			self.write(command)
			self.response = self.read_until(terminator=b'\n')
			self.status = parse(self.response)
			move_check(self.status)

	def set_(self, req='', data='', addr='0'):
		try:
			instruction = set_[req]
		except KeyError:
			print('Invalid Command')
		else:
			command = addr.encode('utf-8') + instruction
			if data:
				command += data.encode('utf-8')

			self.write(command)
			#print(command)
			response = self.read_until(terminator=b'\n')
			#print(response)
			self.status = parse(response)
			error_check(self.status)

	def get_(self, req='status', data='', addr='0'):
		try:
			instruction = get_[req]
		except KeyError:
			print('Invalid Command')
		else:
			command = addr.encode('utf-8') + instruction
			if data:
				command += data.encode('utf-8')

			self.write(command)
			#print(command)
			response = self.read_until(terminator=b'\n')
			print(response)
			self.status = parse(response)
			error_check(self.status)

	def deg_to_hex(self, deg):
		factor = self.counts_per_rev//self.range
		val = hex(deg*factor)
		return val.replace('0x', '').zfill(8).upper()

	def hex_to_deg(self, hexval):
		factor = self.counts_per_rev//self.range
		val = round(int(val,16)/factor)
		return val


## Private methods

	def _get_motor_info(self):
			# instruction = cmd['info']
			self.info = self._send_command(get_['info'])

	def _send_command(self, instruction, msg=None, address=b'0'):
		command = address + instruction
		if msg:
			command += msg
		#print(command)
		self.write(command)
		response = self.read_until(terminator=b'\n')
		#print(response)
		return parse(response)

	def __str__(self):
		string = '\nPort - ' + self.port + '\n\n'
		for key in self.info:
			string += (key + ' - ' + str(self.info[key]) + '\n')			
		return string


	



	










