#   this is the user input and output file
#   this is how you can get a user name
import statistics

def greeting():
    name = input("hello, what is your name?\n")
    print("Hello there " + name + " how are you?\n")

def avg():
    numbers = input("put a list of numbers here:\n")
    sums = sum(numbers)
    result = (sums)/(numbers)
    print (result)


#   this is where you can choose which function to run
def run_function(func_name):
   if func_name == "greeting":
        greeting()
   elif func_name == "avg":
        avg()
   else:
        print("Invalid function name")
        
var1 = input("Which function would you like to run today? Your options are: greeting, avg\n")
run_function(var1)