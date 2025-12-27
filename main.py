#-----------------------------File Imports-------------------------------# 

import tkinter as tk
from tkinter import ttk

#---------------------------Create_Roots----------------------------------#
root = tk.Tk()
root.geometry("450x700+100+20")
root.title("ToDo")
root.iconbitmap("icon.ico")
root.configure(bg="lightblue")
root.resizable(False,False)
tasklist = []



#-----------------------------Function------------------------------------#

#--------------Task add the listbox and file--------------#
def add_task(event=None):
    task = task_entry.get()
    task_entry.delete(0,tk.END)
    try:
        with open("tasklist.txt","a") as file:
            file.write(f"\n{task}")

        listbox.insert(tk.END,task)
        tasklist.append(task)
    except:
        print("File Not Work")    


#-------------task delete the list box and file------------#
def delete_task():
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    tasklist.remove(task)
    
    try:
        with open("tasklist.txt","w") as file:
            for task in tasklist:
                file.write(f"\n{task}")

    except:
        print("File Not Work")

#------------Get the listbox for the previus add task ------#
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


#------------------------------------Styles-------------------------------------#
s = ttk.Style()
s.configure("TButton",font=('Arial',12),background="blue",clickcolor="green",)

Lstyle=ttk.Style()
Lstyle.configure("TLabel",font=("Arial", 15),borderwidth=10,background="red")


#----------------------------------UI Desings-----------------------------------#

#---Main_headline---

heading = ttk.Label(root,text="Your ToDo",font="Arial 20 bold",background="yellow")
heading.pack(pady=10,padx=10)

#------headline-----
remaining_task = ttk.Label(root,text="Remaining Tasks",font="Arial 15")
remaining_task.place(x=20,y=70)

#---create the Frame----
frame1 = ttk.Frame(root,width=350,height=300)
frame1.place(x=20,y=120)

#----create the listbox----
listbox = tk.Listbox(frame1,font="Arial 15",width=37,height=13,highlightthickness=0,selectbackground="red",background="lightgrey")
listbox.pack()

#-----delete button-----
delete_button = ttk.Button(root,text="Delete",style="TButton",width=10,command=delete_task)
delete_button.place(x=20,y=450)

#---headline task----
taskadd_heading = ttk.Label(root,text="Add New Task",style="TLabel")
taskadd_heading.place(x=20,y=500)


#---2nd Frame-----
frame2 = ttk.Frame(root,width=350,height=50)
frame2.place(x=20,y=550)


#-----Entry filed task------
task_entry = ttk.Entry(frame2,font="Arial 18",width=28)
task_entry.pack()

#Event Bind 
task_entry.bind("<Return>",add_task)


#add task button
taskadd_button = ttk.Button(root,text="ADD TASK",style="TButton",command=add_task)
taskadd_button.place(x=19,y=600)


#---File open call function-----
open_task()







#----------------------------------main_loop----------------------------------------#
root.mainloop()