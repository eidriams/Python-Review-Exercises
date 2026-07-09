"""Create a Stack Class
In the last section, we talked about what a stack is and how we can use an array to represent a stack. 
In this section, we will be creating our own stack class. Although you can use arrays to create stacks, 
sometimes it is best to limit the amount of control we have with our stacks. 
Apart from the push and pop method, stacks have other useful methods. 
Let's add a peek, isEmpty, and clear method to our stack class.

Write a push method that pushes an element to the top of the stack, 
a pop method that removes and returns the element on the top of the stack, 
a peek method that looks at the top element in the stack, 
an isEmpty method that checks if the stack is empty, and 
a clear method that removes all elements from the stack. 


Tests:
Waiting:1. Your Stack class should have a push method.
Waiting:2. Your Stack class should have a pop method.
Waiting:3. Your Stack class should have a peek method.
Waiting:4. Your Stack class should have a isEmpty method.
Waiting:5. Your Stack class should have a clear method.
Waiting:6. The peek method should return the top element of the stack
Waiting:7. The pop method should remove and return the top element of the stack
Waiting:8. The isEmpty method should return true if a stack does not contain any elements
Waiting:9. The clear method should remove all element from the stack"""


class Stack():

    def __init__(self,array = None):

        if array is None:
            self.items = []
        else:
            self.items = list(array)
        
    
    def __str__(self):
        return str(self.items)
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty stack")
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty stack")
        return self.items[-1]
    
    def clear(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    

test1 = [4,6,23,2,7,2]
stacky = Stack()
hutch = Stack(test1)
stacky.push(5)
print(stacky,hutch)





