# if condition statement

hungry = True
if hungry:
    print("Eat some Food")



# if else statement

num = 50
if num >= 32:
    print("The value of num is greater than 32")
else:
    print("num is less than 32")



# if...elif...else statement

marks = 70
if marks >= 90:
    print("scored an A")
elif marks >= 80:
    print("scored A B")
elif marks >=70:
    print("scored a C")
else:
    print("Average")  


# for loop

names = {"Habibi", "Festus", "Jahnet", "Kelvin"}
for name in names:
    print(name)


#for loopS:using range

welcome_message = "Welcome home"
for i in range(5):
    print(welcome_message)
    print(i)