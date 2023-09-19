n = int(input("Enter Digit: "))

temp = n
sum = 0

while temp != 0:
    rem = temp % 10
    sum = sum + rem
    temp = temp // 10  # Use integer division

print("Digit Summation is:", sum)
