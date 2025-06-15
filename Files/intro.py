# -------------------
# -- File Handling --
# -------------------

import os

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

#print(os.path.abspath(__file__))

#file = open(r"D:\My_Progict\Software & Programming\Python\Files\tareq.txt")