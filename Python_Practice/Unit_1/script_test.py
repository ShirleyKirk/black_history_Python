bob={
	'name':'Bob Smith',
	'age':42,
	'pay':30000,
	'job':'software'
}
sue={
	'name':'Sue Jones',
	'age':42,
	'pay':40000,
	'job':'hardware'
}
tom={
	'name':'Tom Westons',
	'age':37,
	'pay':61000,
	'job':'all engineering'
}

data_box={}
data_box['bob']=bob
data_box['sue']=sue
data_box['tom']=tom

if __name__=='__main__':
	for key in data_box:
		print(key,'=>',data_box[key])
	
