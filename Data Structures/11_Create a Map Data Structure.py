"""Create a Map Data Structure
The next few challenges will cover maps and hash tables. Maps are data structures that store key-value pairs. 
Maps provide rapid lookup of stored items based on key values and are very common and useful data structures.

Let's get some practice creating our own map. 
What if we wanted to define custom operations? 


Create the following methods and operations on the Map object:

add accepts a key, value pair to add to the map.
remove accepts a key and removes the associated key, value pair
get accepts a key and returns the stored value
has accepts a key and returns true if the key exists or false if it doesn't.
values returns an array of all the values in the map
size returns the number of items in the map
clear empties the map
Tests:
Waiting:1. The Map data structure should exist.
Waiting:2. The Map object should have the following methods: add, remove, get, has, values, clear, and size.
Waiting:3. The add method should add items to the map.
Waiting:4. The has method should return true for added items and false for absent items.
Waiting:5. The get method should accept keys as input and should return the associated values.
Waiting:6. The values method should return all the values stored in the map as strings in an array.
Waiting:7. The clear method should empty the map and the size method should return the number of items present in the map."""

# Viene a ser crear la clase Map y añadir estos metodos


class Map():

    def __init__(self, inidata = None):
        
        
        # Con isinstance
        
        self._dict = {} # con _ para tratarlo como interno 

        if inidata:
            if isinstance(inidata,dict):
                self._dict.update(inidata)
            
            elif isinstance(inidata, Map):
                self._dict.update(inidata._dict)
            
            else:
                # Asumiendo un iterable con pares tipo (k,v)
                for key,value in inidata:
                    self._dict[key] = value

        # Manera de hacerlo sin isinstance
        
        # if hasattr(initial_data, "items"):
        #   self._dict.update(initial_data.items())
        # else:
        #   for key, value in initial_data:
        #       self._dict[key] = value       


    def add(self,key,value):
        # adds key-value pair
        if key in self._dict:
            print("Key already in dict, changing value to",value)
            self._dict[key] = value
        else:
            print(f"Key-Value pair added successfully → {key}:{value}")
            self._dict[key] = value


    def remove(self,key):
        # accpet key and remove the associated key-value pair
        if key in self._dict:
            print(f"Removing key: '{key}'")
            del self._dict[key]
        else:
            print("Key does not exist on dict")
    
    def get(self,key):
        # accept a key and return the store value
        if key in self._dict:
            return self._dict.get(key)
        else:
            return "Key not in dictionary"

    def has(self,key):
        # accept a key and return True if the key exists or False if it doesn't
        return key in self._dict

    def keys(self):
        # Return an array with keys from dict
        return list(self._dict.keys())

    def values(self):
        # Return an array with values from dict
        return list(self._dict.values())

    def size(self):
        # Return the number of items(keys) on the map
        return len(self._dict)

    def clear(self):
        # Empties the dict,map
        self._dict.clear()
        return self._dict

    def __str__(self):
        # Allow printing things
        return str(self._dict)

    def __iter__(self):
        # Allow iterate over class objects
        return iter(self._dict)
    
    def items(self):
        return self._dict.items()



meindik = Map()
print(meindik)
meindik.add('masters',1000)
meindik.add('open','Australia')
print(meindik)
meindik.remove('caramelo')
meindik.remove('open')
print(meindik)
print(meindik.has('masters'))
print(meindik.size())
print(meindik.clear())
meindik.add('tristes','tigres')
meindik.add('pelotas','cuadradas')
print(meindik)



yourdik = Map([('kacken',33),('merluza','veintipico')])
print(yourdik)

m1 = Map({"a": 1, "b": 2})
print(m1)