# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.

# 1.Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}


for lastName in students:
    lastName['Bryant'] = lastName.pop('Jordan')
    print(students)

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]


def function(a):
    i = 15
    a[1][0] = i
    return a

print(function(x))
# Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students[0]['last_name'])

def change_last_name(a):
    a[0]['last_name'] = 'Bryant'
    print(a[0]['last_name'])

change_last_name(students)
# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_directory['soccer'])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]

def change_val(a):
    print(a)
    a[0]['y'] = 30
    print(a)

change_val(z)

# 2.Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(a):
    y = 0
    pair = []
    while y <= len(a) - 1:
        pair.append(a[y])
        print(pair[y])
        y = y + 1

iterateDictionary(students)


# 3.Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# print(students[0]['first_name'])
# print(students[1]['first_name'])
# print(students[2]['first_name'])
# print(students[3]['first_name'])

def iterateDictionary2(a,b):
    y = 0    
    while y <= len(b) - 1:
        print(b[y][a])
        y = y + 1

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4.Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# print(len(dojo['locations']))

def printInfo(a):
    tempLength = len(a['locations'])
    print(str(tempLength) + ' LOCATIONS')
    print(a['locations'])
    y = 0
    while y < tempLength:
        print(a['locations'][y])
        y = y + 1

    tempLength = len(a['instructors'])
    print(str(tempLength) + ' INSTRUCTORS')
    print(a['instructors'])
    y = 0
    while y < tempLength:
        print(a['instructors'][y])
        y = y + 1



printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


