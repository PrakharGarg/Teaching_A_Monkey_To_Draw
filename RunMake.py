import sys
import os

from RunCompare import start_comparison
from MakePhoto import make_photo

# ----
# main
# ----

if __name__ == "__main__" :
    index = 2
    while(index <= 50000) :
        make_photo(index)
        file_name = 'images/square_' + str(index) + '.png'
        script = "echo " + file_name + " > RunCompare.in"
        os.system(script)
        os.system ("python RunCompare.py < RunCompare.in")
        index += 1