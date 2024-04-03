from functools import reduce

def graternumber(m, n):
    if m>n:
        return m
    return n

list1=[23,45,56,67,7008,34,456,678,453]
a=reduce(graternumber, list1)
print(a)