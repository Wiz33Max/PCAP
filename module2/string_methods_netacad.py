
'''the capitalize() method'''
print ('aBcDefGH'.capitalize())

'''the center method'''
# adding some spaces before and after the string
print ('['+ 'Wiz3Max'.center(20)+ ']')

# The two-parameter variant of center()
#  makes use of the character from the
#  second argument, instead of a space.
print ('['+'WizMax'.center(20,'_')+']')

'''the endswith() and startswitch() method'''
if "I'm a great programmer!".endswith('mer!'):
    print ('Yes, it ends with "mer!"')
else:
    print ('No, it does not end with "mer!"')

print("omega".startswith("meg"))
print("omega".startswith("om"))

'''the find method'''
# it's like index, but dont generate error if not find
# it returns -1 if didnt find. works only with strngs
print ("This".find('is'))
print ("that".find('is'))
print ("_"*30)

# 2nd parameter can set the position from with the find wil start
# 3rd parameter set the upper limit
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = 0
while fnd != -1:
    fnd = the_text.find('the', fnd + 1)
    print(fnd)

'''in'''
print ("his" in "his there")

'''isalnum method'''
# checks if the string contains only digits or alphabetical characters (letters)
alpha_numm_ok1 = "ThisStuffAlnum33"
alpha_numm_ok2 = "33thisOneToo"
alpha_numm_nok1 = "Not alnum."
print (alpha_numm_ok1.isalnum(),\
     alpha_numm_ok2.isalnum(),\
         alpha_numm_nok1.isalnum())

'''is alpha'''
ia = "IsAlpha" 
ina = "Is not Alpha"
print (f"{ia} string isalpha - {ia.isalpha()}")
print (f"{ina} string isalpha - {ina.isalpha()}")

'''isdigit method'''
# checks if the string contains only digits

digit_ok1 = "1234567890"
digit_ok2 = "0123456789"
digit_nok1 = "1234567890a"
print (digit_ok1.isdigit(),\
     digit_ok2.isdigit(),\
         digit_nok1.isdigit())

'''islower method'''
'''isupper method'''
'''isspace'''
#  identifies whitespaces only
print('\n'.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

'''join method'''
#  join lists elemenmts into one string, string from which the method has been invoked is used as a separator
print (", ".join("this"))
print (", ".join(["this","that","other","drother"]))

'''lower and upper method'''
ss = "   ThiS WeLl Hard tO REad  "
print (f"{ss.lower()} then {ss.upper()}")

'''lstrip and rstrip method'''
#  Leading characters soecified in arguments, leading whitespaces - default behaviour.

print (f"[{ss.lstrip()}]")
print (f"[{ss.rstrip()}]")

# can specify the chars to strip if passed as an argument
site = "www.cisco.com"
print (f"[domain is {site.lstrip('www.')}]")

'''replace method'''
# all occurences of  1st arg replaced bu 2nd arg
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))

# 3rd arg limit the number of replacements
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

'''rfind method'''
#rfind() method starts searching for the substring "ta" from the end of the specified indexed range

print("This is it!".rfind("is"))
print("This is it!".find("is"))
print("This is it!".rfind("is", 0, 4))

'''split method'''

print("This is it!".split())

print("This is it!".split("is"))

'''strip() method'''
# combines lstrip() and rstrip()
m = "   amx  "
print (f"[{m}]")
print (f"[{m.strip()}]")

'''swapcase method'''

print("This is it!".swapcase())

'''title method'''
#upercase every 1st character i the strings word
print("This is it!".title())

'''
1. Some of the methods offered by strings are:

capitalize() - changes all string letters to capitals;
center() – centers the string inside the field of a known length;
count() – counts the occurrences of a given character;
join() – joins all items of a tuple/list into one string;
lower() – converts all the string's letters into lower-case letters;
lstrip() – removes the white characters from the beginning of the string;
replace() – replaces a given substring with another;
rfind() – finds a substring starting from the end of the string;
rstrip() – removes the trailing white spaces from the end of the string;
split() – splits the string into a substring using a given delimiter;
strip() – removes the leading and trailing white spaces;
swapcase() – swaps the letters' cases (lower to upper and vice versa)
title() – makes the first letter in each word upper-case;
upper() – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith() – does the string end with a given substring?
isalnum() – does the string consist only of letters and digits?
isalpha() – does the string consist only of letters?
islower() – does the string consists only of lower-case letters?
isspace() – does the string consists only of white spaces?
isupper() – does the string consists only of upper-case letters?
startswith() – does the string begin with a given substring?
'''
