import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("To-do-list")
root.geometry("400x650+400+1")

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist",) as taskfile:
        
            task_list.append(task)
            listbox.insert(END , task) 

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"/n")
            
        listbox.delete (ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open("tasklist","r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file = open('tasklist','w')
        file.close()




#icon
Image_icon = PhotoImage(file="image/task.png")
root.iconphoto(False,Image_icon)

#topbar
Top_image = PhotoImage(file="image/topbar.png")
Label(root,image=Top_image).pack()

dock_image = PhotoImage(file="image/dock.png")
Label(root,image=dock_image,bg="#808080").place(x=0,y=0)

note_image = PhotoImage(file="image/task.png")
Label(root,image=note_image,bg="#808080").place(x=340,y=25)

heading = Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#808080")
heading.place(x=130,y=20)

#main
frame = Frame(root,width=400,height=400,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

#add
button = Button(frame,text="ADD",font="arial20bold",width=10,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=900,y=800) 


#listbox
frame1 = Frame(root,bd=3,width=00,height=280,bg="#000000")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="#808080" ,fg="white",cursor = "hand2",selectbackground="#5a95ff")
listbox.pack(side = LEFT , fill = BOTH , padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT,fill=BOTH)

openTaskFile()

#delete
delete_image = PhotoImage(file="image/delete.png")
Button(root,image=delete_image,bd=0,command=deleteTask).pack(side=BOTTOM,pady=10)
button.place(x=300,y=0) 
root.mainloop()

