l1=[1, 2, 3, 4, 6, 8]

# Using Normal approach
l2=[]        # Creating an empty list 
for i in l1:
    l2.append(i*i)  # Appending the square items in list 2

print(l2)   # Printing the list 2 items

#Using the Listcomprehensive approcah

l2=[i*i for i in l1]   # In this step we are asking to print the sq of num inside the list
l3=[i*i for i in l1 if i>2]  # we can also use if stamt inside this list comp
print(l2)
print(l3)

# Similarly we can use set, dictonary comprehension also

