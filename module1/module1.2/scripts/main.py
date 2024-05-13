from sys import path
import os
path.append('..\\modules')

import os
import sys

''' insert a module subfolder in PATH environement variable'''
# Get the parent folder of the current script
file_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(file_folder)
# Append the modules folder to the sys.path list
sys.path.append(os.path.join(parent_folder, "modules"))
#print (sys.path)


# Now you can import the module
import module

print (module.__counter)
list1 = [2,3,4,3,2]
x = module.suml(list1)
print (x)