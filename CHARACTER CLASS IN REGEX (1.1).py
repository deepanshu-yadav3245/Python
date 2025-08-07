# Character class typically refers to a set of characters that can define using regular expressions
# Character classes are used to specify used to specify rang or group of characters you want to search in data

# find digit in given data
import re

pattern = r'[a-z A-Z 0-9]'
data = "the price is $100 Z,Y"

match_iter = re.finditer(pattern, data)

for match in match_iter:
    print(match)


print()

# Condition for password:-- 1.contain at least one digit or at least one uppercase

import re

password = input("Enter the password:")

pattern = '[0-9 A-Z]'

if re.findall(pattern,password):
    print("valid password")
else:
    print("Invalid password")



print()


# REGEX SPECIAL SEQUENCES:--

# In regular expression (regex) use special sequences to represent common character classes or group of character.

# \d:- Matches any digit character                                  \D:- Matches any non digit character,
# \w:- Matches any word character (alphanumeric plus underscore)    \W:- Matches any non word character.
# \s:- Matches any whitespace char (spaces,tabs,newline,etc.)       \S:- Matches any non whitespaces character.
# \b:- Matches a word boundary                                      \A:- startswith
# \Z:- endswith                                                      .:- Matches every character


import re
text = "Hello my phone number is 123"
pattern = r'\d'
result = re.finditer(pattern,text)
for match in result:
    print(match.start(),match.group())

