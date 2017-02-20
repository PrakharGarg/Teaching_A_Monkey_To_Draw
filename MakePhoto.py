import turtle as T
import canvasvg
import os

T.setup(width=500, height=500, startx=0, starty=0)
T.forward(90)
T.left(90)
T.forward(90)
T.left(90)
T.forward(90)
T.left(90)
T.forward(90)
T.left(90)

T.hideturtle()
ts = T.getscreen().getcanvas()
canvasvg.saveall("image.svg",ts)

os.system("convert -size 500x500 image.svg square_1.png")