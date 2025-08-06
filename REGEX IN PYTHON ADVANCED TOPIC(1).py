# there are the number of functions depending ways of working
#  search() , match(),  finditer(),  findall()

# SEARCH() FUNCTION:---

# Syntax:- re.search(pattern,data)    pattern:--  the regex pattern you want to search for
#                                  data:-- input string in which you want to search for pattern

import re

pattern = "python"  # pattern to search
data = "python is very powerful and python has lots of features"  # data to search in....

match = re.search(pattern, data)
print(match)
print(type(match))

if match:
    print("found:", match.group())  # match.group function mai ye hame kya found karna hai ye batata hai
else:
    print("not found:")

    print()

# RE.MATCH():--

# Purpose :- search for a pattern at the beginning of a string.
# SYNTAX:- re.match(pattern,string,flags=0)
# pattern :- the regular expression pattern you want to search for.
# data:- input string in which you want to search for pattern.
# Return:- If a match is found at beginning of the string,the string it returns a match object,otherwise it returns none

import re

pattern = "pythoN"  # pattern to search
data = "python is very powerful and python has lots of features"  # data to search in....

match = re.match(pattern, data,re.IGNORECASE)  # here re.IGNORECASE ignor the case sensitive  word (upper case or lower case)
print(match)
print(type(match))

if match:
    print("found:", match.group())  # match.group function mai ye hame kya found karna hai ye batata hai
else:
    print("not found:")

print()

# RE.FINDITER()
# SYNTAX:- re.finditer(pattern,data,flags=0)
# Return:- iterator object containing match info.

