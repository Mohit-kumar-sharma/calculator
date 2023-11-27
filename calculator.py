from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            Value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    elif text=="Bck":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    
root = Tk()
root.title("Calculator ------ Mohit & Sharma ")
root.geometry("500x630")

scvalue=StringVar()
scvalue.set("")
screen= Entry(root,textvariable=scvalue,font="Lucida 20 bold")
screen.pack(fill=X,padx=8,pady=10,ipadx=10)

f= Frame(root,bg="grey")
button = Button(f,text="Bck",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18, pady=12)

button = Button(f,text="00",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="C", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="+", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)
f.pack()

f= Frame(root,bg="grey")
button = Button(f,text="7",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18, pady=12)

button = Button(f,text="8",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="9", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="/", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)
f.pack()


f= Frame(root,bg="grey")
button = Button(f,text="4",padx=16,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18, pady=12)

button = Button(f,text="5",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="6", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="*", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)
f.pack()

f= Frame(root,bg="grey")
button = Button(f,text="1",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18, pady=12)

button = Button(f,text="2",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="3", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="-", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)
f.pack()

f= Frame(root,bg="grey")
button = Button(f,text="0",padx=17,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18, pady=12)

button = Button(f,text=".",padx=18,pady= 18, font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="=", padx=18,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)

button = Button(f,text="+", padx=19,pady= 18,font="Lucida 20 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=12)
f.pack()

root.mainloop()