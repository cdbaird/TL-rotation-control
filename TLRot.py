import serial as s
import serial.tools.list_ports as lp
import sys
from cmd import cmd

def find_ports():
	if sys.platform.startswith('darwin'):
		ports = [comport.device for comport in lp.comports()]
		# print(ports)
	else:
		raise OSError('Not Implemented for this OS: %s' % sys.platform)
	
	avail_ports = []	
	for port in ports:
		try:
			p = s.Serial(port)
			p.close()
			avail_ports.append(port)
		except (OSError, s.SerialException):
			pass

	return avail_ports

class TLMotor():

	def __init__(self, port, baud=9600, bytesize=8, parity='N'):
		try:
			self.motor = s.Serial(port, baud, bytesize, parity)

		except s.SerialException:
			print('Could not open port %s' % port)

		if self.motor.is_open:
			self.get_motor_info()


	def get_motor_info(self):
		# instruction = cmd['info']
		self.info = self.send_command(cmd['info'])

	def home(self, msg=b'0'): # 0 for CW, 1 for ACW
		# instruction = b'ho'		 
		self.status = self.send_command(cmd['home'], msg)

	def fw_jog(self):
		self.status = self.send_command(cmd['forward'])

	def get_step_size(self):
		self.status = self.send_command(cmd['get_step'])

	def set_step_size(self, msg):
		self.status = self.send_command(cmd['set_step'], msg)

	def send_command(self, instruction, msg=None, address=b'0'):
		command = address + instruction
		if msg:
			command += msg
		#print(command)
		self.motor.write(command)
		response = self.motor.read_until(terminator=b'\n')
		return response


def response_parse(response):
	pass
		 



def main():
	ports = find_ports()
	mot1 = TLMotor(ports[1])
	#print(mot1.info)
	#mot1.home()
	#print(mot1.status)
	#mot1.get_step_size()
	#print(mot1.status)
	#mot1.fw_jog()
	#print(mot1.status)




if __name__ =='__main__':
	main()