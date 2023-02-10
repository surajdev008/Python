n=int(input("Enter a 3 digit number:"))
temp=n
count=0
sum=0
while temp>0:
    temp=temp//10
    count=count+1
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**count
    temp=temp//10
if n==sum:print(n,"is an armstrong")
else:print(n,"is not an armstrong")