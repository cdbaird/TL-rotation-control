import serial as s
import serial.tools.list_ports as lp
import sys
from .errcodes import error_codes


# Some helper functions for TLRot module

def find_ports():
	avail_ports = []
	for port in lp.comports():
		if port.serial_number:
			try:
				p = s.Serial(port.device)
				p.close()
				avail_ports.append(port)
			except (OSError, s.SerialException):
				print('%s unavailable.\n')
				#pass
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
		return (code, str(int(errcode, 16)))

	else:
		return (code, msg[3:])


## Fails if message contains hex digit > 9 after code, e.g. '0POFFFFFFFD'. Deprecated
def get_msg_code(msg):
	print('WARNING: get_msg_code does not work correctly. Don\'t use it!')
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
	elif ((status[0] == "GS") and (status[1] != '0')): # is there an error?		
		err = error_codes[status[1]]
		print('ERROR: %s' % err)
	elif (status[0] == "PO"):
		print("Move complete")







def main():
	test_msg = b'0IN081080004120170701016800040000\r\n'
	print(parse(test_msg))




if __name__ =='__main__':
	main()