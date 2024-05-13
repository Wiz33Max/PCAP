''' imoprt pack.zip package
by getting the main file location, concatenate it with the module
pack.zip and appending it to the PATH variable.
Then we can import any of the modules within that will make
the other modules avalible '''


from sys import path as path_s
from os import path as path_o

print (path_o.dirname(__file__))
pack_path = path_o.join(path_o.dirname(__file__),"pack.zip")

print (pack_path)
path_s.append(pack_path)
print (path_s)
import extra.iota
import extra.good.best.tau as T

print (T.FunT())

print (extra.iota.FunI())