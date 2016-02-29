import shelve
data_box=shelve.open('class-shelve')
for key in data_box:
	print(key,"=>\n",data_box[key].name,':',data_box[key].pay)

#print(data_box['tom'].lastName())
#bob=data_box['bob']
#print(bob.lastName())