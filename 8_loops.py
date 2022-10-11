for i in range(10):
    print(i ** i)

friendsList = ['Akshay', 'Baba', 'Vishal', 'Sanjana']

for name in friendsList:
    print(name * 2)

valid_age = 18
current_age = 0
while current_age < valid_age:
    current_age += 1
    print(current_age)
print('Loop has ended')

for i in range(10):
    if i == 3:
        continue
    if i > 6:
        break
    print(i)

