#boolean values can be stored in variables
print(42 == 42)
print('hello' == 'hello')
print( True and True)
print( (4<5) and (5<6))

#a condition always evaluates to a boolean value , yess/no
# “If this condition is true, do this thing, or else do this other thing.” Other code you’ll write is the same as saying, “Keep repeating these instructions as long as this condition continues to be true.”

# "if" - will execute if the condition is true

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

#elif statemenst are automatically skipped once a true condition has found
# order is imp in elif statements

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)

print('Enter either 1 or 2 in spam :')
spam = int(input('> '))
if spam == 1:
    print('Hello')
elif spam == 2 :
    print('Howdy')
else:
    print('Greetings !')