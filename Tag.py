from tkinter import *
from time import sleep
# region "Variables"
HEIGHT = 600
WIDTH = 800
window = Tk()
window.title("Test Environment")
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()
# endregion


class Sprite:
    def __init__(self, colour, x1, y1, x2, y2):
        self.colour = colour
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.sprite = c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.colour)
        self.SPEED = 10
        c.bind_all('<Key>', self.move)

        self.coordinates = c.coords(self.sprite)
        self.x1, self.y1, self.x2, self.y2 = self.coordinates
        self.moving = False

    def get_coords(self):
        self.coordinates = c.coords(self.sprite)
        self.x1, self.y1, self.x2, self.y2 = self.coordinates

    # region "Movement Logic"
    def up(self):
        self.get_coords()
        while self.y1 >= 5:
            self.get_coords()
            if self.y1 <= 5:
                break
            else:
                sleep(0.1)
                c.move(self.sprite, 0, -self.SPEED)
                window.update()

    def down(self):
        self.get_coords()
        while self.y2 <= 595:
            self.get_coords()
            if self.y2 >= 595:
                break
            else:
                sleep(0.1)
                c.move(self.sprite, 0, self.SPEED)
                window.update()

    def left(self):
        self.get_coords()
        while self.x1 >= 5:
            self.get_coords()
            if self.x1 <= 5:
                break
            else:
                sleep(0.1)
                c.move(self.sprite, -self.SPEED, 0)
                window.update()

    def right(self):
        self.get_coords()
        while self.x2 <= 795:
            self.get_coords()
            if self.x2 >= 795:
                break
            else:
                sleep(0.1)
                c.move(self.sprite, self.SPEED, 0)
                window.update()
    # endregion


class Player(Sprite):
    def move(self, event):
        if event.keysym == "Up":
            self.up()

        elif event.keysym == "Down":
            self.down()

        elif event.keysym == "Left":
            self.left()

        elif event.keysym == "Right":
            self.right()


pac = Player("Red", 5, 5, 25, 25)

window.mainloop()
