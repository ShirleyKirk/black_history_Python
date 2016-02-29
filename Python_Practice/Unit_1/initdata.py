bob={'name':'Bob Smith','age':42,'pay':30000,'job':'software'}
sue={'name':'Sue Jones','age':45,'pay':40000,'job':'hardware'}
tom={'name':'Tom Doe','age':50,'pay':50000,'job':'manager'}

db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

if __name__=='__main__':
	for key in db:
		print(key,"=>",db[key])