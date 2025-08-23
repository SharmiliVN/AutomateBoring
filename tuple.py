#tuple use parentheses, like strings are immutable
#can't modify, append Or remove their values

print(type(('hello' ,)))
print(type('hello'))

def eggs(some_para):
    some_para.append('Hello')
spam=[1,2,3]
eggs(spam)
print(eggs(spam))

#copy and deepcopy()
#copy.copy() makes a duplicate copy of a mutable value lika a list or dictionary

import copy

spam=['A', 'B' , 'C']
cheese = copy.copy(spam) #creates a duplicate copy
cheese[1] = 42
print(spam)
print(cheese)


