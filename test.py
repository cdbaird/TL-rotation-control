import elliptec
import random as r
import time

def main():
	ports = elliptec.find_ports()
	print(ports)
	mot1 = elliptec.Motor(ports[0])
	#print(mot1)
	#mot1.do_('home', '0')
	
	test = ['00007ffe', '00007fff', '00008000', '00008001', '00008002','00008003','00008004']

	zero_val = []
	for i in range(0,32768,100):
		v = r.randint(0,1)
		if v == 0:
			val = hex(i).replace('0x', '').zfill(8)
		else:
			val = hex(i).replace('0x', '').zfill(8).upper()

		#val = mot1.deg_to_hex(r.randint(1,359))
		#val = mot1.deg_to_hex(45*val)
		req = mot1.set_('stepsize', val)
		rsp = mot1.get_('stepsize')
		print(req.decode())
		print(rsp.decode()[3:])
		if (rsp == b'0GJ00000000\r\n'):
			zero_val.append(req.decode())
		#time.sleep(1.0)


	print('Zero Value for: \n')
	print('\n'.join(zero_val))


	print('Zero Value Count = %s' % str(len(zero_val)))
	for item in zero_val:
		for char in item:
			if char.isdigit():
				item = item.replace(char, '')
		if item.isupper():
			print('FALSE')





		#	print(val, rsp)


	# #(mot1.status)
	# mot1.do_('forward')
	# mot1.set_('stepsize', '00020000')
	# #(mot1.status)
	# mot1.do_('forward')


	



if __name__ == '__main__':
	main()
