from src.Turtle import Turtle
from graphics import *
from math import cos, radians
from Koch_Fractal import koch_Fractal
def koch_Snowflake(win:GraphWin, turtle:Turtle, radius:int, degree:int, opposite=False):
	sideLength = 2*(radius*cos(radians(30)))

	turtle.move(0, -radius)

	turtle.turnTo(60)
	p2 = koch_Fractal(win, turtle, sideLength, degree, opposite)

	turtle.moveTo(p2)
	turtle.turn(120)
	p3 = koch_Fractal(win, turtle, sideLength, degree, opposite)

	turtle.moveTo(p3)
	turtle.turn(120)
	p1 = koch_Fractal(win, turtle, sideLength, degree, opposite)

def test():
	win = GraphWin("", 400, 400)
	t = Turtle(win, Point(0,0), 60)
	
	center = Point(200, 200)
	radius = 100
	p1 = Point(center.getX(), center.getY()-radius)
	t.moveTo(p1)
	
	centerCirc = Circle(center, 5)
	centerCirc.setFill("black")
	centerCirc.draw(win)

	#find side length
	length = 2*(radius*cos(radians(30)))
	p2 = t.draw(win, length)

	t.turn(120)
	t.moveTo(p2)
	p3 = t.draw(win, length)

	t.turn(120)
	t.moveTo(p3)
	t.draw(win, length)
	

	win.getMouse()
	win.close()
	