from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


win = Tk()

img = ImageTk.PhotoImage(Image.open("images/pic1.png"))

win.geometry("600x600")
win.config(bg="light blue")
win.title("Admission Form")
win.iconphoto(win, img)

noteBook = ttk.Notebook(win)

win1 = Frame(noteBook, bg="light blue")
win2 = Frame(noteBook, bg="light blue")
win3 = Frame(noteBook, bg="light blue")

noteBook.add(win1, text="Admission Form")
noteBook.pack(expand=True, fill="both")

programs = ["Engineering", "Computer Science", "Physics", "Chemistry"]
educations = ["Matric", "FSc"]
percentages = [50, 60, 70, 80, 90]
ages = [18, 19, 20, 21, 22, 23, 24]
genders = ["Male", "Female"]
domiciles = ["Bahawalpur", "Non-Bahawalpur"]

data = []

engRequirements = ["FSc", 80, 20, 23, "Bahawalpur"]
csRequirements = ["Matric", 60, 18, 20, "Bahawalpur"]
phyRequirements = ["FSc", 70, 20, 22, "Bahawalpur"]
cheRequirements = ["Matric", 80, 19, 21, "Bahawalpur"]

Password = "1234"


def submitname():
    name = Name.get()
    data.append(name)


def submitprogram():
    program = listbox1.get(listbox1.curselection())
    data.append(program)


def submiteducation():
    education = listbox2.get(listbox2.curselection())
    data.append(education)


def submitpercentage():
    percentage = listbox3.get(listbox3.curselection())
    data.append(percentage)


def submitage():
    age = listbox4.get(listbox4.curselection())
    data.append(age)


def submitgender():
    gender = listbox5.get(listbox5.curselection())
    data.append(gender)


def submitdomicile():
    domicile = listbox6.get(listbox6.curselection())
    data.append(domicile)


def label(txt1, txt2, color):
    global lb1
    global lb2
    global lb3
    global lb4
    global lb5

    lb1 = Label(win1, text=txt1, font=("Arial", 15, "bold"),
                fg=color, bg="light blue")
    lb1.place(x=450, y=150)
    lb2 = Label(win1, text=txt2, font=("Arial", 15, "bold"),
                fg=color, bg="light blue")
    lb2.place(x=475, y=200)
    lb3 = Label(win1, text="elligible", font=("Arial", 15, "bold"),
                fg=color, bg="light blue")
    lb3.place(x=475, y=250)
    lb4 = Label(win1, text="for this", font=("Arial", 15, "bold"),
                fg=color, bg="light blue")
    lb4.place(x=475, y=300)
    lb5 = Label(win1, text="program", font=("Arial", 15, "bold"),
                fg=color, bg="light blue")
    lb5.place(x=475, y=350)


def done():
    try:
        if data[1] == "Engineering":
            if data[2] == engRequirements[0] and data[3] > int(engRequirements[1]) and (
                    int(engRequirements[2]) < data[4] < int(engRequirements[3])) and data[6] == engRequirements[4]:
                label("Congratulations", "You are", "green")
            else:
                label("We are sorry", "You are not", "red")

        elif data[1] == "Computer Science":
            if data[2] == csRequirements[0] and data[3] > int(csRequirements[1]) and (
                    int(csRequirements[2]) <= data[4] < int(csRequirements[3])) and data[6] == csRequirements[4]:
                label("Congratulations", "You are", "green")
            else:
                label("We are sorry", "You are not", "red")

        elif data[1] == "Physics":
            if data[2] == phyRequirements[0] and data[3] > int(phyRequirements[1]) and (
                    int(phyRequirements[2]) <= data[4] < int(phyRequirements[3])) and data[6] == phyRequirements[4]:
                label("Congratulations", "You are", "green")
            else:
                label("We are sorry", "You are not", "red")

        elif data[1] == "Chemistry":
            if data[2] == cheRequirements[0] and data[3] > int(cheRequirements[1]) and (
                    int(cheRequirements[2]) <= data[4] < int(cheRequirements[3])) and data[6] == cheRequirements[4]:
                label("Congratulations", "You are", "green")
            else:
                label("We are sorry", "You are not", "red")
    except IndexError as error:
        print(error)


def login():
    noteBook.add(win2, text="Ädministrator login")
    noteBook.hide(win1)


def settingswin():
    noteBook.add(win3, text="Settings")
    noteBook.hide(win2)


