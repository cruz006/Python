#   this is a tutorial for Python, IN Python
#   you can assign variables values as well 
#   as quotes or really anything you want, 
#    all you need to do is print it
var=3
print("1+2=", var)
var1="do you see what i mean?"
print(var1 + "\n")
#   press enter to see the results

#   Assignments can be done on more 
#   than one variable "simultaneously"
#   on the same line like this
a, b = 3, 4
print(a,b + "\n")

#   This will not work without the str() command
one = 1
two = 2
hello = "hello"
print(str(one)+str(two)+str(hello) + "\n")

#   testing code, this is just to be able
#   to see the difference between 
#   each, and then prints them
mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print("String: %s" % mystring  + "\n")
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat  + "\n")
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint + "\n")

#   message, or msg also works
msg="Hello World!"
print(msg  + "\n")

#    here too is how you can make a whole sentence
helloworld = "hello" + " " + "world"
print(helloworld  + "\n")

#   myint is my interger
#   mystring is my string myfloat is a whole number with a deicaml point to be exact
#   str is equal to	Text
#   int, float, complex are all Numeric
#   list, tuple, range count as Sequences
#   dict is for Mapping
#   set, frozenset are for Sets
#   bool is Boolean
#   bytes, bytearray, memoryview are all Binary
