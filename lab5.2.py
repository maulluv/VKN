num1 = int(input("Ведіть чотирицифрове число   "))
a = num1 % 10
b = num1 //10 % 10 
c = num1 //100 % 10
d = num1 //1000 % 10
minimum=min(a,b,c,d)
maximum=max(a,b,c,d)
suma=(minimum + maximum)
print(suma)