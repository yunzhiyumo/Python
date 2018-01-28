
# coding: utf-8

# In[12]:


import tkinter as tk   #python2.7是import Tkinter as tk

w = tk.Tk()
w.title('my window')
w.geometry('200x200')

e = tk.Entry(w,show='*')
e.pack()

t = tk.Text(w,height=2)
t.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)
    
def insert_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(w,text='insert point',height='2',width='20',command=insert_point)
b1.pack()

b2 = tk.Button(w,text='insert end',height='2',width='20',command=insert_end)
b2.pack()
    
w.mainloop()

