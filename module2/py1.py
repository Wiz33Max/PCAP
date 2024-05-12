import math
# print ([name for name in dir(math)]) # list comprehention
# for name in dir(math):
# from pprint import pprint as pp
# pp (name for name in dir(pp))
squares_generator = (x**2 for x in range(1, 6))

# Convert the generator to a list to force evaluation and print
squares_generator = (x**2 for x in range(1, 6))

# Loop through the generator and print each element
for square in squares_generator:
    print(square)

#or

# Convert the generator to a list to force evaluation and print
squares_list = list(squares_generator)
print(squares_list)

def line ():
    print ('-' * 80)

# usefull math relaterd functions (pow(x,y) is a base function):
import math

line()

x = 3.45
print(math.pi)

## Print the value of x rounded up to the nearest integer
print(math.ceil(x))

# Print the value of x rounded down to the nearest integer
print(math.floor(x))

# Print the value of x with the decimal part removed (truncated)
print(math.trunc(x))

y=-43
# Print the absolute value of x (ignores the sign)
print(math.fabs(y))


# Print the square root of x
print(math.sqrt(x))

from random import *
line()
seed(0)
for i in range (5):
    print (i)
    print(random())
    #generate a num from 0 to 9
    print (math.trunc((random()*10)))
    #generate a num from 0 to 99
    print (math.trunc((random()*100)))
    #generate a num from 0 to 999
    print (math.trunc((random()*1000)))
    #generate a num from 0 to 9999
    print (math.trunc((random()*10000)))
    #generate a num from 0 to 99999
    print (math.trunc((random()*100000)))
    #generate a num from 0 to 999999
    print (math.trunc((random()*1000000)))
    #generate a num from 0 to 9999999
    print (math.trunc((random()*10000000)))

line()
print ('better integer rand gen')
beg = 1
end = 20
step = 5
left = 1
right = 9

print (randrange(beg, end))
# minimum diff b/w any of the outputed concequent rnd numbers
for i in range (10):
    print (randrange(beg, end, step)) 
line ()
#rand int

x1 = randint(left, right)
print (f"rand int is {randint(left, right)}")

line()
line()

beg = 1
end =10

print(randrange(end))
print(randrange(beg, end))
print(randrange(beg, end, step))
print(randint(left, right))

for i in range(10):
    print(randint(1, 9), end=" ")
print ("")
for i in range(10):
    print(randrange(1, 9), end=" ")
