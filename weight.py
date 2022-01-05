from tkinter import *

window = Tk()
window.title("Weight Converter")
window.geometry("620x200+600+400")
window.resizable(False, False)
window.configure(bg = 'sky blue')

def weight_conversion():
    in_kg = float(e1_value.get())
    in_grams = in_kg * 1000
    in_pounds = in_kg * 2.20462
    in_ounces = in_kg * 35.274
    t1.insert(END, in_grams)
    t2.insert(END, in_pounds)
    t3.insert(END, in_ounces)

def clear():
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")
    t3.delete("1.0", "end")
    e1_value.set("")

#Entries
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value, width = 23, bg = 'white')
e1.grid(row = 1, column = 1, padx = 10, pady = 10)
e1.config(font = ('Calibri', 11), bd = 2)

#Buttons
b1 = Button(window, text = 'Convert', bg = 'yellow', command = weight_conversion)
b1.grid(row = 1, column = 2, padx = 10, pady = 10)
b1.config(font = ('Calibri', 11), width = 10)

b2 = Button(window, text = 'Clear', bg = 'yellow', command = clear)
b2.grid(row = 1, column = 3, padx = 10, pady = 10)
b2.config(font = ('Calibri', 11), width = 10)

#Labels
l0 = Label(window, text = 'Enter Weight', bg = 'sky blue')
l0.grid(row = 0, column = 1, padx = 50, pady = 10)
l0.config(font = ('Arial', 10), width = 10)

l1 = Label(window, text = 'Kg', bg = 'sky blue')
l1.grid(row = 1, column = 0, padx = 10, pady = 10)
l1.config(font = ('Arial', 15))

l2 = Label(window, text = 'In grams', bg = 'sky blue')
l2.grid(row = 3, column = 1, padx = 10, pady = 10)
l2.config(font = ('Arial', 12))

l3 = Label(window, text = 'In pounds', bg = 'sky blue')
l3.grid(row = 3, column = 2, padx = 10, pady = 10)
l3.config(font = ('Arial', 12))

l4 = Label(window, text = 'In ounces', bg = 'sky blue')
l4.grid(row = 3, column = 3, padx = 10, pady = 10)
l4.config(font = ('Arial', 12))

#Text Boxes
t1 = Text(window, height = 1, width = 20, bg = 'white')
t1.grid(row = 4, column = 1, padx = 10)
t1.config(fg = 'red', font = ('Arial', 11))

t2 = Text(window, height = 1, width = 20, bg = 'white')
t2.grid(row = 4, column = 2, padx = 10)
t2.config(fg = 'red', font = ('Arial', 11))

t3 = Text(window, height = 1, width = 20, bg = 'white')
t3.grid(row = 4, column = 3, padx = 10)
t3.config(fg = 'red', font = ('Arial', 11))

window.mainloop()