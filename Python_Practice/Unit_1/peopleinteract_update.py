import shelve
from person import Person

fieldnames=('name','age','pay','job')
data=shelve.open('class-shelves')
maxfield=max(len(element) for element in fieldnames)

while True:
	key = input('\nkey=? => ')
	if not key:
		break
	if key in data:
		record=data[key]
		for field in fieldnames:
			print(field.ljust(maxfield),'=>',getattr(record,field))
	else:
		record=Person(name='?',age='?',pay=0,job=None)
		for field in fieldnames:
			currval = getattr(record,field)
			newtext = input('\t[%s]=%s\n\t\tnew=?=>' %(field,currval))
			if newtext:
				setattr(record,field,eval(newtext))
		for field in fieldnames:
			print(field.ljust(maxfield),'=>',getattr(record,field))
	data[key]=record
data.close()
