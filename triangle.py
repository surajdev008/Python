print("Enter the three sides of the triangle:")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

s = (a + b + c) / 2

area1 = s*(s-a)*(s-b)*(s-c)

area = pow(area1,0.5)
print("The area of the triangle is",area)
