"""Perform a Union on Two Sets
In this exercise we are going to perform a union on two sets of data. 
We will create a method on our Set data structure called union. 
This method should take another Set as an argument and return the union of the two sets, excluding any duplicate values.

For example, if setA = ['a','b','c'] and setB = ['a','b','d','e'], 
then the union of setA and setB is: setA.union(setB) = ['a', 'b', 'c', 'd', 'e'].

Tests:
Waiting:1. Your Set class should have a union method.
Waiting:2. The union of a Set containing values ["a", "b", "c"] and a Set containing values ["c", "d"] 
           should return a new Set containing values ["a", "b", "c", "d"]."""


# Reciclamos la clase Set() creada anteriormente

class Set():
    
    def __init__(self,tupla = None):

        if tupla is None:

            self.items = set()
        
        else:

            self.items = set(tupla)

    

    def add(self, item):
        
        if item in self.items:
            print(f"Item ({item}) already in set, not duplicates allowed")
            return False
        else:
            print(f"Item ({item}) added to {self} successfully")
            self.items.add(item)
            return True 


    def remove(self,item):
        
        if item in self.items:
            print(f"Item ({item}) removed successfully")
            self.items.remove(item)
            return True
        
        else:
            print(f"Item ({item}) not in set, cannot be removed")
            return False


    def size(self):
        
        return f"Number of items in collection → {len(self.items)}"
    
    def __str__ (self):

        return str(self.items)
    
    def union(self,sett):

        uniset = set()
        
        for item in sett:

            if item in self.items:

                uniset.add(item)
        
        return uniset





unifythis = Set(["a", "b", "c"])

withthis = ['a','b','d','e']

withthat = ["a", "b", "j", "k"]

print(unifythis.union(withthis))
print(unifythis.union(withthat))

