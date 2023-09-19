# Input a number from the user
n = int(input("Enter a number: "))

# Find the number of digits in n
num_digits = len(str(n))

print(num_digits)
# Initialize a variable to store the sum of cubes of digits
sum_of_cubes = 0

# Create a temporary variable to manipulate
temp = n

# Calculate the sum of cubes of digits
while temp > 0:
    digit = temp % 10
    sum_of_cubes=sum_of_cubes+digit**num_digits
    temp //= 10

# Check if it's an Armstrong number
if n == sum_of_cubes:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")
