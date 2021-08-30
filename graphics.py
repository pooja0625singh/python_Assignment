from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("This is Title")
root.geometry("400x300")
def btn_click():
    messagebox.showinfo("Message", "Button Clicked")

button = Button(root, text="Click Me", bg = "red", font=("Times New Roman", 25), command=btn_click)
button.place(relx="0.5", rely="0.5", anchor=CENTER)

root.mainloop()