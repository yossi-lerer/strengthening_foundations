# exe 1
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])

# exe 2
students = ['yossi', 'mosh']
print(f"numbers of student {len(students)}. The first student {students[0]}. The last student {students[-1]}")
students[1] = "or"
print(students)

# exe 3
grades = [80, 50, 90, 100, 30]
grades.append(75)
grades.insert(0, 88)
grades[2] = 76
print(grades)

# exe 4
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers.pop(0)
print(list_of_numbers)
list_of_numbers.pop(-1)
print(list_of_numbers)
list_of_numbers.pop(3)
print(list_of_numbers)

# exe 5
list_of_product = ["pc", "phone", "clock"]
if "pc" in list_of_product:
    print("pc")
if "keyword" not in list_of_product:
    print("keyword is not in the list")

# exe 6
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_of_numbers:
    print(num)

# exe 7
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_of_numbers:
    if num % 2 == 0:
        print(num)

# exe 8
grades = [80, 50, 90, 100, 30]
sum_of_grades = 0
for grade in grades:
    sum_of_grades += grade
print(sum_of_grades)

# exe 9
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
high_num = None
for num in list_of_numbers:
    if high_num == None:
        high_num = list_of_numbers[0]
    if num > high_num:
        high_num = num
print(high_num)

# exe 10
names = ['yossi', 'mosh']
user_input_name = input("Please enter name to search: ")
flag = False
for name in names:
    if user_input_name == name:
        flag = True
if flag:
    print("Found")
else:
    print("Not Found")

# exe 11
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 5, 10]
user_input_number = int(input("Please enter number to search: "))
i = 0
index_founded = []
for num in list_of_numbers:
    if num == user_input_number:
        index_founded.append(i)
    i += 1 
if index_founded != []:
    print(index_founded)
else:
    print("Not Found")

# exe 12
list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
count = 0
for num in list_of_numbers:
    if num > 50:
        count += 1
print(count)

# exe 13
list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
new_list = []
count = 0
for num in list_of_numbers:
    if num % 2 == 0:
        new_list.append(num)
print(new_list)

# exe 14
names = ['yossi', 'mosh']
i = 0
while i <= len(names) -1:
    print(names[i], i)
    i += 1