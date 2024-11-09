from tkinter import *
from tkinter.ttk import *

window = Tk()

df = [['tom', 10, 'Male'], ['juli', 12, 'Male'], ['nick', 15, 'Male'], ['juli', 14, 'Female'], ['nick', 20, 'Male']] #column = Name, Age, Gender

def callback1(e):
    name = cbox.get()
    lbox.delete("0", "end")
    values_from_selected_name = list(set([record[1] for record in df if record[0]==name]))
    lbox['values'] = values_from_selected_name

Label(window, text='Name: ').grid(row=0, column=0, padx=10, pady=10)
cbox = Combobox(window, width=10, state="readonly")
cbox.grid(row=0, column=1)
all_values = list(set([record[0] for record in df]))
cbox['values'] = all_values
cbox.bind("<<ComboboxSelected>>", callback1)

Label(window, text='Age: ').grid(row=1, column=0)
lbox = Combobox(window, width=10)
lbox.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()