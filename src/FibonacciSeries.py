
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
a,b = 0,1;
while a < 100:
    print(a)
    a,b = b, a+b
    