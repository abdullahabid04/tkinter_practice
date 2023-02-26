from tkinter import *
from PIL import ImageTk, Image

win = Tk()

img = ImageTk.PhotoImage(Image.open("images/pic1.png"))

menuBar = Menu(win)

win.geometry("600x600")
win.config(bg="light blue", menu=menuBar)
win.title("Admission Form")
win.iconphoto(win, img)

Label(win, text="Check your admission elligiblity", font=("Arial", 20, "bold"),
      bg="light blue", fg="green", padx=10, pady=10, justify=CENTER).place(x=70, y=70)

programMenu = Menu(menuBar)
menuBar.add_cascade(label="Program", menu=programMenu)
programMenu.add_command(label="Engineering")
programMenu.add_command(label="Computer Science")
programMenu.add_command(label="Chemistry")
programMenu.add_command(label="Physics")

educationMenu = Menu(menuBar)
menuBar.add_cascade(label="Qualification", menu=educationMenu)
educationMenu.add_command(label="Matric")
educationMenu.add_command(label="FSc")

percentageMenu = Menu(menuBar)
menuBar.add_cascade(label="Percentage", menu=percentageMenu)
percentageMenu.add_command(label="above 50 %")
percentageMenu.add_command(label="above 60 %")
percentageMenu.add_command(label="above 70 %")
percentageMenu.add_command(label="above 80 %")
percentageMenu.add_command(label="above 90 %")

ageMenu = Menu(menuBar)
menuBar.add_cascade(label="Age", menu=ageMenu)
ageMenu.add_command(label="19")
ageMenu.add_command(label="20")
ageMenu.add_command(label="21")
ageMenu.add_command(label="22")
ageMenu.add_command(label="23")

genderMenu = Menu(menuBar)
menuBar.add_cascade(label="Gender", menu=genderMenu)
genderMenu.add_command(label="M")
genderMenu.add_command(label="F")

domicileMenu = Menu(menuBar)
menuBar.add_cascade(label="Domicile", menu=domicileMenu)
domicileMenu.add_command(label="Bahawalpur")
domicileMenu.add_command(label="non_Bahawalpur")

win.mainloop()
