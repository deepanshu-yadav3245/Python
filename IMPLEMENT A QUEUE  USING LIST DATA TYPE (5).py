# the queue is linear data structure
# stores item  first in first out(FIFO)manner

# queue operation
# (1) enqueue: Add an item to the queue.
# (2) dequeue: removes an item from the queue.
# (3) front: get the front item from queue.
# (4) rear: get the last item from queue.

l = []
while True:
    c = int(input('''
      1 push Elements
      2 pop first Elements 
      3 front Elements
      4 Display stack 
      5 exit
 
 '''))
    if c == 1:
        n = input("enter the value:-");
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Empty queue")
        else:
            del l[0]
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("first queue value:-", l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("last queue value:-", l[-1])
    elif c == 5:
        print("display queue", 1)
    elif c == 6:
        break;

    else:
        print("invalid operation")
