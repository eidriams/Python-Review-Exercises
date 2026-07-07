"""Perform a Subset Check on Two Sets of Data
In this exercise, we are going to perform a subset test on 2 sets of data. 
We will create a method on our Set data structure called isSubsetOf. 
This will compare the first set against the second, and if the first set is fully contained within the second, it will return true.

For example, if setA = ['a','b'] and setB = ['a','b','c','d'], then setA is a subset of setB, so setA.isSubsetOf(setB) should return true.

Tests:
Waiting:1. Your Set class should have a isSubsetOf method.
Waiting:2. The first Set should be contained in the second Set.
Waiting:3. ['a', 'b'].isSubsetOf(['a', 'b', 'c', 'd']) should return true.
Waiting:4. ['a', 'b', 'c'].isSubsetOf(['a', 'b']) should return false.
Waiting:5. [].isSubsetOf([]) should return true.
Waiting:6. ['a', 'b'].isSubsetOf(['c', 'd']) should return false."""

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
    
    def isSubsetOf(self,sett):

        # Compara el primero con el segundo, si el segundo contiene todos los elementos del primero, devuelve True, False de lo contrario
        
        for item in self.items:
            if item not in sett:
                return False
        return True
        
    def isSupersetOf(self,sett):

        # Compara el segundo elemento con el primero, si el primero contiene todos los elementos del segundo, True, False de lo contrario
        return Set(sett).isSubsetOf(self.items)
        # De esta manera se evita repetir codigo ya que los metodos subset y superset son complemetarios
        # for item in sett:
        #     if item not in self.items:
        #         return False
        # return True

    # Hacer que la clase sea iterable para poder llamar
    # print("este inverso →",norte.isSupersetOf(este))
    # Y no producir TypeError 'Set' is not iterable
    
    def __iter__(self):
        return iter(self.items)

oeste = Set(['a', 'b', 'c'])

sur = Set([])

este = Set(['a', 'b'])

norte = Set(['a', 'b', 'c', 'd'])

print("Este →",este.isSubsetOf(['a', 'b', 'c', 'd']))

print("Oeste →",oeste.isSubsetOf(['a', 'b']))

print("Set([]) vacio →",Set([]).isSubsetOf([]))

print("Y este →",este.isSubsetOf(['c', 'd']))

print("Def Set class →",Set(['a', 'b']).isSubsetOf(['a', 'b', 'c', 'd']))

print("\nLos supersets")


print("Este →",este.isSupersetOf(['a', 'b', 'c', 'd']))

print("este inverso →",norte.isSupersetOf(['a', 'b', 'c','d']))

print("este inverso →",norte.isSupersetOf(este))