def submit():
    if password.get() == Password:
        acceptLabel = Label(win2, text="Access accepted", font=("Arial", 15, "bold"),
                            fg="green", bg="light blue")
        acceptLabel.place(x=200, y=350)

        settingswin()
    else:
        denyLabel = Label(win2, text="Access denied", font=("Arial", 15, "bold"),
                          fg="red", bg="light blue")
        denyLabel.place(x=200, y=350)


def submitdata():
    engRequirements[0] = engeducation.get()
    engRequirements[1] = engpercentage.get()
    engRequirements[2] = englowage.get()
    engRequirements[3] = engupage.get()
    engRequirements[4] = engdomicile.get()

    csRequirements[0] = cseducation.get()
    csRequirements[1] = cspercentage.get()
    csRequirements[2] = cslowage.get()
    csRequirements[3] = csupage.get()
    csRequirements[4] = csdomicile.get()

    phyRequirements[0] = phyeducation.get()
    phyRequirements[1] = phypercentage.get()
    phyRequirements[2] = phylowage.get()
    phyRequirements[3] = phyupage.get()
    phyRequirements[4] = phydomicile.get()

    cheRequirements[0] = cheeducation.get()
    cheRequirements[1] = chepercentage.get()
    cheRequirements[2] = chelowage.get()
    cheRequirements[3] = cheupage.get()
    cheRequirements[4] = chedomicile.get()

    noteBook.add(win1, text="Admission Form")
    noteBook.hide(win3)


def reset():
    lb1.destroy()
    lb2.destroy()
    lb3.destroy()
    lb4.destroy()
    lb5.destroy()

    Name.delete(0, END)
    data.clear()


Label(win1, text="Check your admission elligiblity", font=("Arial", 20, "italic"),
      bg="light blue", fg="green", padx=5, pady=5, justify=CENTER).place(x=110, y=20)
Label(win1, text="Enter your Name", font=("Arial", 10, "bold"), fg="black", bg="light blue"
      ).place(x=60, y=97)

Name = Entry(win1, fg="blue", bg="light blue", width=30)
Name.place(x=190, y=100)

listbox1 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)
listbox2 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)
listbox3 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)
listbox4 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)
listbox5 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)
listbox6 = Listbox(win1, fg="blue", bg="light green", selectmode=SINGLE)

listBoxes = [listbox1, listbox2, listbox3, listbox4, listbox5, listbox6]
xCoordsListBoxes = [50, 180, 310, 50, 180, 310]
yCoordsListBoxes = [160, 160, 160, 310, 310, 310]

for i in range(6):
    listBoxes[i].place(x=xCoordsListBoxes[i], y=yCoordsListBoxes[i])

for i in range(len(programs)):
    listbox1.insert(i, programs[i])
listbox1.config(height=4, width=20)
for i in range(len(educations)):
    listbox2.insert(i, educations[i])
listbox2.config(height=4, width=20)
for i in range(len(percentages)):
    listbox3.insert(i, percentages[i])
listbox3.config(height=4, width=20)
for i in range(len(ages)):
    listbox4.insert(i, ages[i])
listbox4.config(height=4, width=20)
for i in range(len(genders)):
    listbox5.insert(i, genders[i])
listbox5.config(height=4, width=20)
for i in range(len(domiciles)):
    listbox6.insert(i, domiciles[i])
listbox6.config(height=4, width=20)

textsOfLabels = ["Program", "Qualification", "Percentage", "Age", "Gender", "Domicile"]
xCoordsOfLabels = [60, 182, 313, 75, 195, 320]
yCoordsOfLabels = [135, 135, 135, 280, 280, 280]

for i in range(6):
    Label(win1, text=f'Choose {textsOfLabels[i]}', font=("Arial", 9, "bold"), fg="black", bg="light blue"
          ).place(x=xCoordsOfLabels[i], y=yCoordsOfLabels[i])

functionsOfButtons = [submitname, submitprogram, submiteducation, submitpercentage, submitage, submitgender,
                      submitdomicile, done, login, reset, win.quit]
textsOfButtons = ["Submit", "Submit", "Submit", "Submit", "Submit", "Submit", "Submit", "done", "Administrator login",
                  "reset", "quit"]
xCoordsOfButtons = [383, 90, 220, 350, 90, 220, 350, 225, 0, 150, 300]
yCoordsOfButtons = [97, 240, 240, 240, 390, 390, 390, 450, 0, 450, 450]

for i in range(11):
    Button(win1, text=textsOfButtons[i], fg="black", bg="silver", activeforeground="black",
           activebackground="silver", padx=3, pady=1, command=functionsOfButtons[i]
           ).place(x=xCoordsOfButtons[i], y=yCoordsOfButtons[i])

