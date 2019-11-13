import io
import tkinter
import os
from tkinter import *
from tkinter import messagebox
tk=Tk()
tk.geometry("200x150")
tk.title("Shutdown")
def shutdown():
	var2=var1.get()
	if var2=="kaungkhantzaw":
		b=messagebox.askquestion('Shutdown','Are you sure want to shutdown in 1 second?')
		if b=="yes":
			os.system('shutdown -s -t 1')
			tk.destroy()
		else:
			pass
	else:
		a.delete(0,END)
		messagebox.showwarning('Shutdown','Administrator Password Invalid!!')
def quit(self):
	shutdown()
var1=StringVar()
Label(tk,text="SHUTDOWN",font=10,bg="red").pack()
Label(tk,text="").pack()
Label(tk,text="Enter Administrator Password").pack()
a=Entry(tk,bd=5,textvariable=var1,show="*")
a.pack()
Label(tk,text="").pack()
Button(tk,text="Enter",bg="yellow",command=shutdown).pack()
tk.bind('<Return>',quit)
tk.mainloop()