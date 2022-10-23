import math 
x = float ( input( "Перший діапазон (а)"))
b = float ( input( "Другий діапазон (а)"))
h = float ( input( "Крок (h) "))
while x<=b: 
		y= math.log(math.fabs(2 * x + 7), 5) + (x - 4) ** 1/3
		print("x=%.1f     y=%.3f"%(x,y))