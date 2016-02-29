#from initdata_classes import bob,sue,tom
import shelve
from person import Person
from manager import Manager

bob=Person('Bob Smith',42,30000,'software')
sue=Person('Sue Jones',45,40000,'hardware')
tom=Manager('Tom Doe',50,50000,'manager')

data_box=shelve.open('class-shelve')
data_box['bob']=bob
data_box['sue']=sue
data_box['tom']=tom

for element in data_box:
	print(element,'=>\n',data_box[element].name)

data_box.close()