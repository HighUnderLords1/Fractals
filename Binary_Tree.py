from graphics import GraphWin
from src.Turtle import Turtle
def binary_Tree(win:GraphWin, turtle:Turtle, length:float, degree:int, angle:float):
	if degree == 0:
		p = turtle.draw(win, length)
		return p
	else:
		degree -= 1

		turtle = turtle.clone()
		p = turtle.draw(win, length)
		turtle.moveTo(p)
		
		turtle.turn(angle)
	
		p = binary_Tree(win, turtle, length*0.8, degree, angle)
	
		turtle.turn(-(angle*2))
	
		p = binary_Tree(win, turtle, length*0.8, degree, angle)
	
		return p