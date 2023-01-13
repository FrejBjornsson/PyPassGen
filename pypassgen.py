# importing Libraries
import random
import string
import pyperclip
from tkinter import *

import customtkinter
from customtkinter import *


# Set theme of app
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# initialize window
root = customtkinter.CTk()
root.geometry("400x500")
root.resizable(FALSE, FALSE)
root.title("PyPassGen 1.0.0")
root.iconbitmap(bitmap='iconkey.ico')

# Frame for app
frame = customtkinter.CTkFrame(master=root, corner_radius=20)
frame.pack(pady=20, padx=60, fill="both", expand=True)


# heading
heading_label = customtkinter.CTkLabel(master=frame, text='PyPassGen Password Generator')
heading_label.pack(pady=12, padx=10)

# select password length
pass_length_label = customtkinter.CTkLabel(master=frame, text='PASSWORD LENGTH')
pass_length_label.pack(pady=12, padx=10)

pass_len = IntVar()
pass_length_spinbox = Spinbox(master=frame, from_=8, to=32, textvariable=pass_len)
pass_length_spinbox.pack(pady=12, padx=10)

# define function
pass_str = StringVar()


def pass_gen():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# button
generate_pass_button = customtkinter.CTkButton(master=frame, text="GENERATE PASSWORD", command=pass_gen)

generate_pass_button.pack(pady=12, padx=10)

pass_input = customtkinter.CTkEntry(master=frame,  textvariable=pass_str)
pass_input.pack(pady=12, padx=10)


# function to copy
def copy_pass():
    pyperclip.copy(pass_str.get())


copy_pass_btn = customtkinter.CTkButton(master=frame, text='COPY TO CLIPBOARD', command=copy_pass)

copy_pass_btn.pack(pady=12, padx=10)


# function to clear
def clear_pass():
    pass_input.delete(0, 'end')


clear_pass_btn = customtkinter.CTkButton(master=frame, text='CLEAR PASSWORD', command=clear_pass)
clear_pass_btn.pack(pady=12, padx=10)

# loop to run program
root.mainloop()
