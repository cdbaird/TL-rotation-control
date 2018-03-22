
get_ = {
	'info' : b'in',
	'status' : b'gs',
	'position': b'gp',
	'stepsize' : b'gj'
	}

set_ = {
	'stepsize' : b'sj',
	'isolate'  : b'is'
	}

mov_ = {
	'home' : b'ho',
	'forward' : b'fw',
	'backward' : b'bw',
	'absolute' : b'ma',
	'relative' : b'mr'
	}


def commands():
	return [get_, set_, mov_]

if __name__ == '__main__':
	keys = cmd.keys()
	print('\n'.join(keys))
