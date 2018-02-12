import serial as s
import serial.tools.list_ports as lp
import sys

from .errcodes import error_codes


# Some helper functions for TLRot module

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

def parse(msg):
	if not msg.endswith(b'\r\n'):
		print('Status/Response may be incomplete!')
	msg = msg.decode().strip()
	code = msg[1:3]
	try: 
		addr = int(msg[0], 16)
	except ValueError:
		raise ValueError('Invalid Address: %s' % msg[0])

	if (code.upper() == 'IN'):
		info = {'Address' : str(addr),
			'Motor Type' : msg[3:5],
			'Serial No.' : msg[5:13],
			'Year' : msg[13:17],
			'Firmware' : msg[17:19],
			'Thread' : is_metric(msg[19]),
			'Hardware' : msg[20],
			'Range' : (int(msg[21:25], 16)),
			'Pulse/Rev' : (int(msg[25:], 16)) }
		return info

	elif (code.upper() == 'PO'):
		pos = msg[3:]
		return (code, (s32(int(pos, 16))))

	elif (code.upper() == 'GS'):
		errcode = msg[3:]
		return (code, int(errcode, 16))

def get_msg_code(msg):
	code = [c for c in msg if not c.isdigit()]
	return ''.join(code)

def is_metric(num):
	if (num == '0'):
		thread_type = 'Metric'
	elif(num == '1'):
		thread_type = 'Imperial'
	else:
		thread_type = None

	return thread_type

def s32(value): # Convert 32bit signed hex to int
	return -(value & 0x80000000) | (value & 0x7fffffff)

def error_check(status):
	if not status:
		print('Status is None')
	elif ((status[0] == "GS") and (status[1] != 0)): # is there an error?		
		err = error_codes[status[1]]
		print('ERROR: %s' % err)
	elif (status[0] == "PO"):
		print("Move complete")







def main():
	test_msg = b'0IN081080004120170701016800040000\r\n'
	print(parse(test_msg))




if __name__ =='__main__':
	main()