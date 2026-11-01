# if statement
age = 18
if age >= 18:
    print("Eligible")

# if-else statement
age = 16
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Nested if statement
age = 21

if age >= 18:
    if age >= 21:
        print("Adult")


        # Odd or Even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


    # Nested if - Password Check

password = input("Enter password: ")

if password == "python123":
    print("Password correct")

    if len(password) >= 8:
        print("Login successful")
    else:
        print("Password too short")

else:
    print("Incorrect password")  #nesting

    #loop

    # Loop in Python

# For Loop
for i in range(1, 6):
    print(i)

# While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Break Statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Continue Statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Nested Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

        # Multiplication Table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    # Break Statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Continue Statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)