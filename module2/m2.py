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