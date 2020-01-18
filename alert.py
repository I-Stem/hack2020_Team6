import tkinter
from tkinter import messagebox


top = tkinter.Tk()

def ignoreIntrusion():
    result = messagebox.askquestion("Ignore Intrusion", "Are You Sure?", icon='warning')
    if result == 'yes':
        print ("Ignored")
    else:
        print ("Not Ignored")

B1 = tkinter.Button(top, text = "Ignore Intrusion", command = ignoreIntrusion)
B1.pack()
top.mainloop()