from graphics import Point, GraphWin, Line
from src.getMidpoint import getMidpoint
def lo_Feather(win:GraphWin, level:int, a:Point, b:Point):
	if level == 0:
		Line(a,b).draw(win)
	else:
		level -= 1
		c = getMidpoint(a,b)
		xD = a.getX() + (c.getX() - a.getX()) / 2 - (c.getY() - a.getY()) / 2
		yD = a.getY() + (c.getY() - a.getY()) / 2 + (c.getX() - a.getX()) / 2
		d = Point(xD, yD)
		lo_Feather(win, level, d, a)
		lo_Feather(win, level, d, b)
		lo_Feather(win, level, d, c)