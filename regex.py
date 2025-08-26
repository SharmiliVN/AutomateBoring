import re

phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
print(match_obj.group())

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
print(mo.group(1)) # Returns the first group of the matched text

print(mo.group(2))  # Returns the second group of the matched text

print(mo.group(0))  # Returns the full matched text

print(mo.group())  # Also returns the full matched text
print(mo.groups())
area_code , main_num = mo.groups()
print(area_code)
print(main_num)

import re
pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())
print(match.group(1))

