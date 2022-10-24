import math 
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
x=a
while a<=x<=b:
    y=math.log(abs(2*x+7))+pow(x,1/3)-pow(x,1/3)
    print(x,y)
    x=x+h
    

