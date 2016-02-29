from person import Person
from manager import Manager
import shelve

bob=Person('Bob Smith',42,30000,'software')
sue=Person('Sue Jones',45,40000,'hardware')
tom=Manager('Tom Doe',50,50000,'manager')

data_new=shelve.open('classes-shelve')
data_new['bob']=bob
data_new['sue']=sue
data_new['tom']=tom

#-----test------
#print(data_new['bob'].name)
#print(bob.name)