import cmath
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=(b**2)-(4*a*c)
r1=(-b+cmath.sqrt(d))/(2*a)
print(r1)
r2=(-b-cmath.sqrt(d))/(2*a)
print(r2)
