"""Create a Circular Queue
In this challenge you will be creating a Circular Queue. A circular queue is a queue that writes to the end of a collection then begins overwriting itself at the beginning of the collection. 
This type of data structure is useful in certain situations. 

For example, a circular queue can be used for streaming media. Once the queue is full, new media data will overwrite old data.

A good way to illustrate this concept is with an array of length 5:

[null, null, null, null, null]
 ^Read @ 0
 ^Write @ 0

Here the read and write are both at position 0. Now the queue gets 3 new records a, b, and c. Our queue now looks like:

[a, b, c, null, null]
 ^Read @ 0
          ^Write @ 3
As the read head reads, it can remove values or keep them:

[null, null, null, null, null]
                   ^Read @ 3
                   ^Write @ 3
Now we write the values d, e, and f to the queue. Once the write reaches the end of the array it loops back to the beginning:

[f, null, null, d, e]
                ^Read @ 3
    ^Write @ 1

This approach requires a constant amount of memory but allows files of a much larger size to be processed.

In this challenge we will implement a circular queue. 
The circular queue should provide enqueue and dequeue methods which allow you to read from and write to the queue. 

The class itself should also accept an integer argument which you can use to specify the size of the queue when created. 

When you enqueue items to the queue, the write pointer should advance forward and loop back to the beginning once it reaches the end of the queue. 

The enqueue method should return the item you enqueued if it is successful; otherwise it will return null.

Likewise, the read pointer should advance forward as you dequeue items. When you dequeue an item, that item should be returned. If you cannot dequeue an item, you should return null.

The write pointer should not be allowed to move past the read pointer (our class won't let you overwrite data you haven't read yet) 
and the read pointer should not be able to advance past data you have written.

Tests:
Waiting:1. The enqueue method should add items to the circular queue.
Waiting:2. You should not enqueue items past the read pointer.
Waiting:3. The dequeue method should dequeue items from the queue.
Waiting:4. After an item is dequeued, its position in the queue should be reset to null.
Waiting:5. Trying to dequeue past the write pointer should return null and does not advance the write pointer."""


# Seguimos reutilizando la clase Queue creada



write_pointer = '^Write'
read_pointer = '^Read'

class Queue():
    
    def __init__ (self, size):

        # Tamaño de la lista de cola circular, este ya no va a cambiar tanto si hay enqueue como dequeue
        self.size = size

        # Lista vacía de elementos
        self.items = list(size*['null'])

        #Contador
        self.count = 0

        # Punteros
        self.wpointer = 0
        self.rpointer = 0
        self.write = list(size*['    '])
        self.read = list(size*['    '])
        

    def __str__(self):
        return str(self.items)

    
    def enqueue(self,item):

        # Cuando se mete en cola un elemento, la lista queda del mismo tamaño
        if self.isFull():
            print("Lista llena, haz dequeue primero para añadir mas elementos")
            return False
        else:
            # Enqueue     
            self.items[self.wpointer] = item

            # Avance del Write Pointer
            self.wpointer = (self.wpointer + 1) % self.size
            self.count += 1
                    
            print(self.items)
            print(f"^Write'@ {self.wpointer}")
            print(f"^Read'@ {self.rpointer}\n")

        return self.items

    def dequeue(self):
        
        if self.isEmpty():
            print("Lista vacía, no hay mas elementos en cola de lectura")
            return False
        
        else:
        
            # Dequeue
            self.items[self.rpointer] = 'null' 
            self.count -= 1  

            # Avance del Read Pointer
            self.rpointer = (self.rpointer + 1) % self.size
            print(self.items)
            print(f"^Read'@ {self.rpointer}")
            print(f"^Write'@ {self.wpointer}\n")

        return self.items


    def isEmpty(self):
        # Si está vacía no se puede hacer dequeue
        # Que esté vacia quiere decir que write y read esten en 0
        # Pueden estar en cero y la lista esté llena pq Write haya vuelto al principio, cuidado con eso
        # Que todos los elementos de la lista sean 'null'

        return self.count == 0

    
    def isFull(self):
        # Si está llena no se puede hacer enqueue
        # Estar llena significa que write está al final de la lista,o que ha vuelto a 0
        # ya que marca la posicion siguiente despues de añadir elemento
        # si añado en 1, write marca 2
        
        return self.count == self.size
        
    def clear(self):
        self.items = ['null'] * self.size
        self.wpointer = 0
        self.rpointer = 0
        self.count = 0


    
circ = Queue(5)
print(circ)


print(circ.isEmpty())

circ.dequeue()

circ.enqueue('a')

circ.enqueue('b')

circ.enqueue('c')

circ.enqueue('d')

circ.enqueue('e')

print("Debe de ser True despues de añadir 'e' ->" ,circ.isFull())

circ.dequeue()

circ.enqueue('f')

print("Full? ->",circ.isFull())

circ.enqueue('g')

circ.dequeue()

circ.enqueue('g')

circ.dequeue()
circ.dequeue()
circ.dequeue()
circ.dequeue()
circ.dequeue()
circ.dequeue()




