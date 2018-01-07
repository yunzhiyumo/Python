
# coding: utf-8

# In[63]:


import tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x100')

var = tk.StringVar()
var.set('you hit me')

l = tk.Label(w,textvariable=var,font=('Arial',12),bg='green',height='2',width='15')
l.pack()

sw = False
def hit_me():
    global sw
    if sw == True:
        sw = False
        var.set('you hit me')
    else:
        sw = True
        var.set('')

b = tk.Button(w,text='hit me',height='2',width='15',command=hit_me)
b.pack()

w.mainloop()

