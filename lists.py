# # exe 1
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

# # exe 2
# students = ['yossi', 'mosh']
# print(f"numbers of student {len(students)}. The first student {students[0]}. The last student {students[-1]}")
# students[1] = "or"
# print(students)

# # exe 3
# grades = [80, 50, 90, 100, 30]
# grades.append(75)
# grades.insert(0, 88)
# grades[2] = 76
# print(grades)

# # exe 4
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_of_numbers.pop(0)
# print(list_of_numbers)
# list_of_numbers.pop(-1)
# print(list_of_numbers)
# list_of_numbers.pop(3)
# print(list_of_numbers)

# # exe 5
# list_of_product = ["pc", "phone", "clock"]
# if "pc" in list_of_product:
#     print("pc")
# if "keyword" not in list_of_product:
#     print("keyword is not in the list")

# # exe 6
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list_of_numbers:
#     print(num)

# # exe 7
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list_of_numbers:
#     if num % 2 == 0:
#         print(num)

# # exe 8
# grades = [80, 50, 90, 100, 30]
# sum_of_grades = 0
# for grade in grades:
#     sum_of_grades += grade
# print(sum_of_grades)

# # exe 9
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# high_num = None
# for num in list_of_numbers:
#     if high_num == None:
#         high_num = list_of_numbers[0]
#     if num > high_num:
#         high_num = num
# print(high_num)

# # exe 10
# names = ['yossi', 'mosh']
# user_input_name = input("Please enter name to search: ")
# flag = False
# for name in names:
#     if user_input_name == name:
#         flag = True
# if flag:
#     print("Found")
# else:
#     print("Not Found")

# # exe 11
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 5, 10]
# user_input_number = int(input("Please enter number to search: "))
# i = 0
# index_founded = []
# for num in list_of_numbers:
#     if num == user_input_number:
#         index_founded.append(i)
#     i += 1 
# if index_founded != []:
#     print(index_founded)
# else:
#     print("Not Found")

# # exe 12
# list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
# count = 0
# for num in list_of_numbers:
#     if num > 50:
#         count += 1
# print(count)

# # exe 13
# list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
# new_list = []
# count = 0
# for num in list_of_numbers:
#     if num % 2 == 0:
#         new_list.append(num)
# print(new_list)

# # exe 14
# names = ['yossi', 'mosh']
# i = 0
# while i <= len(names) -1:
#     print(names[i], i)
#     i += 1

# # exe 15
# list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
# print(list_of_numbers[0:3])
# print(list_of_numbers[-3:])
# print(list_of_numbers[2:6])
# print(list_of_numbers[::-1])

# # exe 16
# names = ['yossi', 'mosh', "dsv", "svd", "sdvc", "sdv", "sdfb", "adgv", "sdf", "seghb"]
# print(names[::2])
# print(names[1::2])
# print(names[::-2])

# # exe 17
# list_of_numbers = [num for num in range(1 ,21)]
# first_new_list = list_of_numbers[:10]
# second_new_list = list_of_numbers[9:]

# print(list_of_numbers)
# print(first_new_list)
# print(second_new_list)
# print(list_of_numbers[5:14])

# #exe 18
# list_of_numbers = [1, 2, 3, 4, 5, 6, 55, 8, 5, 50]
# print(list_of_numbers[:int((len(list_of_numbers)) /2)])
# print(list_of_numbers[int((len(list_of_numbers)) /2):])

# # exe 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# multi_by_two = [num * 2 for num in numbers]
# multi_by_four = [num * num for num in numbers]
# enen_num = [num for num in numbers if num % 2 == 0]
# greater_than_five = [num for num in numbers if num > 5]

# # exe 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# greater_than_Sixty = [grade for grade in grades if grade > 60]
# less_than_sixtieth = [grade for grade in grades if grade < 60]
# add_five = [grade + 5 for grade in grades]

# # exe 21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# greater_than_four = [name for name in names if len(name) > 4]
# names_in_upper = [name.upper() for name in names ]
# only_start_with_d = [name for name in names if name[0] == "D"]

