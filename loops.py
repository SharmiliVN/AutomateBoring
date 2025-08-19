while True: #this is infinite loop , its while loop where the condition is always true.
    print("Enter your name- ")
    name = input('>')
    if name == 'yourname':
        break
print('thank you !')

while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted.')   

print('hello')
for i in range(5):
    print('on this iteration, i is set to ' + str(i))
print('goodbye !')

#you can use continue and break statements only inside while and for loops
#add up all numbers
total = 0 
for i in range(101):
    total = total + i
print(total)

for i in range(12,16):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(0,-5,-1):
    print(i)

#for loop runs the loop number of times specified
#while loop runs as long as the condition is true


#MODULES
import random

for i in range(5):
    print(random.randint(1,5))
    
import sys

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')


from random import *
sec_no = randint(1,20)
print('i am thinking a number b/w 1 to 20')

for guess in range(1,7):
    print('take a guess.')
    guess= int(input('>'))
               
    if guess < sec_no:
        print('your guess is too low.')
    elif guess > sec_no:
        print('your guess is too high.')
    else:
        break
if guess == sec_no:
    print('good job ! you got it in ' + str(guess) + 'guesses!')
else:
    print('nope.the number was ' +str(sec_no))
    