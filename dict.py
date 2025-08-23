#dictionary-mutable
#key-value pair
my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print('My cat has ' + my_cat['color'] + ' fur.')
#dict have keys not indexes

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
print('age' in spam.values())
print('age' not in spam.values())
print('age' in spam.items())