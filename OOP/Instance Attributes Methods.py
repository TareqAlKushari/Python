# ------------------------------------------
# -- Instance Attributes & Methods Part 1 --
# ------------------------------------------

class Member:
    def __init__(self, first_name, middle_name, last_name):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

    def full_name(self):

        return f"{self.fname} {self.mname} {self.lname}"


member_one = Member("Tareq", "Mohammed", "Al_Kushari")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mohammed", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.full_name())
print(member_two.full_name())
print(member_three.full_name())