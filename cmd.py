
cmd = {
	'info' : b'in',
	'status' : b'gs',
	'home' : b'ho',
	'forward' : b'fw',
	'backward' : b'bw'
	'get_step' : b'gj'
	'set_step' : b'sj'
	}

if __name__ == '__main__':
	keys = cmd.keys()
	print('\n'.join(keys))
