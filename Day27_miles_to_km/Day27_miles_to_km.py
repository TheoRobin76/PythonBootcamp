from tkinter import *

FONT = ("Arial", 16)


def convert():
    try:
        miles = float(num_miles.get())
        km = round(miles * 1.609, 2)
        km_conversion.config(text=km)
    except ValueError:
        pass


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# labels
label1 = Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)
label1.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

km_conversion = Label(text=0, font=FONT)
km_conversion.grid(column=1, row=1)
km_conversion.config(padx=20, pady=20)

# entry
num_miles = Entry(width=5, font=FONT)
num_miles.insert(END, 0)
num_miles.grid(column=1, row=0)

# button
calculate = Button(text="Calculate", font=FONT, command=convert)
calculate.grid(column=1, row=2)


window.mainloop()
