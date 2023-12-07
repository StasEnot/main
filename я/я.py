from tkinter import*

tk=Tk()
tk.geometry("200x200")

def click():
    print("ghbdsn")


id1 = Label(text= "Зоюраження ")
id1.place(x= 60,y=45,width=75,height=45)

idl = Button(text= "Так", command=click)
idl.place(x= 60,y=95,width=75,height=45)


