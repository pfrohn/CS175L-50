'''
Pat Frohn
CS-175L
Turtle Assignment
2/14/22
'''


import math
import turtle

#named constants

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

#size the window

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


x = LENGTH / math.sqrt(2)
diameter = LENGTH + (2 * x)

#initialize the turtle

shells = turtle.Turtle()
shells.fillcolor('blue')
shells.color('red')
shells.shape('turtle')
shells.penup()
shells.goto(-50,125)
shells.pendown()

#draw the octogon
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.forward(LENGTH)
shells.right(45)
shells.penup()
shells.goto(-30,-15)
shells.pendown()
shells.write('Stop', font=('Arial', 24))
shells.penup()
shells.goto(-50,125)




