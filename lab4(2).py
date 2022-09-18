import math
x, y=float(input("вставте число")), float(input("вставте число 2"))
W=(math.sin(x)-math.cos(y))*4.138*math.log1p(abs(math.sin(math.pi/4+2.31*x)))
print(W)