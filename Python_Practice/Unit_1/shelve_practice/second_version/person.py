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