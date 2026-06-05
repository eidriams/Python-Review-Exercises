"""Create a Set Class
In this exercise we are going to create a class named Set to emulate an abstract data structure called "set". 
A set is like an array, but it cannot contain duplicate values. 
The typical use for a set is to simply check for the presence of an item. 

First, we will create an add method that adds a value to our set collection as long as the value does not already exist in the set. 
Then we will create a remove method that removes a value from the set collection if it already exists. 
And finally, we will create a size method that returns the number of elements inside the set collection.

Create an add method that adds a unique value to the set collection and returns true if the value was successfully added and false otherwise.

Create a remove method that accepts a value and checks if it exists in the set. If it does, then this method should remove it from the set collection, and return true. 
Otherwise, it should return false. Create a size method that returns the size of the set collection.

Tests:
Waiting:1. Your Set class should have an add method.
Waiting:2. Your add method should not add duplicate values.
Waiting:3. Your add method should return true when a value has been successfully added.
Waiting:4. Your add method should return false when a duplicate value is added.
Waiting:5. Your Set class should have a remove method.
Waiting:6. Your remove method should only remove items that are present in the set.
Waiting:7. Your remove method should remove the given item from the set.
Waiting:8. Your Set class should have a size method.
Waiting:9. The size method should return the number of elements in the collection."""


# myset = set()
# print(myset)
# myset.add(6)
# print(myset)
# myset.add(5)
# print(myset)

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
    

meinset = Set()

print(meinset.add(3))
print(meinset.add(4))
print(meinset.add(8))
print(meinset.size())
print(meinset.add(3))
print(meinset.remove(2))
print(meinset)


miosetto = Set([2,6,4,9,5])
print("Este es miosetto →",miosetto)
miosetto.add(7)
