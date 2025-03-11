# Print the data in single line
print('Hello World!') 

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. In the following example, the initial newline is not included
# print data in multiple lines
print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)

# using escape sequence (\)
print('I\'m a python developer')

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote
print(r'C:\some\name')

# Strings can be concatenated (glued together) with the + operator, and repeated with *
print('Py' + 'thon')
print('Py' * 3)

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py''thon')

# This feature is particularly useful when you want to break long strings:
print('Put several strings within parentheses '
'to have them joined together.')

# If you want to concatenate variables or a variable and a literal, use +
prefix = 'Py'
print(prefix + 'thon')

#Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
word = 'Python'
print(word[0])  # character in position 0

# Indices may also be negative numbers, to start counting from the right:

print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])

#In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring:
word = 'Python'
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

# Attempting to use an index that is too large will result in an error:

word = 'Python'
# print(word[42])  # results an error sincee the word has only 6 characters

#However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])  # slicing is forgiving

#Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

# word[0] = 'J'  # results an error

# The built-in function len() returns the length of a string:

print(len('Python'))