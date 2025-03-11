# In a for or while loop the break statement may be paired with an else clause. 
# If the loop finishes without executing the break, the else clause executes.

# In a for loop, the else clause is executed after the loop finishes its final iteration, that is, if no break occurred.
# In a while loop, it’s executed after the loop’s condition becomes false

# In either kind of loop, the else clause is not executed if the loop was terminated by a break. 
# Of course, other ways of ending the loop early, such as a return or a raised exception, will also skip execution of the else clause.

for n in range(2,10):
    for x in range(2, n):
        print('n:', n, 'x:', x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print('stategy 2 : ADVANCED WAY OF FINDING PRIME NUMBERS')
for n in range(2,10):
        for x in range(2, int(n/2)):
            print('n:', n, 'x:', x)
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')