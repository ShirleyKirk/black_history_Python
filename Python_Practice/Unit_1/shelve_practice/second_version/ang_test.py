from person import Person
import shelve

yuki=Person('Oreki_Yuki',20,5000,'Engineering')
data=shelve.open('Okay-shelve')
data['yuki']=yuki
print (yuki.name)
print (data['yuki'].name)

