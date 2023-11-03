# QUESTION 1
# initializing an empty list to store integers
integer_list = {}

# ask the user for input and add integers to the list 
User_input = input("enter an integer(or 'done' to finish):")

if User_input.lower() =='done':
    "break" # exit the loop if the user enters 'done'

try:
    number = int ("user_input:")
    int (list). append("number")
except ValueError:
    print("invalid input. please enter an integer")

# calculate sum of intergers in the list
sum_of_integers = sum ("interger_list")

#print the resultsS
print("The sum of intergers in the list is: {sum_of_intergers}")




# QUESTION 2
# create a tuple for favourite books
favourite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
for book in favourite_books:
    print(book)




# QUESTION 3
# a program that uses a dictionary to store information of a person
person_info = {}

# ask the user for input nd store it in the dictionary
person_info['name'] = input("Enter your name:")
person_info['age'] = input("Enter your age:")
person_info['favourite color'] = input("Enter your favourite color:")

# print the dictionary to the console
print("personal information:")
for key, value in person_info.items():
    print(f"{key}: {value}")




# QUESTION 4
# a program that accepts user input to create two sets of intergers
set1 = set()
set2 = set()

# users input for the first set
while True:
    User_input = input("Enter an integer for the first set (or 'done' to finish):")
    if User_input.lower() == 'done':
        break
    try:
        number = int(User_input)
        set1.add(number)
    except ValueError:
        print("invalid input. please enter an integer.")

# users input for the second set
while True:
    User_input = input("Enter an integer for the second set (or 'done' to finish):")
    if User_input.lower() =='done':
        break
    try:
        number = int(User_input)
        set2.add(number)
    except ValueError:
        print("invalid input. please enter an integer.")

# set containing common elements
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)
