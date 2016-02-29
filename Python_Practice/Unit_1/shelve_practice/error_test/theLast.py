import shelve
from person import Person
from manager import Manager

data_new=shelve.open('open-shelve')
data_new['bob']=bob
data_new['sue']=sue
data_new['tom']=tom

print(data_new['bob'].name)
print(bob.name)