Label(win2, text="Enter your e-mail : ", font=("Arial", 10, "bold"), fg="black",
      bg="light blue").place(x=100, y=200)
Entry(win2, fg="blue", bg="light blue", width=30).place(x=250, y=203)
Label(win2, text="Enter your password : ", font=("Arial", 10, "bold"), fg="black",
      bg="light blue").place(x=100, y=250)
password = Entry(win2, fg="blue", bg="light blue", width=30)
password.place(x=250, y=253)

Button(win2, text="Submit", fg="black", bg="silver", activeforeground="black",
       activebackground="silver", padx=3, pady=1, command=submit).place(x=250, y=300)
Button(win3, text="Submit", fg="black", bg="silver", activeforeground="black",
       activebackground="silver", padx=3, pady=1, command=submitdata).place(x=250, y=500)

textOfLabels1 = ["Engineering", "Computer Scirnce", "Physics", "Chemistry", "Education", "Percentage", "Lower age",
                 "Upper age", "Domicile"]
xCoordsOfLabels1 = [10, 10, 10, 10, 150, 240, 330, 420, 510]
yCoordsOfLabels1 = [100, 200, 300, 400, 50, 50, 50, 50, 50]

for i in range(9):
    Label(win3, text=textOfLabels1[i], font=("Arial", 10, "bold"), fg="black",
          bg="light blue").place(x=xCoordsOfLabels1[i], y=yCoordsOfLabels1[i])

engeducation = Entry(win3, fg="blue", bg="light blue", width=10)
engpercentage = Entry(win3, fg="blue", bg="light blue", width=10)
englowage = Entry(win3, fg="blue", bg="light blue", width=10)
engupage = Entry(win3, fg="blue", bg="light blue", width=10)
engdomicile = Entry(win3, fg="blue", bg="light blue", width=14)

cseducation = Entry(win3, fg="blue", bg="light blue", width=10)
cspercentage = Entry(win3, fg="blue", bg="light blue", width=10)
cslowage = Entry(win3, fg="blue", bg="light blue", width=10)
csupage = Entry(win3, fg="blue", bg="light blue", width=10)
csdomicile = Entry(win3, fg="blue", bg="light blue", width=14)

phyeducation = Entry(win3, fg="blue", bg="light blue", width=10)
phypercentage = Entry(win3, fg="blue", bg="light blue", width=10)
phylowage = Entry(win3, fg="blue", bg="light blue", width=10)
phyupage = Entry(win3, fg="blue", bg="light blue", width=10)
phydomicile = Entry(win3, fg="blue", bg="light blue", width=14)

cheeducation = Entry(win3, fg="blue", bg="light blue", width=10)
chepercentage = Entry(win3, fg="blue", bg="light blue", width=10)
chelowage = Entry(win3, fg="blue", bg="light blue", width=10)
cheupage = Entry(win3, fg="blue", bg="light blue", width=10)
chedomicile = Entry(win3, fg="blue", bg="light blue", width=14)

engeducation.place(x=150, y=100)
engpercentage.place(x=240, y=100)
englowage.place(x=330, y=100)
engupage.place(x=420, y=100)
engdomicile.place(x=505, y=100)

cseducation.place(x=150, y=200)
cspercentage.place(x=240, y=200)
cslowage.place(x=330, y=200)
csupage.place(x=420, y=200)
csdomicile.place(x=505, y=200)

phyeducation.place(x=150, y=300)
phypercentage.place(x=240, y=300)
phylowage.place(x=330, y=300)
phyupage.place(x=420, y=300)
phydomicile.place(x=505, y=300)

cheeducation.place(x=150, y=400)
chepercentage.place(x=240, y=400)
chelowage.place(x=330, y=400)
cheupage.place(x=420, y=400)
chedomicile.place(x=505, y=400)

engeducation.insert(0, "FSc")
engpercentage.insert(0, "80")
englowage.insert(0, "20")
engupage.insert(0, "23")
engdomicile.insert(0, "Bahawalpur")

cseducation.insert(0, "Matric")
cspercentage.insert(0, "50")
cslowage.insert(0, "18")
csupage.insert(0, "20")
csdomicile.insert(0, "Bahawalpur")

phyeducation.insert(0, "FSc")
phypercentage.insert(0, "70")
phylowage.insert(0, "19")
phyupage.insert(0, "22")
phydomicile.insert(0, "Bahawalpur")

cheeducation.insert(0, "Matric")
chepercentage.insert(0, "60")
chelowage.insert(0, "20")
cheupage.insert(0, "22")
chedomicile.insert(0, "Bahawalpur")

win1.mainloop()
