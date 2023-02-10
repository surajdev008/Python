n = int(input("Enter how many fibonacci numbers you want?"))
x=0
y=1
if n == 1:
    print(x)
elif n == 2 :
    print(x)
    print(y)
else :
    print(x)
    print(y)
    while n > 2 : 
        z = x+y
        print(z)
        x = y
        y = z
        n=n-1