'''
A Python script that draws the Singapore flag centred at origin following the
technical specifications given by:
https://en.wikipedia.org/wiki/File:Construction_Sheet_of_the_Flag_of_Singapore.svg
'''
from turtle import *

setup(width = 1.0, height = 1.0)
title("Singapore Flag")
t = Turtle()
bgcolor("black")
t.speed(10)

SCALER = 15
########## CONSTANTS BASED ON TECHNICAL SPECIFICATIONS; DON'T MODIFY ###########
UNIT = 18
RED = "#EE2536"
CRESCENT_RADIUS = 3 + 7.25 / 2
CRESCENT_LEFT_OFFSET = 4.78 + CRESCENT_RADIUS 
CRESCENT_TOP_OFFSET = (18 - 13.25) / 2
STAR_CENTRE_OFFSET = 4.78 + 3 + 7.25
STAR_SEP_ANGLE = 72
STAR_RADIUS = 7.6 / 2
STAR_HEIGHT = 3.45
VERTICES = 5
ANGLE = 360 / VERTICES
INT_ANGLE = 180 - 2 * ANGLE
CIRCLE_SEP = 3
################################################################################
def draw_rect(length, height, pen_colour=None, fill_colour=None, top_left=None):
    if top_left:
        t.pu()
        t.goto(top_left)
    if pen_colour:
        t.pencolor(pen_colour)
    if fill_colour:
        t.fillcolor(fill_colour)
        t.begin_fill()
    t.pd()
    for _ in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(height)
        t.rt(90)
    if fill_colour:
        t.end_fill()
    t.pu()

def draw_star(height, centre=None, fill=None):
    t.pu()
    if centre:
        t.goto(centre)
    t.seth(90)
    t.fd(height / 2)
    t.seth(270)
    t.lt(INT_ANGLE / 2)
    t.pd()
    if fill:
        t.begin_fill() 
    for _ in range(VERTICES):
        t.fd(height)
        t.rt(2 * ANGLE)
        # t.dot()
    if fill:
        t.end_fill()
    t.pu()

def draw_circle(radius, pen_colour=None, fill_colour=None, start=None):
    if start:
        t.pu()
        t.goto(start)
    if pen_colour:
        t.pencolor(pen_colour)
    if fill_colour:
        t.fillcolor(fill_colour)
        t.begin_fill()
    t.pd()
    t.circle(radius)
    if fill_colour:
        t.end_fill()
    t.pu()

def draw_crescent(radius, offset, bg_colour=None, pen_colour=None, fill_colour=None, start=None):
    if start:
        t.pu()
        t.goto(start)
    draw_circle(radius, pen_colour, fill_colour)
    t.fd(offset)
    if not bg_colour:
        draw_circle(radius, bgcolor(), bgcolor())
    else:
        draw_circle(radius, bg_colour, bg_colour)

#top half
draw_rect(UNIT * SCALER * 3, UNIT * SCALER, RED, RED, (-1.5 * UNIT * SCALER, UNIT * SCALER))
#bottom half
draw_rect(UNIT * SCALER * 3, UNIT * SCALER, "white", "white", (-1.5 * UNIT * SCALER, 0))
#white crescent: white circle & red circle with horizontal offset
t.goto((-1.5 * UNIT + CRESCENT_LEFT_OFFSET) * SCALER, (UNIT - CRESCENT_TOP_OFFSET) * SCALER)
t.rt(180)
draw_crescent(CRESCENT_RADIUS * SCALER, -CIRCLE_SEP * SCALER, RED, "white", "white")
#stars
t.goto((-1.5 * UNIT + STAR_CENTRE_OFFSET) * SCALER, UNIT * SCALER / 2)
STAR_CENTRE = t.pos()
t.seth(90)
for i in range(5):
    t.seth(90)
    t.rt(i * STAR_SEP_ANGLE)
    t.fd(STAR_RADIUS * SCALER)
    t.color("white")
    draw_star(STAR_HEIGHT * SCALER, None, True)
    t.goto(STAR_CENTRE)
t.ht()
done()
