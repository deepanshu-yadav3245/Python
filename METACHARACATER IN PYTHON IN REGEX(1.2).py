# Metacharacter are special character that affect how the regular expression around them are interpreted
# Metacharacter in regex:--
# . (DOT) , ^ (Caret), $ (Dollar), * (asterisk), + (plus) , ? (Question mark), [] (Square bracket), | (pipe), \ (backslash)


# . (DOT)
# inside the regular expression, a dot represent any character expect the new line character,which is \n.
import re
data = "hello\nworld"
pattern = r'.'
matches = re.finditer(pattern,data)
for match in matches:
    print(match)

print()



# + (plus)
# means preceding expression or character should repeat one or more times with as many repetition as possible.

import re
data = "hello,world"
pattern = r'l+'
matches = re.finditer(pattern,data)
for match in matches:
    print(matches)