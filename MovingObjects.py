from tkinter import *
import time

win = Tk()

win.config(bg="white")

WIDTH = 800
HEIGHT = 800

canvas = Canvas(win, width=WIDTH, height=HEIGHT)
canvas.config(bg="white")
canvas.pack()


class Ball:
    def __init__(self, canvas, x, y, diameter, ballx, bally, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.ballx = ballx
        self.bally = bally

    def move_ball(self):
        coordinates = self.canvas.coords(self.image)

        if (coordinates[2] >= self.canvas.winfo_width()) or (coordinates[0] < 0):
            self.ballx = -self.ballx

        if (coordinates[3] >= self.canvas.winfo_height()) or (coordinates[1] < 0):
            self.bally = -self.bally

        self.canvas.move(self.image, self.ballx, self.bally)


ball1 = Ball(canvas, 100, 100, 50, 1, 10, "Blue")
ball2 = Ball(canvas, 125, 125, 50, 2, 9, "Green")
ball3 = Ball(canvas, 150, 150, 50, 3, 8, "Red")
ball4 = Ball(canvas, 175, 175, 50, 4, 7, "Yellow")
ball5 = Ball(canvas, 200, 200, 50, 5, 6, "Black")
ball6 = Ball(canvas, 100, 100, 50, 6, 5, "Grey")
ball7 = Ball(canvas, 125, 125, 50, 7, 4, "Orange")
ball8 = Ball(canvas, 150, 150, 50, 8, 3, "Pink")
ball9 = Ball(canvas, 175, 175, 50, 9, 2, "Purple")
ball10 = Ball(canvas, 200, 200, 50, 10, 1, "Brown")

list_of_balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10]

while True:
    for i in range(len(list_of_balls)):
        list_of_balls[i].move_ball()

    win.update()

    time.sleep(0.01)

win.mainloop()
