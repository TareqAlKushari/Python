# ---------------------------------
# -- Modules => Built in Modules --
# ---------------------------------
# [1] Modules is A File Contain A Set of Functiona
# [2] You Can Import Module in Your App to Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own  Modules
# [5] Modules Saves Your Time 
# ---------------------------------------------------

# Import Main Module
# import random
# print(random)
# print(f"Print Random Float Number {random.random()}")

# Show All Functiona Inside Module
# import random
# print(dir(random))

# Import One or Two Functiona From Module
from random import randint, random
print(f"Print Random Integer Number {randint(100, 900)}")
print(f"Print Random Float Number {random()}")