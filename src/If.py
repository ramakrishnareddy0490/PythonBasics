x = int(input('Enter your age: '))
if(x < 5):
    print('You are an infant')
elif x < 18:
    print('You are a minor')
else:
    print('You are an adult')

# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.