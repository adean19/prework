# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of # the function. The first line of the code has been defined as below.


def hello_name(user_name):
    """Display a simple greeting. """
    print("hello" + "_" + user_name)

hello_name('Username')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for value in range (1, 100, 2):
        print (value)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(list)

a_list = [1, 2, 3, 4, 5]
max_num_in_list


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0  :
        return True
    elif a_year % 400 == 0 :
        return True
    else: 
        return False
    
a_year = 2023 
print(is_leap_year(a_year))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if len(a_list) < 1:
        return False
    min_val = min(a_list)
    max_val = max(a_list)
    if max_val - min_val +1 == len(a_list):
        for i in range(len(a_list)):
            if a_list[i] < 0:
                j = -a_list[i] - min_val
            else:
                j = a_list[i] - min_val
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else: 
                    return False
        return True
    return False

a_list = [1, 2, 3, 4, 5]
print(is_consecutive(a_list))


        

