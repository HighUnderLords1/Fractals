from graphics import *
from Koch_Fractal import koch_Fractal
from Koch_Snowflake import koch_Snowflake
from Lo_Feather import lo_Feather
from Sierpinski_Triangle import sierpinski_Triangle
from Binary_Tree import binary_Tree
from src.Turtle import Turtle
from src.Button import Button
import time

def getDegree(maxDegrees):
	win = GraphWin("Degrees Amount", 400, 150)
	win.setCoords(0,0,400,150)
	t = Text(Point(200, 125), f"Please enter degrees (max: {maxDegrees}): ")
	t.draw(win)
	t.setSize(15)
	entry = Entry(Point(200, 75), 30)
	entry.draw(win)
	go = Button(win, Point(200, 35), 200, 20, "Execute")
	go.activate()
	while True and win.isOpen():
		p = win.getMouse()
		if go.clicked(p):
			win.close()
	try:
		result = int(entry.getText())
		return max(min(result, maxDegrees),0)
	except:
		return maxDegrees//2

def getAngle(maxAngle):
	win = GraphWin("Angle Amount", 400, 150)
	win.setCoords(0,0,400,150)
	t = Text(Point(200, 125), f"Please enter angle (max: {maxAngle}): ")
	t.draw(win)
	t.setSize(15)
	entry = Entry(Point(200, 75), 30)
	entry.draw(win)
	go = Button(win, Point(200, 35), 200, 20, "Execute")
	go.activate()
	while True and win.isOpen():
		p = win.getMouse()
		if go.clicked(p):
			win.close()
	try:
		result = int(entry.getText())
		return max(min(result, maxAngle),0)
	except:
		return maxAngle//2

def runAllFractals():
	running = True
	maxDegrees = 7
	degree = getDegree(maxDegrees)
	#degree = int(input(f"Enter Degree (Max {maxDegrees}): "))
	#degree = max(min(degree, maxDegrees),0)
	#degree = 6
	win1 = GraphWin(f"Lo Feather Fractal on degree {degree}", 400, 400)
	lo_Feather(win1, degree, Point(50, 50), Point(300, 300))

	win2 = GraphWin(f"Koch Fractal on degree {degree}", 400, 400)
	t1 = Turtle(win2, Point(0, 200), 0)
	koch_Fractal(win2, t1, 400, degree)

	win3 = GraphWin(f"Koch Snowflake on degree {degree}", 400, 400)
	t2 = Turtle(win3, Point(200, 200), 0)
	koch_Snowflake(win3, t2, 100, degree)

	win4 = GraphWin(f"Sierpinkski Triangle on degree {degree}", 400, 400)
	t3 = Turtle(win4, Point(200, 100), 0)
	sierpinski_Triangle(win4, 200, degree, t3)

	win5 = GraphWin(f"Binary Tree on degree {degree}", 400, 400)
	angle = getAngle(360)
	t4 = Turtle(win5, Point(200, 300), 360-90)
	binary_Tree(win5, t4, 70, degree, angle)
	
	while running:
		for win in [win1, win2, win3, win4, win5]:
			if win.checkMouse():
				running = False
	for win in [win1, win2, win3, win4, win5]:
		win.close()
if __name__ == '__main__':
	runAllFractals()
	