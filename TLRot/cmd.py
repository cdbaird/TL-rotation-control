
cmd = {
	'get_info' : b'in',
	'get_status' : b'gs',
	'get_pos': b'po',
	'get_step' : b'gj',
	'set_step' : b'sj',
	'home' : b'ho',
	'forward' : b'fw',
	'backward' : b'bw',
	'move_abs' : b'ma',
	'move_rel' : b'mr'

	}


def commands():
	return cmd

if __name__ == '__main__':
	keys = cmd.keys()
	print('\n'.join(keys))
