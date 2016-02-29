from person import Person 
from manager import Manager
import shelve

bob=Person('Bob Smith',42,30000,'software')
sue=Person('Sue Jones',45,40000,'hardware')
tom=Manager('Tom Doe',50,50000)

data=shelve.open('class-shelves')
data['bob']=bob
data['sue']=sue
data['tom']=tom

#print(bob.name)
#print(data['bob'].name)
data.close()