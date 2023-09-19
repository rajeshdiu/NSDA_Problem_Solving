n=int(input("Enter Digit:"))
sum=0
temp=n
print("Before Reverese The Digit : ",temp)
while (temp!=0):
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10
print("After Reverese The Digit : ",sum)
    
