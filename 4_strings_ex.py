name = 'Akshay'

address = ''' B4-405 Rahul Nisarg, 
Atul Nagar Phase 2
Warje, Pune-411058'''

# indexing
print(name[0])
print(name[-1])

# slice
slicedStr = name[0:4]
print(slicedStr)

#  if we don't specify the starting range then 0 will be considered
slice1 = name[:4]
print(slice1)

#  if we don't specify the ending range then n-1 will be considered
slice2 = name[2:]
print(slice2)

# we can also give the step
slice3 = name[0:5:2]
print(slice3)

# slice with negative index
slice4 = name[::-1]
print(slice4)

slice5 = name[0:5:-1]
print(slice5)

slice6 = name[-1:0:-1]
print(slice6)

slice7 = name[-1:0:1]
print(slice7)

# + operator is used as concatenation
# * operator repeats n number of times

print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.islower())
print(name.isupper())
print(name.upper())
print(name.lower())
x = '   Akshay  '
print(x.lstrip())
print(x.rstrip())