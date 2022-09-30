import math 
x=float(input("Введіть х  "))
def f1(x1):
     rez= 2.31 - math.log1p(abs(x - 6))
     return(rez)
def f2(x2): 
     rez= math.cos(x + 3) + math.sin(2 * x + math.pi / 2)
     return(rez)
def f3(x3): 
     rez= 3 / x + math.pow(math.e, x) / math.pow(x, 3)
     return(rez)
y=0.0
if x > 3:
    y=f1(x)
elif 0 <= x:
    y=f2(x)
else:
    y=f3(x)
print(y)