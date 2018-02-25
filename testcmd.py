testcmds = [('0in', b'0IN081080004120170701016800040000\r\n'),	# OK
			('1in', b''),										# cmd ERR Wrong Address
			('0in0', b'0IN081080004120170701016800040000\r\n'),	# cmd ERR Unnecessary data
			('0ho0', b'0PO00000001\r\n'),						# OK
			('0ho0', b'0POFFFFFFFF\r\n'),						# OK (-ve position value)
			('0gp', b'0POFFFFFFFF\r\n'),						# OK (-ve position value)
			('0gs',b'0GS00\r\n'),								# OK
			('0ho0', b'0GS02\r\n'),								# rsp ERR can't move
			('0fw', b'0GS02\r\n'),								# rsp ERR "
			('0bw', b'0GS02\r\n'),								# rsp ERR "
			('0gs', b'0GS02\r\n'),								# rsp ERR "
			('0sj00008000', b'0GS00\r\n'),						# OK
			('0sj00007fff', b'0GS00\r\n'),						# cmd ERR (lowercase hex)
			('0sj00007FFF', b'0GS00\r\n'),						# OK
			('0gj', b'0GJ00008000\r\n'),						# OK
			('0ma', b''),										# cmd ERR no data
			('0ma00040000', b'0GS0C\r\n'),						# rsp ERR out of range
			('0mr', b''),										# cmd ERR no data
			('0mr00040000', b'0PO00000000\r\n'),				# OK ?
			('0mr00050000', b'0PO0000FFFA\r\n'),				# cmd ERR, rsp unpredictable
			]