import ctypes


class Meralist:
    
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)
        
    def __len__(self):
        return self. n    # Find the length of a list
       
        
    def __make_array(self,capacity):
         # create a C type array (static,referential) with size capacity
         return (capacity*ctypes.py_object)()


L = Meralist()
len(L)
