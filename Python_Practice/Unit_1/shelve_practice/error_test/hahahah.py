import shelve
#from person import Person

data=shelve.open('open-shelve')
print(data['bob'].name)