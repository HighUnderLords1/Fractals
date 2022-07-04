from src.Turtle import Turtle
def koch_Fractal(win, turtle:Turtle, length, degree, opposite=False):
	if degree == 0:
		p = turtle.draw(win, length)
		return p
	else:
		length1 = length/3
		degree1 = degree-1
		turnChange = 1
		if opposite:
			turnChange = -1
		p2 = koch_Fractal(win, turtle, length1, degree1)
		turtle.turn(-60*turnChange)
		turtle.moveTo(p2)
		p3 = koch_Fractal(win, turtle, length1, degree1)
		turtle.turn(120*turnChange)
		turtle.moveTo(p3)
		p4 = koch_Fractal(win, turtle, length1, degree1)
		turtle.moveTo(p4)
		turtle.turn(-60*turnChange)
		p5 = koch_Fractal(win, turtle, length1, degree1)
		turtle.moveTo(p5)
		return p5