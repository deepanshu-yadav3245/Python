# the stack is linear data structure
# store item in a last in first out(LIFO) or first in last out(FIFO)

# stack operation
# (1) push=< inserting an element
# (2) pop=< deletion an element (last element)
# (3) peek=< display the last element
# display=< display list

l = []
while True:
    c = int(input('''
        1 push Element
        2 pop Elements 
        3 peek Elements
        4 Display stack 
        5 Exit
    
    '''))

    if c == 1:
        n = input("enter the value")
        l.append(n)
        print(l)
    if c == 2:
        if len(l) == 0:
            print("Empty stack")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("empty stack")
        else:
            print("last stack value", l[-1])
    elif c == 4:
        print("display stack")
    elif c == 5:
        break;
    else:
        print("invalid operation")
