from tkinter import *

window = Tk()
window.title('My first gui program')
window.minsize(width=600, height=600)
window.config(padx=10, pady=10)
my_label = Label(text='I am a label', font=("Arial", 24, "bold"))
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='New new text')
my_label.grid(column=0, row=0)
#  BUTTON
input = Entry()
input.grid(column=1, row=1)
input_result = input.get()


def button_clicked():
    input_result = input.get()
    my_label.config(text=input_result)


button = Button(text='click me', fg='red', bg='blue', command=button_clicked)
button.grid(column=3, row=3)


window.mainloop()
