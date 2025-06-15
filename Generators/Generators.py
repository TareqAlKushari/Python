# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function with "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By using next() it Resume From where it Called "yield" Not from Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4

# print(myGenerator())

myGen = myGenerator()

print(next(myGen))

print("Hello From Python: ")

print(next(myGen))

print("Hello From Python: ")

print(next(myGen))

print("#" * 50)

for number in myGenerator():
    print(number)

print("#" * 50)

for number in myGen:
    print(number)