import TLRot

def revolve360(motor, revs=1):
	motor.get_step_size()
	stepsize = 0x8000
	steps_per_rev = 0x40000
	jognum = steps_per_rev//stepsize
	for _ in range(revs*jognum):
		motor.fw_jog()
		print(motor.status)



def main():
	ports = TLRot.find_ports()
	mot1 = TLRot.Motor(ports[1])
	print(mot1)
	print(mot1.status)
	print('Homing...')
	mot1.home()
	print(mot1.status)
	# print('Moving...')
	# mot1.move_rel(b'00000010')
	# print(mot1.status)
	# print('Homing...')
	# mot1.home()
	# print(mot1.status)
	# revolve360(mot1, 2)

if __name__ == '__main__':
	main()
