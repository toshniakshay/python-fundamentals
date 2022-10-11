"""
name = input('Enter your name\n')

print(name)
print('Welcome to multiplication calculator')

number1 = int(input('Enter 1st number\n'))
number2 = int(input('Enter 2st number\n'))

result = number1 * number2

print('Multiplication is', result)
"""

englishMarks = float(input('Enter marks of english\n'))
scienceMarks = float(input('Enter marks of science\n'))
mathsMarks = float(input('Enter marks of maths\n'))

avg = (englishMarks + scienceMarks + mathsMarks)/ 3
avg = round(avg, 2)  # restrict to 2 decimal places
print('Your average score is', avg)

