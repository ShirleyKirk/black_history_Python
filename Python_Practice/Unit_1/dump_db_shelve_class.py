import shelve

data=shelve.open('class-shelves')
for key in data:
	print (data[key].name)