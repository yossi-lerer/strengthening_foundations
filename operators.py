#exe 1
num1 = 25
num2 = 7
print(f"the sum of {num1} and {num2} is {num1 + num2}")
print(f"the sub of {num1} and {num2} is {num1 - num2}")
print(f"the multi of {num1} and {num2} is {num1 * num2}")
print(f"the divide of {num1} and {num2} is {num1 / num2}")
print(f"the full divide (//) of {num1} and {num2} is {num1 // num2}")
print(f"the % of {num1} and {num2} is {num1 % num2}")
print(f"the ** of {num1} and {num2} is {num1 ** num2}")

# exe 2
balance = 1000
print(balance)
balance += 250
print(balance)
balance *=  2
print(balance)
balance -=  2
print(balance)
balance /= 4
print(balance)

#exe 3
Discount_amount_in_shekels = 10
Price_after_the_discount = 1200
print(f"the Discount amount in shekels is {Discount_amount_in_shekels * Price_after_the_discount / 100}")

# exe 4
amount = float(input("Please enter the amount of money: "))
interest_rate = float(input("Please enter the annual interest rate (in %): "))
print(f"The interest for one year is: {amount * interest_rate / 100}")

# exe 5
grade1 = float(input("Please enter the first grade: "))
grade2 = float(input("Please enter the second grade: "))
grade3 = float(input("Please enter the third grade: "))
print(f"The average of the three grades is: {(grade1 + grade2 + grade3) / 3}")

# exe 6
first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"
print("Hello, my name is " + first_name + " " + last_name + " and I live in " + city + ".")
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")

# exe 7
full_name = input("Please enter your full name: ")
print(f"Your full name is: {full_name}")
print(f"The number of characters in your name is: {len(full_name)}")
print(f"Your name in uppercase is: {full_name.upper()}")
print(f"Your name in lowercase is: {full_name.lower()}")

# exe 8
sentence = input("Please enter a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())
