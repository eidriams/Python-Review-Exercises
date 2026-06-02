"""Create a Queue Class
Like stacks, queues are a collection of elements. But unlike stacks, queues follow the FIFO (First-In First-Out) principle. 
Elements added to a queue are pushed to the tail, or the end, of the queue, and only the element at the front of the queue is allowed to be removed.

We could use an array to represent a queue, but just like stacks, we want to limit the amount of control we have over our queues.

The two main methods of a queue class is the enqueue and the dequeue method. 
The enqueue method pushes an element to the tail of the queue, and the dequeue method removes and returns the element at the front of the queue. 
Other useful methods are the front, size, and isEmpty methods.

Write an enqueue method that pushes an element to the tail of the queue, a dequeue method that removes and returns the front element, 
a front method that lets us see the front element, a size method that shows the length, and an isEmpty method to check if the queue is empty.

Tests:

1. Your Queue class should have a enqueue method.
2. Your Queue class should have a dequeue method.
3. Your Queue class should have a front method.
4. Your Queue class should have a size method.
5. Your Queue class should have an isEmpty method.
6. The dequeue method should remove and return the front element of the queue
7. The front method should return value of the front element of the queue
8. The size method should return the length of the queue
9. The isEmpty method should return false if there are elements in the queue
"""

class Queue():
    
    def __init__ (self, arr = None):
        if arr is None:
            self.items = []
        else:
            self.items = list(arr)

    def __str__(self):
        return str(self.items)

    # Poner elemento en la cola siguiendo FIFO (First In, First Out)
    # First in quiere decir que insertamos en indice -1, First Out que sale indice 0
    # front [1,2,3,4] back, entra por back, con un append, y sale por front con un pop(0)
    def enqueue(self,item):
        self.items.append(item)


    def dequeue(self):
        
        if self.isEmpty():
            raise IndexError("Queue vacía")
         
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def clear(self):
        self.items = []

    def front(self):
        if self.isEmpty():
            raise IndexError("Queue vacía")
        return self.items[0]
    
    def tail(self):
        if self.isEmpty():
            raise IndexError("Queue vacía")
        return self.items[-1]
    

cola = Queue([1,2,3,4,5,6,7])
print(cola)
cola.enqueue(300)
print(cola)
print("Elemento dequeado:",cola.dequeue())
print(cola)
print(cola.size())
print(cola.isEmpty())
print(cola.front())
print(cola.tail())
cola.clear()
print(cola)
print(cola.isEmpty())


