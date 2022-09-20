import math 
def func1(x1,x2):     
    W=(math.sin(x1)-math.cos(x2))*4.138*math.log1p(abs(math.sin(math.pi/4+2.31*x1)))     
    return(W) 
a=float(input("Введіть a")) 
b=float(input("Введіть b"))
y=func1(a,b) 
print(y)
