#function is a mini program within a program
#python has several built-in finc such as len, print,input

def hello(name):
    print('write your own name ' + name)
hello('sharmili')

import random
for i in range(100):  # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print()  # Print one newline at the end.

def spam():
    eggs = 'SPAMSPAM'
    bacon()
    print(eggs)  # Prints 'SPAMSPAM'

def bacon():
    ham = 'hamham'
    eggs = 'BACONBACON'
spam()

def spam():
    print(eggs)  # Prints 'GLOBALGLOBAL'
eggs = 'GLOBALGLOBAL'
spam()
print(eggs)

