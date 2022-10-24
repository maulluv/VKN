a=float(input("введіть чотирьохзначне число "))
s=float(a%10)
d=float((a%100-s)/10)
f=float((a%1000-a%100)/100)
g=float((a-a%1000)/1000)
if s>=d and s>=f and s>=g:
    h=s
if s<=d and d>=f and d>=g:
    h=d
if f>=d and s<=f and f>=g:
    h=f
if g>=d and g>=f and s<=g:
    h=g

if s<=d and s<=f and s<=g:
    j=s
if s>=d and d<=f and d<=g:
    j=d
if f<=d and s>=f and f<=g:
    jh=f
if g<=d and g<=f and s>=g:
    j=g
print(h*g)