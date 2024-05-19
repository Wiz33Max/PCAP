string = 'hello'
print (ord(string[0]))
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
print (the_string[0])
print (the_string[-1])
print (the_string[-2])
print()
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
'''This slice starts from the
 beginning and includes every
  second character, so it prints adf.
   <index_begining_inclusif:index_end_exclusif:step)
    '''
print(alpha[1::2])

print ('_'*20)
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
print("f" not in alphabet)
print("F" not in alphabet)

a = ['a','b','c','d','e','f']
del a[0]
# cantt do that with a string

a.append("A")
# cant do that with a string either

'''only concatenate and creayte a new string, cause string are immutable
'''

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# Demonstrating min() - Example 1: (with max() the same thing)
# works on lists and strings, but cant be empty!!
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))
print ('\n'+'_'*20+'\n')

# index method (not function)
print("aAbByYzZaA".index("b"))

print ("\n index() method:")
str1 = "Max is Great!"
try:
    print (str1.index("Max"))
    print (str1.index("max"))
except:
    print ("Not Found")    

# list() function creates a list of
# individual eleements of the argiment

print(list("Max"))
print (list({'I':"i", 'A':'a'}))

# Demonstrating the count() method. Number of occurences.
print("abcabc".count("b"))
print('abcabc'.count("d"))

