import math 
x1 = int(input("Координата абсциси точки А"))
y2 = int(input("Координата ордината точки B"))
x2 = 0
y1 = 0
mn = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
os = abs(x1) * 2
print("Бічна сторона = ", mn)
print("Основа =", os )
