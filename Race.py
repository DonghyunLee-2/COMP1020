#By Donghyun Lee (u1538647)
from graphics import GraphWin, Line, Image, Point, update
from Dice import Dice
import time
import random


class Horse:
    def __init__(self, speed, y_pos, image_file, window):
        self.x_pos = 50
        self.y_pos = y_pos
        self.image = Image(Point(self.x_pos, self.y_pos), image_file)
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        move_distance = self.dice.roll()
        self.image.move(move_distance, 0)
        self.x_pos += move_distance

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x


def main():
    win = GraphWin("Horse Race", 700, 350)
    win.setBackground('lightblue')

    horse1_image = "Horse_Pink.png"
    horse2_image = "Horse_Green.png"

    horse1 = Horse(random.randint(3,6), 100, horse1_image, win)
    horse2 = Horse(random.randint(3,6), 200, horse2_image, win)

    horse1.draw()
    horse2.draw()

    finish_line = Line(Point(600, 0), Point(600, 350))
    finish_line.setWidth(4)
    finish_line.setOutline("black")
    finish_line.draw(win)

    win.getMouse()

    race_over = False
    while not race_over:
        horse1.move()
        horse2.move()
        update(10)
        time.sleep(0.1)

        if horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600):
            print("Its a tie!")
            race_over = True
        elif horse1.crossed_finish_line(600):
            print("Horse 1 is the winner!")
            print("Congratulations!")
            race_over = True
        elif horse2.crossed_finish_line(600):
            print("Horse 2 is the winner!")
            print("Congratulations!")
            race_over = True

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()