import turtle as T
import canvasvg
import os
from random import randint

def make_photo(index):
    T.speed(0)

    T.setup(width=100, height=100, startx=0, starty=0)
    for x in range(4) :
        # print(T.xcor())
        coord = (randint(-50,50), randint(-50,50))
        # print(coord)
        T.goto(coord)

    T.hideturtle()
    ts = T.getscreen().getcanvas()
    canvasvg.saveall("image.svg",ts)
    T.clear()
    script = "convert -size 100x100 image.svg images/square_" + str(index)  + ".png"

    os.system(script)
    os.system("rm image.svg")
