#   lists i =n python can be used for mutliple things, 
#   and can work similar to arrays as well
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print("\n")

#       this prints out everything       
for x in(mylist):
        print(x)

#       this is called an index, for when you want to print out an individual item from a list
#       the [] in mylist[] serve to choose which item you want, and they start off at 0
mylist = [0,1,2,3,4,5,6,7,8,9,10]
print(mylist[1])
print("\n")


#       this is the code added to make everything work
numbers =[]
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
print("\n")

strings =[]
strings.append("hello")
strings.append("world")
print(strings)
print("\n")

#       here is an example of a little excercise you can do that involves lists
#       it takes the index number from the list and prints it
names = []
names = ["Rayden" , "John", "Ev"]
second_name = names[1]
print("The second name on the names list is %s" % second_name)
print("\n")