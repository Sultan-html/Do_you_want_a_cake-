from tkinter import *
import random
from tkinter import messagebox
print('ehf=fe=fwef')

root = Tk()
root.title('Опрос')
root.geometry('400x300')
root.configure(bg='lightblue')

def move_button(event):
    button_yes.place(x=random.randint(0, 350), y=random.randint(0, 250))
#fdssd
def click_no():
    button_no.config(state=DISABLED)
    label.pack_forget()
    button_yes.place_forget()
    button_no.place_forget()
    label_no = Label(root, text='Круто мне больше достанется лох', font=('Arial', 15), bg='lightyellow', fg='black')
    label_no.pack(pady=80)

def click_yes():
    messagebox.showinfo('Поздравляю челик', 'Торт твой')
    root.destroy()

label = Label(root, text='Хочешь торт?', font=('Arial', 20), bg='lightgreen', fg='black')
label.pack(pady=20)

button_yes = Button(root, text='Да', bg='red', fg='white', width=5, height=2, command=click_yes)
button_no = Button(root, text='Нет', bg='green', fg='white', command=click_no, width=5, height=2)

button_yes.place(x=250, y=100)
button_no.place(x=80, y=100)

button_yes.bind('<Enter>', move_button)
#ураа сделал таск коммерческий проект
root.mainloop()
