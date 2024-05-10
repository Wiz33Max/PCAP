# V1 import math
from math import *

class Main:
    def main(self):
        # V1 self.value = str(math.sin(math.pi/2))
        self.value = str(sin(pi/2))

        self.value = self.value.rstrip('.0')
        print (self.value)

if __name__=="__main__":
    instance = Main()  # Create an instance of the Main class
    instance.main() # Call the main method od the Main class instance