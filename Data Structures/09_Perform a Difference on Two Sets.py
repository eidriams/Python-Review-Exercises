"""Perform a Difference on Two Sets of Data
In this exercise we are going to perform a difference on 2 sets of data. We will create a method on our Set data structure called difference. 
A difference of sets should compare two sets and return the items present in the first set that are absent in the second. 
This method should take another Set as an argument and return the difference of the two sets.

For example, if setA = ['a','b','c'] and setB = ['a','b','d','e'], then the difference of setA and setB is: setA.difference(setB) = ['c'].

Tests:
Waiting:1. Your Set class should have a difference method.
Waiting:2. Your difference method should return the proper collection."""

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
    
    def intersection(self,sett):

        interset = set()

        for item in self.items:
            if item in sett:
                interset.add(item)            
        
        return interset
    
    def difference(self,sett):

        diffeset = set()

        for item in self.items:
            if item not in sett:
                diffeset.add(item)

        return diffeset
                


setA = ['a','b','c']
setB = ['a','b','d','e']

sete = Set(setA)
gibernau = Set(setB)

print(sete.difference(setB))
print(gibernau.difference(setA))