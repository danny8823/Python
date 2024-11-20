from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)


def action():
    miles_input = miles_entry.get()
    converted_num = int(miles_input) * 1.6
    km_result_label.config(text=f'{round(converted_num)}')


calc_button = Button(text='Calculate', command=action)
calc_button.grid(column=1, row=2)
window.mainloop()
