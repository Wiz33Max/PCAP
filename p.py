import platform as p
#print (dir(p))
#help (p)
print (p.system())
help (p.system)

# function help
#help (p.platform)
print(p.platform())
# or print(p.platform(1))
print(p.platform(0, 1))
print(f"Processor : {p.machine()}")

print(p.python_version())

print(p.python_build())

print(p.python_compiler())

print(p.python_branch())

print(p.python_implementation())

print(p.python_revision())

print(p.python_version_tuple())

import os
dir(os)

print(os.name)

print(os.getcwd())

print(os.listdir())

print(os.environ)

import os

print(f"HOME: {os.environ.get('HOME')}")


print(f"HOMEPATH: {os.environ.get('HOMEPATH')}")

print(f"PATH : {os.environ.get('PATH')}")

print(f" PYTHONPATH : {os.environ.get('PYTHONPATH')}")

print(f" USERNAME : {os.environ.get('USERNAME')}")

print(f" COMPUTERNAME : {os.environ.get('COMPUTERNAME')}")

print(f" PROCESSOR_IDENTIFIER : {os.environ.get('PROCESSOR_IDENTIFIER')}")
print(f" PROCESSOR_ARCHITECTURE : {os.environ.get('PROCESSOR_ARCHITECTURE')}")
