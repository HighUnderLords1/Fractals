from graphics import Point
def getMidpoint(p1, p2):
	x = (p1.getX()+p2.getX())/2
	y = (p1.getY()+p2.getY())/2
	return Point(x, y)