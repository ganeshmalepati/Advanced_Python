list1 = [1, 2, 3, 4, 6, 7]

# Using normal approch for the counter wise like one by one printing
i=0
for item in list1:
    print(f"The square of item {i+1} is {item*item}")
    i+=1

# Using Enumerate funcation it will increase the counter of a iterator effectively
for i, item in enumerate(list1):
    print(f"The items are {i+1} is {item}")

