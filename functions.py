def my_name():
    return("Hello World")
print(my_name())


def add_sum(a, b):
    answer = a + b
    # print(answer)
    return answer

# add_sum(3, 7)    
print("output", add_sum(3, 7))



# Arbitrary function
def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print("Total sum", add_nums(3, 4, 6, 8, 9))


# Arbitrary Arguments, **kwargs
def add_ages(**ages):
    age_sum = 0
    for v, k in ages.items():
        age_sum += k
    return age_sum
print("Total Ages", add_ages(Jahnet = 20, Festus = 22, Kelvin = 23))  


# Local scope
def add_sum(a, b):
    answer = a + b
    return answer
print(add_sum(12, 5))


# enclosing scope
def add_nums(a, b):
    answer = a + b
    def double_it():
        double = answer * 2
        print(double)
    double_it()
    return answer
print(add_nums(12, 53))


# Global scope
global_var = 13

def add_nums(a, b):
    total = a + b
    print("Global Variables", global_var)
    def double_it():
        #local var
        double = total * 2
        print("Global var in inner function:", global_var)
        print("Double:", double)
    double_it
    return total
add_nums(13, 5)