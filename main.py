from tkinter import *
import random

root = Tk()
root.title('Just_code')
root.geometry('300x250')

def click_yes():
    button_yes.config(state=DISABLED)
    button_yes.place(x=random.randint(0, 250), y=random.randint(0, 200))

def click_no():
    button_no.config(state=DISABLED)
    label.pack_forget()
    button_yes.place_forget()
    button_no.place_forget()
    label_no = Label(root, text='Круто мне больше достанется', font=('Arial', 15), bg='light yellow', fg='black')
    label_no.pack()

label = Label(root, text='Хочешь торт?', font=('Arial', 20), bg='light green')
label.pack(pady=20)

button_yes = Button(root, text='Да', bg='red', command=click_yes, width=3, height=1)
button_no = Button(root, text='Нет', bg='green', command=click_no, width=3, height=1)

button_yes.place(x=200, y=80)
button_no.place(x=80, y=80)

if __name__ == '__main__':
    root.mainloop()
