from tkinter import *


# tkinter documentation: http://tcl.tk/man/tcl8.6/contents.htm

def button_clicked():
    new_text = input.get()
    label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# button 1
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

# button 2
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# entry
input = Entry(width=10)
input.get()
input.grid(column=3, row=2)


window.mainloop()
