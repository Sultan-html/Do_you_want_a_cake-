from tkinter import *
import random

root = Tk()
root.title('Опрос')
root.geometry('300x250')
root.configure(bg='lightblue')

def move_button(event):
    button_yes.place(x=random.randint(0, 250), y=random.randint(0, 200))

def click_no():
    button_no.config(state=DISABLED)
    label.pack_forget()
    button_yes.place_forget()
    button_no.place_forget()
    label_no = Label(root, text='Круто, мне больше достанется!', font=('Arial', 15), bg='lightyellow', fg='black')
    label_no.pack(pady=80)

label = Label(root, text='Хочешь торт?', font=('Arial', 20), bg='lightgreen', fg='black')
label.pack(pady=20)

button_yes = Button(root, text='Да', bg='red', fg='white', width=3, height=1)
button_no = Button(root, text='Нет', bg='green', fg='white', command=click_no, width=3, height=1)

button_yes.place(x=200, y=80)
button_no.place(x=80, y=80)

button_yes.bind('<Enter>', move_button)

root.mainloop()
