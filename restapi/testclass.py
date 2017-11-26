import pprint

import requests
import json

# hey there, comment

class math:
	''' this is a math class  '''	
	def sum(self, a, b):
		''' addes two numbers '''
		return a+b
		
	def sub(self, a, b):
		''' subtract two numbers '''
		return a-b

	def mul(self, a, b):
		''' multiply two numbers '''
		return a*b

	# original method
	def restcall(self):
		''' it's a sample rest api call'''
		
		# this is using request module here.
		response = requests.get('http://echo.jsontest.com/title/ipsum/content/blah')
		return json.loads(response.content)


class operation(math):

	# default constructor
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	# method override.
	def restcall(self):
		''' it's a sample local rest api call'''
		
		# this is using request module here.
		response = requests.get('http://127.0.0.1:8000/datadetail/')
		return json.loads(response.content)
	
	def detail(self):
		''' it's a sample local rest api call'''
		
		# this is using request module here.
		response = requests.get('http://127.0.0.1:8000/userdetail/')
		return json.loads(response.content)
	
	def div(self):
		''' divide two numbers '''
		return self.a / self.b


m = math()
o = operation(20, 10)

#print o.restcall()
#print o.detail()

print json.dumps(o.restcall(), indent=4, sort_keys=True)
print json.dumps(o.detail(), indent=4, sort_keys=True)

print o.__doc__
print m.mul.__doc__

#help(o)

print o.div()

#print m.sum(5, 6)
#print m.sub(5, 6)
#print m.mul(5, 6)
#print o.div(16, 2)
#print o.mul(16, 2)
#print o.div(m.sum(20, 10), m.sub(20, 10))
#print m.restcall()


