import math 
x = float(input("Введіть х  "))
a = math.e ** (0.9 * x + 4) + (x + 2 * x **2) **1/4
b = 61 * (abs(x + 2) + 1)
c = 9*math.cos(0.7 * x + math.sqrt(x))
print("Значення функції дорівнює", a/b-c)