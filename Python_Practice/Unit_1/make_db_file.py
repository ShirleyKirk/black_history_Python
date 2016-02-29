dbfilename = 'people-file'
ENDDB = 'end the data box.'
ENDREC = 'end the record'
RECSEP = '=>'

def storeDbase(data_box,dbfilename=dbfilename):
	dbfile = open(dbfilename,'w')
	for key in data_box:
		dbfile.write(key+'\n')
		for (name,value) in data_box[key].items():
			dbfile.write(name+RECSEP+repr(value)+'\n')
		dbfile.write(ENDREC)
	dbfile.write(ENDDB)
	dbfile.close()
def loadDbase(dbfilename=dbfilename):
	dbfile=open(dbfilename)
	import sys
	sys.stdin=dbfile
	data_box={}
	key=input()
	while key!=ENDDB:
		record={}
		field=input()
		while field!=ENDREC:
			name,value=field.split(RECSEP)
			record[name]=eval(value)
			field=input()
		data_box[key]=record
		key=input()
	return data_box

if __name__=='__main__':
	from script_test import data_box
	storeDbase(data_box)