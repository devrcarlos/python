
#teste

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()

photo = PhotoImage(file='teste_gif.gif').subsample(5)

img = Label(master=root, image=photo)
img.pack(side=TOP)

text = Label(master=root, font=('Courier', 18), text='Olá world!')
text.pack(side=BOTTOM)

img.pack()

root.mainloop()