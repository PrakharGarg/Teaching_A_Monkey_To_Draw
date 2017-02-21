import turtle as T
import canvasvg
import os
from random import randint

T.speed(0)

T.setup(width=100, height=100, startx=50, starty=50)
T.forward(60)
T.left(90)
T.forward(60)
T.left(90)
T.forward(60)
T.left(90)
T.forward(60)
T.left(90)

T.hideturtle()
ts = T.getscreen().getcanvas()
canvasvg.saveall("image.svg",ts)
T.clear()
script = "convert -size 100x100 image.svg images/square_1.png"

os.system(script)
os.system("rm image.svg")
