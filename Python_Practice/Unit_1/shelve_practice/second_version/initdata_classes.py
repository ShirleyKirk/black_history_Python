class Person:
	def __init__(self,name,age,pay,job):
		self.name=name
		self.age=age
		self.pay=pay
		self.job=job
	def __str__(self):
		pass
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay *=(1.0+percent)

class Manager(Person):
	def giveRaise(self,percent,bonus=0.1):
		self.pay *= (1.0+bonus+percent)

bob=Person('Bob Smith',42,30000,'software')
sue=Person('Sue Jones',45,40000,'hardware')
tom=Manager('Tom Doe',50,50000,'manager')

#data_box={}
#data_box['bob']=bob
#data_box['sue']=sue
#data_box['tom']=tom

#for element in data_box:
#	print(element,'=>\n',data_box[element].name)