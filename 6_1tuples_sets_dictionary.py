# Tuples are immutable
name = 'Akshay'
print(name)

nameTuple = ('A', 'K', 'S', 'H', 'A', 'Y')

n = tuple(name)
print(n)

# duplicate elements are omitted
# Indexing is not allowed as items are saved in random index
# Iteration is same as list
duplicateSet = {1, 2, 3, 423, 1, 2, 3}
print(duplicateSet)

tuple1 = (15)  # python considers it as mathmatical bracket
print(type(tuple1))

tuple2 = (15,)  # should add comma in case of single value tuple
tuple2 = 15, # optional way
print(type(tuple2))

# list elements of tuples can be updated but not the list entirely
tupple3 = ('Test', 'Test3', [1, 2, 3, 4])
print(tupple3)
my_list = tupple3[2]
my_list[0] = 100
print(tupple3)

# Dictionary
# Key value pair data structure
# value for the same key will be re-written in the dictionary
# Heterogeneous in nature
marks = {
    'Akshay': 100,
    'Sunil': 200,
    'Sakshi': 300
}

print(marks)
print(marks['Akshay'])

for student in marks:
    print(student, marks[student])

# Dictionary Comprehensions


# Set operations
friends = {"Anam", "Sunil", "Sakshi", "Jeevan"}
abroad = {"Jeevan"}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends = {"Anam", "Sunil", "Sakshi"}
abroad_friends = {"Jeevan", "Abhay"}

all_friends = local_friends.union(abroad_friends)
print(all_friends)

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))


testTuple = 15,
print(type(testTuple))
