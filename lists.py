#list data type - contains multiple values in ordered seq
spam= ['string', 3.14, 'boy', 999]
print(spam)

#[] empty list = ' ' empty string
#indexes start from 0
print(spam[3])
print('this is a ' + spam[0])

#list can also contain other list values

ham = [[1,2,3] , 'pig' , 'snail']
print (ham[0])
print(ham[0][1])

#hve negative indexex
print(spam[-1])
print(ham[-3])

#slicing
spam= ['string', 3.14, 'boy', 999]
print(spam[1:-1])
print(spam[1:3])
print(len(spam))

#can do value updates
spam[1]= 'point'
print(spam)

#can be done concatenation and replications

egg= [1,2,3]+[4,5,6]
print(egg)
egg = egg+spam
print(egg)

egg = [1,2,3] * 3
print(egg)

spam= ['string', 3.14, 'boy', 999]
del spam[1]
print(spam)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])


my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(cat)

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(cat)

#enumerate func returns both index of the item in the list and item in the list
#where as range(len(name)) returns only num of items

bacon = ['zophie']
bacon *= 3
print(bacon)

#method - is called on a value
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))# list values have index method 


#adding values - append-end of the list
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.append('add')
print(spam)
spam.insert(2,'hi')
print(spam)
spam.remove('hi')
print(spam)
spam.sort()
print(spam)
spam.sort(reverse= True)
print(spam)
spam.reverse()
print(spam)
print(spam[1])

var1 = 'Zophie'
print(var1[1])
#list is a mutable data type. i.e add , remove or change its values
#string is immutable