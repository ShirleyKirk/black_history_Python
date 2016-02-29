from person import Person

class Manager(Person):
	"""docstring for Manager"""
	def __init__(self,name,age,pay):
		Person.__init__(self,name,age,pay,'manager')
	def giveRaise(self,percent,bonus=0.1):
		Person.giveRaise(self,percent+bonus)	
			