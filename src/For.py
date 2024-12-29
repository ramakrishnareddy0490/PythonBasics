# The for statement in Python differs a bit from what you may be used to in C or Pascal. 
# Rather than always iterating over an arithmetic progression of numbers (like in Pascal), 
# or giving the user the ability to define both the iteration step and halting condition (as C), 
# 
# Python’s for statement iterates over the items of any sequence (a list or a string), 
# in the order that they appear in the sequence. For example (no pun intended):

# iterating a list and measuring the length of each element(String) in the list
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, 'word has',len(w), 'characters')

# Code that modifies a collection while iterating over that same collection can be tricky to get right. 
# Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print('User data -', users)
# Strategy 1:  Iterate over a copy
print("Strategy 1")
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print('Active user data -', users)

# Strategy 2:  Create a new collection
print("Strategy 2")
# create new empty collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print('User data -', users)
active_users, inactive_users = {}, {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status;
    else:
        inactive_users[user] = status;
print('Active user data -', active_users)
print('Inactive user data -', inactive_users)