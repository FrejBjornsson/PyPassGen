# importing Libraries
from tkinter import *
import random
import string
from tkinter import Tk
import pyperclip

# initialize window
root: Tk = Tk()
root.geometry("310x200")
root.configure(bg='black')
root.resizable(0, 0)
root.title("FrejSoftware - PyPassGen")
root.iconbitmap('C:/Users/frejb/Desktop/PyPassGen/iconkey.ico')

# heading
heading = Label(root, text='P A S S W O R D\nG E N E R A T O R', fg='green', bg='black',
                font=("gothic", 15, "bold")).pack(side=TOP, pady=5)

# select password length
pass_label = Label(root, text='PASSWORD LENGTH').pack(pady=5)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=2).pack()

# define function
pass_str = StringVar()


def PassGen():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# button
Button(root, text="GENERATE PASSWORD", command=PassGen).pack(pady=5)
Entry(root, textvariable=pass_str, width=38).pack()


# function to copy
def Copy_pass():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_pass).pack(pady=5)


# function to clear
def Clear_pass():
    pyperclip.determine_clipboard()


# loop to run program
root.mainloop()
