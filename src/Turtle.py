from math import sin, cos, radians, degrees
from graphics import GraphWin, Point, Line, Circle
class Turtle:

	def main():
		win = GraphWin("Turtle Test", 500, 500)
		length = 400/3
		a = Point(50, 250)
		t = Turtle(a, 0)
		b = t.draw(win, length)
		t.moveTo(b)
		t.turn(-60)
		c = t.draw(win, length)
		t.moveTo(c)
		t.turn(120)
		d = t.draw(win, length)
		t.moveTo(d)
		t.turn(-60)
		e = t.draw(win, length)
		t.moveTo(e)
		
		
	
	def __init__(self, win:GraphWin, location:Point, direction:float):
		self.win = win
		self.location = location
		self.direction = radians(direction)

		while self.direction < 0:
			self.direction+=360

		while self.direction >= 360:
			self.direction-=360

	def moveTo(self, point:Point):
		dx = point.getX()-self.location.getX()
		dy = point.getY()-self.location.getY()
		self.location = point

	def move(self, dx, dy):
		self.location = Point(self.location.getX()+dx, self.location.getY()+dy)

	def draw(self, win:GraphWin, length):
		dx = length * cos(self.direction)
		dy = length * sin(self.direction)
		p2 = Point(self.location.getX()+dx, self.location.getY()+dy)
		self.line = Line(self.location, p2)
		self.line.draw(win)
		return p2

	def calcDraw(self, length):
		dx = length * cos(self.direction)
		dy = length * sin(self.direction)
		p2 = Point(self.location.getX()+dx, self.location.getY()+dy)
		return p2

	def turn(self, degreesToChange:float):
		self.direction+=radians(degreesToChange)
		
		while degrees(self.direction) < 0:
			self.direction+=radians(360)

		while degrees(self.direction) >= 360:
			self.direction-=radians(360)

	def turnTo(self, absDegrees:float):
		self.direction = radians(absDegrees)
		
		while degrees(self.direction) < 0:
			self.direction+=radians(360)

		while degrees(self.direction) >= 360:
			self.direction-=radians(360)

	def clone(self):
		return Turtle(self.win, self.location.clone(), degrees(self.direction))
