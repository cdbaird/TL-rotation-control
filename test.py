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
	print([p.device for p in ports])
	mot1 = elliptec.Motor(ports[0][0])
	mot1.do_('home', '0')
	mot1.get_('status')
	print(mot1.status[1])



if __name__ == '__main__':
	main()
