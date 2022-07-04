from graphics import GraphWin, Point, Circle
from src.Turtle import Turtle
from math import cos, radians

def make_equilateral_triangle(win:GraphWin, turtle:Turtle, sideLength:float):
	turtle.turnTo(60)
	p2 = turtle.draw(win, sideLength)
	turtle.turn(120)
	turtle.moveTo(p2)
	p3 = turtle.draw(win, sideLength)
	turtle.turn(120)
	turtle.moveTo(p3)
	p1 = turtle.draw(win, sideLength)
	turtle.moveTo(p1)
	
	return p1, p2, p3, turtle

def sierpinski_Triangle(win:GraphWin, sideLength:float, degree:int, turtle:Turtle):
	if degree == 0:
		return make_equilateral_triangle(win, turtle, sideLength)
	else:
		degree-=1
		sideLength/=2

		p1, p2, p3, turtle = sierpinski_Triangle(win, sideLength, degree, turtle)
		turtle.moveTo(p2)
		_, p2, _, turtle = sierpinski_Triangle(win, sideLength, degree, turtle)
		turtle.moveTo(p3)
		_, _, p3, turtle = sierpinski_Triangle(win, sideLength, degree, turtle)
		
		return p1, p2, p3, turtle
		