# # exe 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new_list = [num for num in numbers if num % 3 == 0 and num > 10]

# # exe 23
# numbers = [int(input("Enter number")) for num in range(10)]
# print(numbers)
# high_number = None
# low_number = None
# for num in numbers:
#     if high_number == None and low_number == None:
#         high_number = num
#         low_number = num
#     if num > high_number: # type: ignore
#         high_number = num
#     if num < high_number: # type: ignore
#         low_number = num
# print(high_number, low_number)

# # exe 24
# users = ["Moshe", "David", "Dana", "Noa", "Michael"]
# user_input_name = input("Enter name ")
# if user_input_name in users:
#     users.remove(user_input_name)
#     print(users)
# else:
#     print("name not found")

# # exe 25
# list_of_numbers = [num for num in range(1 ,11)]
# even_list = [num for num in list_of_numbers if num % 2 == 0]
# add_list = [num for num in list_of_numbers if num % 2 != 0]
# greater_than_20 = [num for num in list_of_numbers if num > 20]
# print(list_of_numbers)
# print(even_list)
# print(add_list)
# print(greater_than_20)

# # exe 26
# list_of_numbers = [num for num in range(1 ,11)]
# user_input = int(input("Enter num "))
# user_search = []
# i = 0
# for num in list_of_numbers:
#     if num == user_input:
#         user_search.append(i)
#     i += 1
# if user_search != []:
#     print(f"The {user_input} in list {len(user_search)} times. ")
# else:
#     print("Not found")

# # exe 27
# first_list = [num for num in range(1 ,11)]
# second_list = [num for num in range(10 ,21)]
# one_list = first_list + second_list
# print(one_list)
# print(one_list[:5])
# print(one_list[-5:])
# print(one_list[::-1])

# # exe 28
# list_of_numbers = [num for num in range(1 ,11)]
# user_input = int(input("Enter num "))
# flag = False
# for num in list_of_numbers:
#     if num == user_input:
#         flag = True
# if flag:
#     print("The num is already in ")
# else:
#     list_of_numbers.append(user_input)
#     print(list_of_numbers)

# final project
grades = [85, 72, 90, 55, 100, 63, 48, 77]

while True:
    print('''
    ===== Grades Management =====

    1. Show all grades
    2. Add a grade
    3. Search for a grade
    4. Remove a grade
    5. Show passing grades
    6. Show failing grades
    7. Show highest and lowest grade
    8. Show average grade
    9. Show first 3 grades
    10. Show grades in reverse
    0. Exit
    ''')
    menu_choose = int(input("please enter number from the menu"))
    if menu_choose == 1:
        print(grades)
    elif menu_choose == 2:
        grades.append(int(input("Enter grade ")))
    elif menu_choose == 3:
        user_input = int(input("Enter num "))
        user_search = []
        i = 0
        for num in grades:
            if num == user_input:
                user_search.append(i)
            i +=1
        if user_search != []:
            print(f"Location {user_search} ")
        else:
            print("Not found")
    elif menu_choose == 4:
        user_input = int(input("Enter num "))
        grades.remove(user_input)
    elif menu_choose == 5:
        print([grade for grade in grades if grade > 60])
    elif menu_choose == 6:
        print([grade for grade in grades if grade <= 60])
    elif menu_choose == 7:
        high_number = None
        low_number = None
        for grade in grades:
            if high_number == None and low_number == None:
                high_number = grade
                low_number = grade
            if grade > high_number: # type: ignore
                high_number = grade
            if grade < high_number: # type: ignore
                low_number = grade
        print(high_number, low_number)
    elif menu_choose == 8:
        total = 0
        for grade in grades:
            total += grade
        print(f"avg {total / len(grades)}")
    elif menu_choose == 9:
        print(grades[:3])
    elif menu_choose == 10:
        print(grades[::-1])
    elif menu_choose == 0:
        break