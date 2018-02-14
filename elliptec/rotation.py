import serial as s
from .cmd import cmd
from .helper import parse, error_check
import sys

class Motor(s.Serial):

	def __init__(self, port, baud=9600, bytesize=8, parity='N'):
		try:
			#self.motor = s.Serial(port, baud, bytesize, parity)
			super().__init__(port, baud, bytesize, parity, timeout=2)
		except s.SerialException:
			print('Could not open port %s' % port)
			sys.exit()

		if self.is_open:
			self.port = port
			self.get_motor_info()
			self.conv_factor = float(self.info['Range'])/float(self.info['Pulse/Rev'])
			self.get_status()
			self.get_position()

	def do(self, req='get_status', data=None, addr=b'0'):
		try:
			instruction = cmd[req]
		except KeyError:
			print('Invalid Command')
		command = addr + instruction
		if data:
			command += data.encode('utf-8')

		self.write(command)
		response = self.read_until(terminator=b'\n')
		self.status = parse(response)	

## Get parameters

	def get_motor_info(self):
		# instruction = cmd['info']
		self.info = self.send_command(cmd['get_info'])
		
	def get_status(self):
		self.status = self.send_command(cmd['get_status'])

	def get_step_size(self):
		self.status = self.send_command(cmd['get_step'])

	def get_position(self):
		self.position = self.send_command(cmd['get_pos'])[1] # Shouldn't need message code 
		self.position_deg = self.position * self.conv_factor

## Set parameters

	def set_step_size(self, msg):
		self.status = self.send_command(cmd['set_step'], msg)
	
## Move stage

	def mv_home(self, msg=b'0'): # 0 for CW, 1 for ACW		 
		self.status = self.send_command(cmd['home'], msg)

	def mv_fstep(self):
		self.status = self.send_command(cmd['forward'])

	def mv_bstep(self):
		self.status = self.send_command(cmd['backward'])

	def mv_abs(self, msg=None):
		if not msg:
			raise IOError('move_abs requires a value!')

		self.status = self.send_command(cmd['move_abs'], msg)

	def mv_rel(self, msg=None):
		if not msg:
			raise IOError('move_rel requires a value!')

		self.status = self.send_command(cmd['move_rel'], msg)


## Private methods

	def send_command(self, instruction, msg=None, address=b'0'):
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

## Main methods

	def home(self):
		error_check(self.status)
		self.mv_home()
		error_check(self.status)
		self.get_position()
		print(self.position_deg)

	def fstep(self):
		print(self.status)
		error_check(self.status)
		self.mv_fstep()
		print(self.status)
		error_check(self.status)
		self.get_position()
		print(self.position_deg)

	



	










