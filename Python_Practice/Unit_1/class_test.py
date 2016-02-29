class Person:
	def __init__(self,name,age,pay=0,job=None):
		self.name=name
		self.age=age
		self.pay=pay
		self.job=job
	def giveRaise(self,percent,bonus=0.1):
		self.pay*=(1.0+percent+bonus)
	def __str__(self):
		return '<%s => %s>' %(self.__class__.__name__,self.name)

if __name__=='__main__':
	bob=Person('Bob Smith',42,30000,'software')
	sue=Person('Sue Jones',45,40000,'hardware')
	tom=Person('Tom Doe',50,50000)
	people=[bob,sue,tom]
	for element in people:
		element.giveRaise(.10)
		print (element.name,'=>',element.pay)
	print (tom)