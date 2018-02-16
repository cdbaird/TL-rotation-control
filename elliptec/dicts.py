
commands = {
	'info'		:	('in', 0),
	'status'	:	('gs', 0),
	'position'	:	('gp', 0),
	'get_step'	:	('gj', 0),
	'set_step'	:	('sj', 8),
	'home'		:	('ho', 1),
	'forward'	:	('fw', 0),
	'backward'	:	('bw', 0),
	'absolute'	:	('ma', 8),
	'relative'	:	('mr', 8)
	}

responses = {
	'IN' : {
			'Address' : '',
			'Motor Type' : '',
			'Serial No.' : '',
			'Year' : '',
			'Firmware' : '',
			'Thread' : '',
			'Hardware' : '',
			'Range' : '',
			'Pulse/Rev' : ''
			},
	'GS' : {
			'0' : 'Status OK',
			'1' : 'Communication Timeout',
			'2' : 'Mechanical Timeout',
			'3' : 'Command Error',
			'4' : 'Value Out of Range',
			'5' : 'Module Isolated',
			'6' : 'Module Out of Isolation',
			'7' : 'Initialisation Error',
			'8' : 'Thermal Error',
			'9' : 'Busy',
			'10': 'Sensor Error',
			'11': 'Motor Error',
			'12': 'Out of Range',
			'13': 'Over Current Error',
			},
	'GJ' : {'Stepsize' : '00000000'},
	'PO' : {'Position' : '00000000'},
	'BO' : {'Position' : '00000000'}
}
