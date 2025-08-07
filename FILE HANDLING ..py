# (1) FILE HANDLING:-
# What is file:-File are named location on disk to store information.
#               They are used to store data permanently.
#               Data is store in non-volatile memory.
# (2) TYPE OF FILES:- (1) Text Files:-   Store data in the form of character.it used to store data and string.
#                 (2) Binary Files:- Store data in the form of bytes(group of 8 bits).

# (3) WHAT IS FILE HANDLING:- File handling means that Opening a file. Performing some operation on it. closing file.
#                         File handling use to store the data permanent in the file.

# (4) OPENING FILE:-
# Python provide an in-built function open() to open a file
# syntax:- f=open(filename,mode='r') here filename:- file to be accessed, mode:- access mode(purpose to open file)
#                                                    f:- file handler file pointer

# (5) SYNTAX OF FILE HANDLING:

# f = open(filename,mode='r',buffering,encoding=none,errors=none,newline=none,closefd=true)

# (6) HERE BUFFERING MEANS:-
# Positive integer value used to set buffer size for file.
# In text mode,buffer size can be 0.

# (7) ENCODING:-
# Encoding type used to decode and encode file.
# Should be used  in text mode only.
# Default value depend on OS, for windows:-cp1252

# (8) ERROR:-
# Represent how encoding and decoding error are to be handled
# cannot be used in binary mode.
# some standard value are:- strict,ignor,replace etc

# (9) NEWLINE
# it can be \n,\r,\r\n.

f = open('hello.text', mode='r', buffering=10, encoding='utf-8')
if f:
    print("opened")
print(f)

# (10) CLOSING A FILE:-
# After performing operation,we have to close a file.
# close():-- function used to close a file.
# SYNTAX:- file_handler.close()

# (11) FILE OBJECT METHOD:-(1)-Readable(), (2)-writeable()
# Readable:- This method is used to check whether file is readable or not.
# writeable:- This method is used to check whether file is writable or not.

f = open("hello.txt", mode='w+')
print(f.readable())
print(f.writable())
f.close()

# (12) CHECK FILE EXIST OR NOT:-
# Isfile():-This method is used to check file exist on not.This method belong to path module which is sub-module of os
# Syntax:- import os
#          os.path.isfile(filename)

import os
print(os.path.isfile("hello.text"))

# (13) WAYS OF CLOSING FILES:
# Normal Way, Using exception handling, With statement

# NORMAL WAYS:-f=open('filename',mode='r')
#              f.close

# USING EXCEPTION HANDLING: try:
#                               f=open('filename',mode='r')
#                           finally:
#                                   f.close()

# WITH STATEMENT:
# with open('filename',mode='r') as f:
#           data=f.read()
#           print(data)

# (14) MODE OF OPENING FILE:-When you open a file for operation you have to specify mode.mode specifies the purpose opening file
# Two type of modes: (1):Text modes (2):Binary modes.

# TEXT MODE:-   When you open a file in text modes python treat its content as "str" type Store data in binary form
# BINARY MODE:- When you open a file for binary mode,python uses the  data without any encoding.binary mode file reflect the raw data directly in the file
#               Python treat file content as "bytes" type these modes are used while dealing with non-text files like images audio video etc.


