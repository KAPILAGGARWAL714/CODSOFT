from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
kap = Tk()
kap.geometry('500x450+500+200')
kap.title('TO-DO LIST')
kap.config(bg='#223441')
kap.resizable(width=False, height=False)

frame = Frame(kap)
frame.pack(pady=20)

lb = Listbox(frame, width=35, height=10, font=('Times', 18), bd=0,
    fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(kap, font=('comicsansms', 24), width=20)
my_entry.pack()

button_frame = Frame(kap, bg="#223441")
button_frame.pack(pady=20)

addTask_btn = Button(button_frame, text='Add Task', font=('comicsansms 14 bold'),
    bg='#c5f776', padx=20, pady=4, command=newTask, width=6, relief=SUNKEN)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT,padx=5, ipadx=6)

delTask_btn = Button(button_frame, text='Delete Task', font=('comicsansms 14 bold'),
    bg='#ff8b61', padx=20, pady=4, command=deleteTask, width=9, relief=SUNKEN)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT,padx=5, ipadx=1)

kap.mainloop()