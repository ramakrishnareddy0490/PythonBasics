
#In mathematics, the Fibonacci sequence is a sequence in which each term is the sum of the two terms that precede it. 
# Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . 
# Many writers begin the sequence with 0 and 1, although some authors start it from 1 and 1[1][2] and some (as did Fibonacci) from 1 and 2. 
# 
# Starting from 0 and 1, the sequence begins
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

#The Fibonacci numbers were first described in Indian mathematics as early as 200 BC in work by Pingala 
# on enumerating possible patterns of Sanskrit poetry formed from syllables of two lengths.[3][4][5] 
# They are named after the Italian mathematician Leonardo of Pisa, 
# also known as Fibonacci, who introduced the sequence to Western European mathematics in his 1202 book Liber Abaci.


# The first line contains a multiple assignment: 
    # the variables a and b simultaneously get the new values 0 and 1. 
    # On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. 
    # The right-hand side expressions are evaluated from the left to the right.
a,b = 0,1;
print('Fibonacci sequence is - ', end=' ')
while a < 100: # Other comparisons are < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).
  #  print(a) #The body of the loop is indented: indentation is Python’s way of grouping statements.
    print(a, end=',') # The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
    a,b = b, a+b
    