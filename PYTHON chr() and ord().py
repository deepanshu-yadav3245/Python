# PYTHON CHR() FUNCTION

# this takes in an integers i and converts it to a character c,so it returns a character  string
# example= convert integer 65 to ASCII character('A')
#           y= chr(65)
#            print(type(y),y)

a = 78
print(chr(a))

# THE ORD() FUNCTION

# this takes a single unicode character (string of length 1)and return an integer so the format is
#  convert ASCII unicode character 'A' to 65
#  y = ord('A')
#   print(type(y),y)

h = 'a'
print(ord(h))


# PYTHON STRING FORMAT() METHOD

# the format() method formats the specified values and insert them inside placeholder.
# the placeholder is defined using curly brackets{} Read more about the placeholder in the placeholder section below

w = "welcome {} to {} Wscubetech".format("hello",100)
print(w)