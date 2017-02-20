import sys
import os

from RunCompare import start_comparison

# ----
# main
# ----

if __name__ == "__main__" :
    index = 2
    while(index <= 2) :
        file_name = 'images/square_' + str(index) + '.png'
        script = "echo " + file_name + " > RunCompare.in"
        os.system(script)
        os.system ("python RunCompare.py < RunCompare.in")
        index += 1