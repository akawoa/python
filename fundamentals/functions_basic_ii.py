# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(a):
    y = a
    while y >= 0:
        print(y)
        y = y - 1
        if y < 0:
            print("Final else statement")
            break

countdown(5)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

list = ['DaBaby', 'Lets Go']

def print_and_return(a):
    print(a[0])
    return(a[1])

print(print_and_return(list))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

sum = 0
list2 = [5,0]
def first_plus_length(a):
    sum =  a[0] + len(a)
    return sum

print(first_plus_length(list2))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

sum = []
list3 = [0,1,2,3,4,5]
def values_greater_than_second(a):
    i = len(a) - 1
    while i > -1:
        if(len(a) < 2):
            return False
        elif(a[i] > a[1]):
            sum.append(a[i])
            
        i = i - 1
    print(sum)

values_greater_than_second(list3)



# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def length_and_value(a,b):
    special = []
    i = a
    while i > 0:
            special.append(b)
            i = i - 1
    return special

print(length_and_value(3, 1))