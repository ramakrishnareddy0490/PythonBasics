# Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]

# lists can be indexed and sliced
print('First element in the list - ', squares[0])  # indexing returns the item
print('Last element in the list - ', squares[-1])
print('First two elements in the list - ', squares[:2])  # slicing returns a new list

# Lists also support operations like concatenation:
print(squares + [36, 49, 64, 81, 100])

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # square of 8 is 64. so, something's wrong here
cubes[3] = 64  # replace the wrong value
print(cubes)

# You can also add new items at the end of the list, by using the list.append() method (we will see more about methods later):

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print('cubes elements after appending new data at the last of the list - ', cubes)

# Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list.
# Any changes you make to the list through one variable will be seen through all other variables that refer to it.:

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(rgba == rgb)
rgba.append("Alph")
print(rgba)
print(rgb)
print(rgba == rgb)

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(rgba)
print(correct_rgba)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)
letters[2:5] = [] # now remove them
print(letters)
letters[:] = [] # clear the list by replacing all the elements with an empty list
print(letters)

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letters))

#It is possible to nest lists (create lists containing other lists), for example:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
