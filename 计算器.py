from math import *
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
def calc():
    text = var.get()
    result = eval(text)
    result = result / 1.0
    result = str(result)
    var.set(result)
text = ''
result = ''
root = Tk()
pi = 3.1415926535897932
root.geometry('360x48')
root.resizable(width=False,height=False)
root.title('Mini Calculator')
var = StringVar()
entry = Entry(root,textvariable=var,width=360)
button = Button(root,text='GET RESULT',command=calc)
entry.pack()
button.pack()
root.mainloop()