# --------------------------------------------
# -- Decorators => Function with Parameters --
# --------------------------------------------

def myDecorator(func): # Decorator

    def nestedfunc(num1, num2): # Any Name Its Just For Decoration
        
        if num1 < 0 or num2 < 0:

            print("Beware One or Two of The Numbers Is Less Than Zero:")

        func(num1, num2) # Execute Function

    return nestedfunc # Return All Data

def myDecoratorTwo(func): # Decorator

    def nestedfunc(num1, num2): # Any Name Its Just For Decoration

        print("Coming From Decorator Two:")

        func(num1, num2) # Execute Function

    return nestedfunc # Return All Data


@myDecorator
@myDecoratorTwo
def calculate(n1, n2):

    print(n1 + n2)

calculate(-5, 80)