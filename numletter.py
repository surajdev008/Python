string=str(input("Enter a string:"))
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      if(i.isalpha()):
            count2=count2+1
print("The number of digits are:")
print(count1)
print("The number of letters are:")
print(count2)