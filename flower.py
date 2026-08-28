from turtle import *

setup (700,720)
bgcolor("blue")
pu()
setpos(170,70)
pd()
width (4)
speed (0)

R = 1
G = 1
B = 0

for i in range (150):
    begin_fill()
    circle(140 - i,50)
    lt(80)
    circle (130 -i, 50)
    rt(150)

    R -=0.0065
    G -=0.0065

    end_fill()

done()