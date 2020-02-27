from tkinter import *
from PIL import ImageTk, Image

root = Tk()
my_img = ImageTk.PhotoImage(Image.open("IMG_3918.jpg"))
label = Label(image=my_img)
label.pack()


mainloop()