import sys
import serial

from .dicts import commands, responses
from .helper import is_valid_hex


class Motor(serial.Serial):
	def __init__(self, port):
		try:
			super().__init__(port, baudrate=9600, bytesize=8, parity='N', timeout=2)
			print('Connection Established!')
		except serial.SerialException:
			print('Could not open port %s' % port)
			sys.exit()

	def do(self, command):
		if not isinstance(command, Command):
			raise IOError('ERROR: Not a Command Object')
		self.write(command.command)
		self._receive(command.request)

	def _receive(self, request):
		msg = self.read_until(terminator=b'\n')
		self.response = Response(request, msg)


class Command():
	def __init__(self, msg, data=''):
		self.is_valid = False
		
		# default address setting for motor. Shouldn't ever need to change this.
		self.addr = '0' 

		self.msg = str(msg)
		self.data = str(data)
		self._check_command()
		if self.is_valid:
			self._compile_command()

	def _check_command(self):
		try:
			self.request, datasize = commands[self.msg]
			if len(self.data) != datasize:
				raise ValueError
			if (datasize == 8) and (not is_valid_hex(self.data)):
				raise TypeError
		except KeyError:
			raise KeyError('Invalid command, %s' % self.msg)
		except ValueError:
			raise ValueError('Incorrect datasize, %d' % len(self.data))
		except TypeError:
			raise TypeError('Data format incorrect')
		else:
			self.is_valid = True
			
	def _compile_command(self):
		command = self.addr + self.request + self.data
		self.command = command.encode('utf-8')

class Response():
	def __init__(self, request, response):
		print(request)
		print(response)
		self.req = request.upper()
		self.rsp = response
		self.status = None
		self.info = None
		self.position = None
		self.stepsize = None
		self.velocity = None

		self._handle()
		# self._fill_values()

	def _handle(self):
		if not self.rsp.endswith(b'\r\n'):
			print('WARNING: Response incomplete!')
		self.rsp = self.rsp.decode()
		code = self.rsp[1:3]
		data = self.rsp[3:]
		if self.req == code:
			pass








if __name__ == '__main__':
	from helper import find_ports
	ports = find_ports()
	mot = Motor(ports[-1])
	cmd = Command('backward')
	mot.do(cmd)




