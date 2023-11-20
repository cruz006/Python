#   this will be for anything math related and basic operators

#   ok so this is where you can choose which function to run!!!
from enum import Enum

def basics():
    #   using print you can put the problem you want calculated, and the answer is printed 
    print(5 + 2)

    #   using quotes you can show the whole problem
    print("5 + 2 = 7")
    #   Subtraction
    print(5 - 2)

    #   Multiplication
    print(5 * 2)

    #   Division
    print(5 / 2)

    #   Exponent
    print(5 ** 2)
    #   This is the same as 5 * 5

    #   Floor Division
    print(5 // 2)

    #   Modulus
    print(5 % 2)
    firstName = "Rando"

    introduction = "Hi, my name is " + firstName + "."

    print(introduction)

    #   this i show you can add thinks to already established varibales
    var1 = 100
    print(var1)
    var1 += 10
    print(var1)

    var2 = 200
    print(var2)
    var2 *= 7
    print(var2)
    
    var3 = 300
    print(var3)
    var3 /= 10
    print(var3)

    var4 = 400
    print(var4)
    var4 **= 2
    print(var4)

    var5 = 500
    print(500)
    var5 //= 5

    var6 = 600
    print(var6)
    var6 %= 6
    print(var6)

def average():
    number = 1 + 2 * 3 / 4.0
    print(number, "\n")

    average = sum(range(1,11))/10
    print(average, "\n")

    #   this is how you can find an average
    average = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)/10
    print(average, "\n")

def division():
    remainder = 11 % 3
    print(remainder, "\n")
    #   here is an example of division, but this is called MOD
#   When it is 11/3, it can be divded 3 times which equals 9, and then the remainder is stored, which is 2
    remainder = 11 % 3
    print(remainder, "\n")

def multiplication():
    multiply = 7 * 2
    print(multiply, "\n")

def cubed():
    cubed = 7 ** 2
    print(cubed, "\n")

def lists():
    even_numbers = [2, 4, 6, 8]
    odd_numbers = [1, 3, 5, 7]
    all_numbers = odd_numbers + even_numbers
    print(all_numbers, "\n")
    #    then this is how you can use lists and operators to combine them into one
    even_numbers = [2,4,6,8]
    odd_numbers = [1,3,5,7]
    all_numbers = odd_numbers + even_numbers
    print(all_numbers, "\n")

#   here is a way that you can use the operators to check how many items are in one list
    x = object()
    y = object()

# this is how you can combine
    x_list = [x] * 10
    y_list = [y] * 10
    big_list = x_list + y_list

#   this is how you can round numbers
    print("this is how you round 3.567890 = "+ str(round(3.567890)))

#   then this is when you check how many are in each
#   len is a function that retruns the length of an object, which is why we made the x and y list an object
    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list) + "\n")

def squared ():
#   this is how you can use numbers to a power
    squared = 7 ** 2
    print(squared, "\n")

def repeat():
#   this is how you can use repeating words 
    lotsofhellos = "hello " * 10
    print(lotsofhellos, "\n")


def run_function(func_name):
   if func_name == "basics":
        basics()
   elif func_name == "average":
        average()
   elif func_name == "division":
        division()
   elif func_name == "multiplication":
        multiplication()
   elif func_name == "cubed":
        cubed()
   elif func_name == "lists":
        lists()
   elif func_name == "squared":
       squared()
   elif func_name == "repeat":
       repeat()
   else:
        print("Invalid function name")
        
var1 = input("Which function would you like to run today? Your options are: basics, average, division, multiplication, cubed, lists, square, repeat" + "\n")
run_function(var1)

#   another way to do this
'''
class Function(Enum):
    BASICS = 1
    AVG = 2
    DIV = 3
    MULT = 4
    LIST_OPS = 5

def run_function(func_name):
    
   func_name = Function[func_name.upper()]
   
   if func_name == Function.BASICS:
        basics()
   elif func_name == Function.AVG:
        avg()
   elif func_name == Function.DIV:
        div()
   elif func_name == Function.MULT:
        mult()
   elif func_name == Function.LIST_OPS:
        list_ops()
   else:
        print("Invalid function name")
    '''

#   another way too
'''
def run_function(func_name):
   func_name = Function[func_name.upper()]
   
   match func_name:
       case Function.BASICS:
           basics()
       case Function.AVG:
           avg()
       case Function.DIV:
           div()
       case Function.MULT:
           mult()
       case Function.LIST_OPS:
           list_ops()
       case _:
           print("Invalid function name")
'''
