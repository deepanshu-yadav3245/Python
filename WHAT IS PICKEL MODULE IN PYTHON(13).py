# The pickle module a fundamental,but powerful algorithm for serializing and deserializing a python object structure
# Storing data with pickle are :- boolean,integer,float,complex number,string,tuple,list,set,and dictionaries.
# To use pickle, start by importing it in python.
#                (  import pickle    )

# PYTHON PICKLE FUNCTIONS:----
# (1) Dump():- This function is called to serialize an object hierarchy.
# (2) load ():- this function is called to de-serialize an object hierarchy.

import pickle

l = [10, 20, 30, 40]

file = open("writedata,txt", "wb")

pickle.dump(l, file)

file.close()
print(l)
