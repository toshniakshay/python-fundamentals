add = lambda x, y: x + y

print(add(5, 7))

sequence = [1, 5, 6, 7, 8]

doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
