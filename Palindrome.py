n=int(input("Enter Digit: "))
temp=n
sum=0
while (temp!=0):
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10
if sum==n:
    print("Your Digit is Palindrome",sum)
else:
    print("Not Palindrome")