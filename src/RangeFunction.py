# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. 
# It generates arithmetic progressions:

# The given end point is never part of the generated sequence; range(10) generates 10 values from 0 to 9
print('Print the range of 10 values', end=' - ')
for i in range(10):
    print(i, end=',')

# It is possible to let the range start at another number
print('\nPrint the range of values from 5 to 10', end=' - ')
for i in range(5, 10):
    print(i, end=',')

# You can specify a different increment (even negative; sometimes this is called the ‘step’):
print('\nPrint the range of values from 0 to 10 with increment of 2', end=' - ')
for i in range(0, 10, 2):
    print(i, end=',')

# range functin with negative values; sometimes this is called the ‘step’):
print('\nPrint the range of values from -10 to -1010 with increment of -100', end=' - ')
for i in range(-10, -1010, -100):
    print(i, end=',')
# To iterate over the indices of a sequence, you can combine range() and len() as follows:

print()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])