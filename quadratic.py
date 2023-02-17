import math as m

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=b**2-4*a*c
r1=(-b+m.sqrt(d))/(2*a)
r2=(-b-m.sqrt(d))/(2*a)
if(d>0):
    print("roots are real and equal r1=",r1)
    print("roots are real and equal r2=",r2)

else:
    print("roots are imaginary")