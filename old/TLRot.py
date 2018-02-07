import serial as s
import serial.tools.list_ports as lp
import sys
from .cmd import cmd

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



def response_parse(response):
	pass
		 



def main():
	ports = find_ports()
	mot1 = TLMotor(ports[1])
	#print(mot1.info)
	#mot1.home()
	print(mot1.status)
	for _ in range(8):
		mot1.fw_jog()
		print(mot1.status)
	#mot1.fw_jog()




if __name__ =='__main__':
	main()