import math
import random
s=int(input("найменше значення х = "))
d=int(input("найбільше значення х = "))
spisok=[]
def f():
    a=math.log(abs(2*x+7))+pow(x,1/3)-pow(x,1/3)
    spisok.append(a)
for x in range(s,d):
    f()
random.shuffle(spisok)
print(spisok)

