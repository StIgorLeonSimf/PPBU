from turtle import *


colormode(255)
shape('turtle')
speed(0)

r = 255
g = 255
b = 0
br = 0
bg = 255
bb = 0
color((br, bg, bb), (r, g, b))
pensize(4)

for j in range(150, 10, -25):
    # fillcolor((r, g, b))
    color((br, bg, bb), (r, g, b))
    for i in range(8):
        # fillcolor()
        begin_fill()
        circle(j)
        end_fill()
        rt(45)
    r -= 30
    g -= 15
    b += 30
    br += 30
    bg -= 30
    bb += 30

mainloop()