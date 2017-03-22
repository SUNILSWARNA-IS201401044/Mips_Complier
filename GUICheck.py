from Tkinter import *

def prInt():
	print "Helllo"
d={'a':1,'b':2}
root=Tk()
root.title("CA")
#l=Label(root,text="Hello")
#l.pack()
top=Frame(root)
top.pack()
bot=Frame(root)
bot.pack(side=BOTTOM)
but1=Button(top,text=d['a'],fg="red")
but3=Button(top,text=d['b'],fg="purple")
but1.pack()
but3.pack()
ph=PhotoImage(file="ser.png")
lb=Label(root,image=ph)
lb.pack()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
but2=Button(top,text="See",command=prInt)
but2.pack()
root.mainloop()
