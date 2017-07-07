
#Fibonacci sequences adds the previous two numbers together.
#E.g 0,1,1,2,3,5,8,13,21....

x,y,z=0,1,0 #x is 0, y is 1 and z will be be the sum of both numbers.
i = 100000000000000000000000000000000000000
while y < i:
    z = x + y #adds previous two numbers
    x = y # assigns previous num to x
    y = z # assigns sum to y
    print(y)
