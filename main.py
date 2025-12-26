#----------------File Imports------------------# 

import tkinter as tk
from tkinter import ttk

#------------Create_Roots----------------------#
root = tk.Tk()
root.geometry("400x500")
root.title("ToDo")
root.iconbitmap("icon.ico")
tasklist = []


#-------------------Function------------------------------#

def add_task(event):
    task = task_entry.get()
    task_entry.delete(0,tk.END)
    try:
        with open("tasklist.txt","a") as file:
            file.write(f"\n{task}")

        listbox.insert(tk.END,task)
        tasklist.append(task)
    except:
        print("File Not Work")    

def delete_task():
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    tasklist.remove(task)
    
    try:
        with open("tasklist.txt","w") as file:
            for task in tasklist:
                file.write(task)

    except:
        print("File Not Work")


def open_task():

    try:
        with open("tasklist.txt","r") as file:
            tasks = file.readlines()
            print(tasks)
            for task in tasks:
                if task != "\n":
                    listbox.insert(tk.END,task)
                    tasklist.append(task)
    
    
    except:
        print("File Not Work")






#-----------------UI Desings-------------------------------#


heading = ttk.Label(root,text="ALL TASK",font="Arial 20 bold")
heading.pack()

frame1 = ttk.Frame(root,width=350,height=50)
frame1.pack(pady=25)

task_entry = ttk.Entry(frame1,font="Arial 18",width=28)
task_entry.pack()

frame2 = ttk.Frame(root,width=350,height=300)
frame2.pack()

listbox = tk.Listbox(frame2,font="Arial 13",width=42,height=15)
listbox.pack()

#Event Bind 
task_entry.bind("<Return>",add_task)

open_task()

s = ttk.Style()
s.configure("TButton",font=('Arial',12))

delete_button = ttk.Button(root,text="Delete",style="TButton",command=delete_task)
delete_button.pack(side="bottom",pady=12,ipadx=10,ipady=15)








#-----------------------main_loop----------------------------#
root.mainloop()