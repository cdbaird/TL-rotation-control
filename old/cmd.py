
cmd = {
	'get_info' : b'in',
	'get_status' : b'gs',
	'home' : b'ho',
	'get_pos': b'po',
	'forward' : b'fw',
	'backward' : b'bw',
	'get_step' : b'gj',
	'set_step' : b'sj'
	}

if __name__ == '__main__':
	keys = cmd.keys()
	print('\n'.join(keys))
