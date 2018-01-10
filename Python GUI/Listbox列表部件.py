
# coding: utf-8

# In[24]:


import tkinter as tk

w=tk.Tk()
w.title('my window')

var2=tk.StringVar()
l=tk.Label(w,bg='green',height='2',width='15',textvariable=var2)
l.pack()

def do_it():
    value=lb.get(lb.curselection())
    var2.set(value)

b=tk.Button(w,text='确认',height='2',width='15',command=do_it)
b.pack()

var1=tk.StringVar()
var1.set((11,22,33,44))
lb=tk.Listbox(w,width='15',listvariable=var1)
lb.pack()

w.mainloop()

