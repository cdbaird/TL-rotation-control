import sys


class Status():
	def __init__(self, request, response):
		if ((request is None) or (response is None)):
			raise ValueError('Parser input cannot be empty!')

		self.request = self.parse(request)
		self.response = self.parse(response)
		self.info = None
		self.errcode = None
		self.position = None

	def parse(self, msg):
		msg = msg.decode().strip()
		addr = msg[0]
		code = msg[1:3].upper()
		data = msg[3:]
		return (addr, code, data)

	def has_error(self):
		if ((self.response[1] == 'GS') and (self.response[2] != '0')):
			return True

	def has_moved(self):
		code_req = self.request[1]
		code_rsp = self.response[1]
		if ((code_req == 'HO' )
			or (code_req == 'FW')
			or (code_req == 'BW')
			or (code_req == 'MA')
			or (code_req == 'MR')):
			# If a move command was sent, check if it actually moved
			return ((code_rsp == 'PO') or (code_rsp == 'BO'))

	def distribute(self): # if response contains X, update X.
		rsp = self.response
		if ((rsp[1] == 'PO') or (rsp[1] == 'BO')):
			self.position = rsp[2]
		elif (rsp[1] == 'IN'):
			self.info = rsp[2]
		elif (rsp[1] == 'GS'):
			self.errcode = rsp[2]







	
class Other():
	def __init__(self):
		self.var = 'banana'
		self.parse = Parser(b'0in', b'0IN081080004120170701016800040000\r\n')
		self.info = self.parse.info






def test():
	test_request = b'0in'
	test_response = b'0IN081080004120170701016800040000\r\n'
	parser = Parser(test_request, test_response)
	print(parser.request)
	print(parser.response)

if __name__ =='__main__':
	test()