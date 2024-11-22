from tkinter import *

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
background_image = PhotoImage(
    file="/Users/danny714/Desktop/Python/Day 29/pass_manager/logo.png")

website_label = Label(text='Website:')
email_username_label = Label(text='Email/Username:')
password_label = Label(text='Password:')

website_label_input = Entry(width=35)
website_label_input.focus()
email_username_label_input = Entry(width=35)
email_username_label_input.insert(0, "danny@gmail.com")
password_label_input = Entry(width=21)

generate_pass_button = Button(text='Generate Password', width=14)
add_button = Button(text='Add', width=36)


website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_label_input.grid(column=1, row=1, columnspan=2)
email_username_label_input.grid(column=1, row=2, columnspan=2)
password_label_input.grid(column=1, row=3)


add_button.grid(column=1, row=4, columnspan=2)
generate_pass_button.grid(column=2, row=3)

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)


window.mainloop()
