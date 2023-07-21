from tkinter import *


def button_clicked():
    miles_int = float(miles_text_box.get())
    km = miles_int * 1.61
    result_label['text'] = km


window = Tk()

window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
check_input = IntVar()
miles_text_box = Entry(width=10)
miles_text_box.insert(END, string="0")
miles_text_box.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles",)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
