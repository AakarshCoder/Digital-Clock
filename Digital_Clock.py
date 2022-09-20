from tkinter import*
from time import strftime
from tkinter.ttk import*
#Initializing Windows
root = Tk()
root.title('Digital Clock')
def clock():
    tick= strftime('%H:%M:%S')
    label_1.config(text=tick)
    label_1.after(1000,clock)


#Declaring label
label_1= Label(root, font= ('Verdana',100),background=("purple"), foreground = ("yellow"))

label_1.pack(anchor="center")
clock()
mainloop()























