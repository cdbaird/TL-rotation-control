import serial as s

class RotStage():

	def __init__(self, port, baud=9600, bytesize=8, parity='N'):
		try:
			self.motor = s.Serial(port, baud, bytesize, parity)

		except s.SerialException:
			print('Could not open port %s' % port)

		if self.motor.is_open:
			self.get_motor_info()
			self.status = self.get_status()

## Get parameters

	def get_motor_info(self):
		# instruction = cmd['info']
		self.info = self.send_command(cmd['get_info'])

	def get_status(self):
		self.status = self.send_command(cmd['get_status'])

	def get_step_size(self):
		self.status = self.send_command(cmd['get_step'])


## Set parameters

	def set_step_size(self, msg):
		self.status = self.send_command(cmd['set_step'], msg)
	
## Move

	def home(self, msg=b'0'): # 0 for CW, 1 for ACW
		# instruction = b'ho'		 
		self.status = self.send_command(cmd['home'], msg)

	def fw_jog(self):
		self.status = self.send_command(cmd['forward'])

	def bw_jog(self):
		self.status = self.send_command(cmd['backward'])

	

	
## Private methods

	def send_command(self, instruction, msg=None, address=b'0'):
		command = address + instruction
		if msg:
			command += msg
		#print(command)
		self.motor.write(command)
		response = self.motor.read_until(terminator=b'\n')
		return response
