import shelve

fieldnames=('name','age','pay','job')
maxfield=max(len(element) for element in fieldnames)
data=shelve.open('class-shelves')

while True:
	key=input('\nKey? => ')
	if not key:
		break
	try:
		record=data[key]
	except:
		print('No such key "%s"!' %key)
	else:
		for field in fieldnames:
			print(field.ljust(maxfield),'=>',getattr(record,field))