from tkinter import *
from tkinter import ttk

count = 0

window = Tk()

def clicked():
    global count
    count = count + 1

    label1.configure(text = f'Button was clicked {count} times!!!')


window.title("Python Button Counter")
window.geometry('200x200')

window.resizable(False, False)

window.configure(bg='lightgray')
label = Label(window, text="Button Counter")
label.place(relx=0.5, rely=0.4,anchor=CENTER)

label_counter = Label(window, text = f'Button was clicked {count} times!!!')
label_counter.place(relx=0.5, rely=0.5,anchor=CENTER)

button = ttk.Button(window, text = "click on me", command = clicked)
button.place(relx=0.5, rely=0.6,anchor=CENTER)

window.mainloop()
