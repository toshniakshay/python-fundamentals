students_list = []

for i in range(10):
    students_list.append(i)

for i in students_list:
    print(i)

del students_list[5]

print(students_list)


# insert in any location
students_list.insert(2, 250)
print(students_list)

# sorting a list
students_list.sort()
print(students_list)

students_list.sort(reverse=True)
print(students_list)

# pop the last element from the list
students_list.pop()
print(students_list)

# reverse list => list.reverse
# index list.index('item') => returns first occurrence of element
# count list.count('item') => returns occurrences

# # clear list
# students_list.clear()
# print(students_list)

# ABOVE ARE THE METHODS OF THE LIST AS WE ARE USING LIST OBJECT TO INVOKE THEM

# LIST functions
print(len(students_list))
print(max(students_list))
print(min(students_list))
print(sum(students_list))

fruitsList = ['Mango', 'Apple', 'Banana']
print(*fruitsList)

# List comprehension in python
pow2 = [x for x in range(100) if x % 2 == 0]
print(pow2)

pow = [3 ** x for x in range(10)]
print(pow)

friends = ['Sunil', 'Sakshi', 'Sandeep', 'Bhavan', 'Anuja']
print(friends)
friends_with_s_initial = [name for name in friends if name.startswith('S') or name.startswith('s')]
print(friends_with_s_initial)

print(friends is friends_with_s_initial)
print(friends[0] is friends_with_s_initial[0])

print('Friends List location', id(friends))
print('Friends with s List location', id(friends_with_s_initial))

print('Friends List[0] location', id(friends[0]))
print('Friends with s List[0] location', id(friends_with_s_initial[0]))

list = [None, None, None]
print(list)