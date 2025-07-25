# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element 
# -----------------------------------------------------------

myString = "Tareq"

myList = [1, 2, 3, 4, 5]

# for letter in myString:
#     print(letter, end=" ")

# for number in myList:
#     print(number, end=" ")

#print(next(myString)) # myString Object is not an iterator. ... " Is an iterable ".

# myIterator = iter(myString)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

for letter in iter("Al_kushari"):
    print(letter, end=" ")