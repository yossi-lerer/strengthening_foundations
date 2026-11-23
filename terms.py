# print(not (1 > 2))

# # exe 1
# age = int(input("enter your age"))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# # exe 2
# num = float(input("Please enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # exe 3
# num = int(input("Please enter an integer: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# #exe 4
# num1 = float(input("Please enter the first number: "))
# num2 = float(input("Please enter the second number: "))
# if num1 > num2:
#     print(f"The larger number is: {num1}")
# elif num2 > num1:
#     print(f"The larger number is: {num2}")
# else:
#     print("The numbers are equal.")

# # exe 5
# password = "Python123"
# user_input = input("Please enter the password: ")
# print("Access granted" if user_input == password else "Access denied")

# # exe 6
# num = int(input("Please enter a number: "))
# if 1 <= num <= 10:
#     print("The number is between 1 and 10.")
# elif 11 <= num <= 50:
#     print("The number is between 11 and 50.")
# elif 51 <= num <= 100:
#     print("The number is between 51 and 100.")

# # exe 7
# grade = int(input("Please enter the student's grade (0-100): "))
# if 90 <= grade <= 100:
#     print("Excellent")
# elif 80 <= grade <= 89:
#     print("Very Good")
# elif 70 <= grade <= 79:
#     print("Good")
# elif 60 <= grade <= 69:
#     print("Passed")
# elif 0 <= grade <= 59:
#     print("Failed")

# # exe 8
# username = input("Please enter your username: ")
# password = input("Please enter your password: ")
# correct_username = "admin"
# correct_password = "123456"
# if username == correct_username and password == correct_password:
#     print("Login Successful")
# elif username == correct_username and password != correct_password:
#     print("Wrong Password")
# elif username != correct_username:
#     print("Unknown User")

# # exe 9
# age = int(input("Please enter your age: "))
# price = float(input("Please enter the product price: "))
# if age > 60:
#    print(f"The price after 20% discount is: {price * 0.8}")
# elif age < 18:
#    print(f"The price after 10% discount is: {price * 0.9}")
# else:
#    print(f"The price is: {price}")

# # exe 10
# num = int(input("Please enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by both 3 and 5.")
# elif num % 3 == 0:
#     print("The number is divisible by 3.")
# elif num % 5 == 0:
#     print("The number is divisible by 5.")
# else:
#     print("The number is not divisible by 5 and/or 3.")

# # exe 11
# age = int(input("Please enter your age: "))
# is_accompanied = input("Are you accompanied by an adult? ")
# if age >= 18 or (age >= 16 and is_accompanied == "true"):
#     print("access")

# # exe 12
# grade_average = float(input("Please enter the average grade: "))
# income = float(input("Please enter the monthly income: "))
# if grade_average > 90 or (grade_average > 85 and income < 5000):
#     print("The student is eligible for the scholarship.")
# else:
#     print("The student is not eligible for the scholarship.")

# # exe 13
# username = input("Please enter your username: ")
# password = input("Please enter your password: ")
# account_active = input("Is the account active? ")
# if username == "admin" and password == "123456" and account_active == "true":
#     print("Login Successful")

# # exe 14
# num = int(input("Please enter a number: "))
# if 20 <= num <= 80:
#     print("The number is in the range of 20 to 80.")
# if not (num < 20 or num > 80):
#     print("The number is in the range of 20 to 80.")

# #exe 15
# balance = 5000
# amount = float(input("Please enter the amount to withdraw: "))
# if amount > 0:
#     if amount <= balance:
#         balance -= amount
#         print(f"Withdrawal successful. New balance: {balance}")
#     else:
#         print("Error: Insufficient funds.") 

for i in range(3,4):
    if True:
        print(i)
else:
    print(range(3,4))