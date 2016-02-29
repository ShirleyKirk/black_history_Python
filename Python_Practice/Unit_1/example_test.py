from make_db_file import storeDbase,loadDbase

data_box = loadDbase()
data_box['sue']['pay'] *= 1.10 
#data_box['tom']['name'] = 'Tom Tom'

storeDbase(data_box)