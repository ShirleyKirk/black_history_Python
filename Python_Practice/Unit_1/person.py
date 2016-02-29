class Person:
 	"""docstring for Person"""
 	def __init__(self,name,age,pay,job):
 		#super(Person, self).__init__()
 		self.name = name
 		self.age = age
 		self.pay = pay
 		self.job = job
 	def lastName(self):
 		return self.name.split()[-1]
 	def giveRaise(self,percent):
 		self.pay *=(1.0+percent)