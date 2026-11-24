# exe 1
i = 1
while i <= 10:
    print(i)
    i += 1

# exe 2
i = 10
while i >= 1:
    print(i)
    i -= 1
else:
    print("START!")

# exe 3
i = 0 
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# exe 4
num = int(input("Enter num for multi: "))
i = 1
while i <= 5:
    print(num * i)
    i += 1

# exe 5
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
else:
    print(total)

# exe 6
password = input("please enter your password ")
password_stored = "Python123"
while password != password_stored:
    password = input("please enter your password again ")
else:
    print("Welcome!")

# exe 7
secret_number = 27
user_guess = int(input("guess number: "))
while secret_number != user_guess:
    user_guess = int(input("guess number again: "))
else:
    print(f"Correct guess—your number is {secret_number}.")

# exe 8
num = int(input("Please enter int number "))
total = 0 
while num != 0:
    total += num
    num = int(input("Please enter int number "))
else:
    print(total)

# exe 9
grades = []
grade = int(input("To add a new grade please enter num between 1 - 100 "))
while grade != 999:
    grades.append(grade)
    grade = int(input("To add a new grade please enter num between 1 - 100 "))
else:
    print(f"Total grades {len(grades)}. Sum of the grades {sum(grades)}. Avg {sum(grades) / len(grades)}.")

# exe 10
numbers = []
num = int(input("Please enter int number "))
while num >= 0:
    numbers.append(num)
    num = int(input("Please enter int number "))
else:
    print(f"the sum of numbers {sum(numbers)}. User enter {len(numbers)} numbers")

# exe 11
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# exe 12
num = int(input("Enter number: "))
c = 0
while num != 0:
    num //= 10 
    c += 1
print(c)

# exe 13
num = int(input("Enter number: "))
new_num = ""
while num != 0:
    new_num += str(num % 10)
    num //= 10
print(int(new_num))

# exe 14
num = int(input("Enter number: "))
count =2
while count != num:
    if num % count == 0:
        print(f"The {num} is not a Prime number")
        break
    count += 1
else:
    print(f"The {num} is a Prime number ")

# exe 15
balance = 5000

# exe 22
for row in range(1,11):
    for col in range(1,11):
        print(row * col, end="\t")
    print()