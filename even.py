# Program to check if a number is even or odd

# Take input from user
num = int(input("Enter a number: "))

# Check condition
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

# Program to check if a number is prime

# Take input from user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is NOT a Prime Number.")
            break
    else:
        print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")
