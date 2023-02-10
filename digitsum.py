n=int(input("Enter a number:"))
temp=n
count=0
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
print("Digit sum=",sum)