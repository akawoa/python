#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# will print out 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Will print out undefined and 5 or error out becauswe that function is not named (number_of_days_in_a_week_silicon_or_triangle_sides())

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# It will only say "5" because once the return happens it will stop running the code

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# it will only say "5" because once it hits the return it will stop running the function

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# it will print out 5 for the first and for the second we are not feeding it a variable but a function so it will say "None"

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# it will print out 3 on one line and 5 on another line for the first print statements, but on the third, it will throw an error because the types are not supported

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# it will return "25" because we are using concatenation on stringified values that were returned to us

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# it will first print out "100", then since b is not less than ten, it will return "10" back to us


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# it will return back to us "7" as 2 is less than 3, then it will return 14 as 5 is NOT less than 3, then it will return "21"


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# it will return to us "8"


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# it will first print out 500 which is b, then it will print out 500, print out 500, then 300, then 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# it will print out first 500, then 500, then 300, finally 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# it will first print 500, then 500, then 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# it will first print 1, then 3, then 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# It will print out 1, then 3, then 5, then 10