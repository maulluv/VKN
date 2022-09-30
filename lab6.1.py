import math 
a=int(input("Перший діапозон (a) "))
b=int(input("Дрегий діапозон (b) "))
h=int(input("Крок (h) "))
for x in range(a,b+h,h): 
  y= math.log(math.fabs(2 * x + 7), 5) + (x - 4) ** 1/3
  print("x=%.1f     y=%.3f"%(x,y))