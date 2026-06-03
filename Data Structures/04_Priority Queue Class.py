"""Create a Priority Queue Class
In this challenge you will be creating a Priority Queue. 
A Priority Queue is a special type of Queue in which items may have additional information which specifies their priority.
This could be simply represented with an integer. 
Item priority will override placement order in determining the sequence items are dequeued. 
If an item with a higher priority is enqueued after items with lower priority, the higher priority item will be dequeued before all the others.

For instance, let's imagine we have a priority queue with three items:

[['kitten', 2], ['dog', 2], ['rabbit', 2]]

Here the second value (an integer) represents item priority. If we enqueue ['human', 1] with a priority of 1 (assuming lower priorities are given precedence) 
it would then be the first item to be dequeued. The collection would look like this:

[['human', 1], ['kitten', 2], ['dog', 2], ['rabbit', 2]]

We've started writing a PriorityQueue in the code editor. You will need to add an enqueue method for adding items with a priority, 
a dequeue method for removing and returning items, a size method to return the number of items in the queue, a front method to return 
the element at the front of the queue, and finally an isEmpty method that will return true if the queue is empty or false if it is not.

The enqueue should accept items with the format shown above (['human', 1]) where 1 represents the priority. dequeue and front should return only the item's name, not its priority.

Tests:
1. Your PriorityQueue class should have a enqueue method.
2. Your PriorityQueue class should have a dequeue method.
3. Your PriorityQueue class should have a size method.
4. Your PriorityQueue class should have a front method.
5. Your PriorityQueue class should have an isEmpty method.
6. Your PriorityQueue class should correctly keep track of the current number of items using the size method as items are enqueued and dequeued.
7. The front method should return the correct item at the front of the queue as items are enqueued and dequeued.
8. The isEmpty method should return true when the queue is empty.
9. The priority queue should return items with a higher priority before items with a lower priority and return items in first-in-first-out order otherwise."""


# Ya tenemos la clase Queue, asique la paso aqui para modificarla en función de lo que se pide


class Queue():
    
    # Los objetos de clase que vamos a crear son sublistas de 2 elementos (item,prioridad)
    def __init__ (self, arr = None):
        if arr is None:
            self.items = []
        else:
            self.items = list(arr)

    def __str__(self):
        return str(self.items)

    # Aqui habrá que definir la prioridad que tendra cada elemento añadido, valor mas bajo → mayor prioridad
    def enqueue(self,item):
        # Repasamos los elementos de la lista para comprobar prioridad con respecto a la del elemento que vamos a añadir
        if self.isEmpty():
            self.items.append(item)
            return
        else:            
            for i in range(len(self.items)):                
                if self.items[i][1] > item[1]:                    
                    self.items.insert(i,item)
                    # importante usar return para no seguir iterando cuando ya se ha insertado el elemento
                    return
        # Si no encuentra posicion quiere decir que tiene la prioridad de mayor valor y va al final          
        self.items.append(item)

    def dequeue(self):
        
        if self.isEmpty():
            raise IndexError("Queue vacía")
        
        print("\nElemento saliente →", self.items.pop(0))
        print("→ Cola:\n",self.items)
         
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
        print("Primero en la cola → ",self.items[0])
        return self.items[0]
    
    def tail(self):
        if self.isEmpty():
            raise IndexError("Queue vacía")
        return self.items[-1]
    

prueba = Queue()
prueba.enqueue(["leon",5])
print(prueba)
prueba.enqueue(["rata",3])
print(prueba)
prueba.enqueue(["gatito",2])
print(prueba)
prueba.enqueue(["perrete",1])
print(prueba)
prueba.enqueue(["hipopotamo",4])
print(prueba)
prueba.enqueue(["caramelo",6])
print(prueba)
prueba.dequeue()


# # prueba = Queue([["gato",2],["perro",4]])
# # print(prueba)
# prueba2 = Queue()
# print(prueba2)
# prueba2.enqueue(["leon",5])
# print("\n")
# prueba2.enqueue(["pajaro",4])
# # prueba2.enqueue(["cerdo",1])
# print(prueba2)
# prueba2.enqueue(["gatito",3])
# # print(prueba)
# # prueba.front()
# prueba2.front()