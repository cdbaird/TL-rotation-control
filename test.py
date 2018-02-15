import elliptec

def revolve360(motor, revs=1):
	motor.get_step_size()
	stepsize = 0x8000
	steps_per_rev = 0x40000
	jognum = steps_per_rev//stepsize
	for _ in range(revs*jognum):
		motor.fw_jog()
		print(motor.status)



def main():
	ports = elliptec.find_ports()
	#print([p.device for p in ports])
	mot1 = elliptec.Motor(ports[0][0])
	print(mot1)
	mot1.do_('home', '0')
	mot1.get_('status')
	mot1.do_('forward')
	mot1.do_('backward')
	mot1.do_('relative', '00020000')
	mot1.get_('status')
	mot1.do_('absolute', '00009500')
	



if __name__ == '__main__':
	main()
