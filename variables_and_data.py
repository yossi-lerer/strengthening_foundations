# exe 1
first_name = "David"
last_name = "Cohen"
age = 25
city = "Tel Aviv"
email = "david@gmail.com"
print(f'''
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================
''')

#exe 2

birth_year = 2003
current_year = 2026
print(f"You are approximately {current_year - birth_year} years old.")

#exe 3
width = 10
height = 5
print(f"The area of ​​the rectangle is {width  * height}; the perimeter of the rectangle is {(width + height) * 2}.")

# exe 4

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(salary))


# exe 5

first_name = input("first name: ")
last_name = input("last name: ")
age = int(input("age: "))
city = input("city: ")
print(f'''
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
========================
''')

#exe 6
num1 = input("please enter first num ")
num2 = input("please enter second num ")

print(f"the sum of {num1} and {num2} is {int(num1) + int(num2)}")
print(f"the subtraction of {num1} and {num2} is {int(num1) - int(num2)}")
print(f"the product of {num1} and {num2} is {int(num1) * int(num2)}")
print(f"the division of {num1} and {num2} is {int(num1) / int(num2)}")


# exe 7
product_name = input("Please enter the product name: ")
product_price = float(input("Please enter the product price: "))
product_quantity = int(input("Please enter the product quantity: "))
print(f'''
====== Purchase Receipt ======
Product: {product_name}
Price: {product_price}  
Quantity: {product_quantity}
Total: {product_price * product_quantity}
==============================
''')

# exe 9

name = input("Please enter the employee's name: ")
hours_worked = float(input("Please enter the number of hours worked in the month: "))
hourly_rate = float(input("Please enter the hourly rate: "))
print(f'''
====== Salary Report ======
Employee Name: {name}
Hours Worked: {hours_worked}
Hourly Rate: {hourly_rate}
Monthly Salary: {hours_worked * hourly_rate}
===========================
''')

#exe 10 
total_bill = float(input("Please enter the total bill amount: "))
tip_percentage = float(input("Please enter the desired tip percentage: "))
number_of_diners = int(input("Please enter the number of diners: "))
print(f'''
====== Bill Split ======
Tip: {(total_bill * (tip_percentage / 100))}
Total Amount: {total_bill + (total_bill * (tip_percentage / 100))}
Total for each diner: {(total_bill + (total_bill * (tip_percentage / 100))) / number_of_diners}
=========================
''')

#exe 12
a = 10
b = 20
c = a

a = b
b = c

# exe 13
first_name = input("first_name ")
last_name = input("last_name")
age = input("age")
Name_of_Educational_Institution = input("Name_of_Educational_Institution")
Course_Name = input("Course_Name")
Number_of_Months_of_Study = int(input("Number_of_Months_of_Study"))
Monthly_Price = int(input("Monthly_Price"))

print(f'''
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {Name_of_Educational_Institution}
Course: {Course_Name}
Duration: {Number_of_Months_of_Study} Months
Monthly Price: {Monthly_Price}

Total Course Price: {Number_of_Months_of_Study * Monthly_Price}

================================
Registration completed!
================================
''')