from tkinter import *

#-----001 part------#
#Label(text='Spam').pack()
#mainloop()

#-----101 part------#
from tkinter.messagebox import showinfo

'''def reply():
	showinfo(title='popup',message='Ouch!')

window=Tk()
button=Button(window,text='press',command=reply)
button.pack()
window.mainloop()'''

#-----102 part------#
"""class MyGui(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self,parent)
		button = Button(self,text='press',command=self.reply)
		button.pack()
	def reply(self):
		showinfo(title='popup',message='Ouch!!')

if __name__=='__main__':
	window=MyGui()
	window.pack()
	window.mainloop()"""

#-----103 part------#
def reply(name):
	showinfo(title='Reply',message='Hello %s ~: )' %name)

top = Tk()
top.title('Echo')
#top.iconbitmap('py-blue-out.ico')

Label(top,text='Please Enter Your Name:').pack(side=TOP)
ent=Entry(top)
ent.pack(side=TOP)
buttons=Button(top,text="Submit",command=(lambda:reply(ent.get())))
buttons.pack(side=LEFT)
top.mainloop()