from functools import reduce
# Demontration of map
cube=lambda x:x*x*x
list1=[1,4,6,7,8,9]
a=map(cube, list1)
print(list(a))

#initialze the funtion
#implemnt the list values
#map it using list and function name
#print the values of the map converting it into a list

# Demonstration for filter funtion in a map
graternumber=lambda x: x>65
listOfNumber=[34,67,7,89,45,345,69,100]
d=filter(graternumber, listOfNumber)
print(list(d)) 

# Demonstration for reduce function
sum=lambda x,y:x+y
l1=[23,34,45,56,67,680]
a=reduce(sum, l1)
print(a)


