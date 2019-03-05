#Import turtle
from turtle import *

#Useful Constants
diameter = 250
radius = diameter // 2

#Set up canvas
setup()
title('pacman')
bgcolor('grey')

#set up pen for drawing
pendown()
width(6)
penup()

#draw pacmans head
pendown()
fillcolor('yellow')
begin_fill()
left(30)
forward(radius)
left(90)
circle(radius, extent = 300)
end_fill()
home()

#pacman eye
left(90)
penup()
forward(diameter //4)
dot((diameter // 3), 'blue')
dot((diameter // 5), 'black')
penup()
forward (20)
left (90)
forward (20)
pendown
dot ((diameter // 9), 'white')
#exit
hideturtle()
done()


