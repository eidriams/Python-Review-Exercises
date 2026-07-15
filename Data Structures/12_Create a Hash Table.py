"""Create a Hash Table
In this challenge we will learn about hash tables. 
A Hash table is used to implement associative arrays, or mappings of key-value pairs, like the objects and Maps we have just been studying. 
A JavaScript object could be implemented as a hash table, for instance (its actual implementation will depend on the environment it's running in). 
The way a hash table works is that it takes a key input and hashes this key in a deterministic way to some numerical value. 
This numerical value is then used as the actual key the associated value is stored by. 
Then, if you try to access the same key again, the hashing function will process the key, return the same numerical result, which will then be used to look up the associated value. 

This provides very efficient O(1) lookup time on average.

Hash tables can be implemented as arrays with hash functions producing array indices within a specified range. 
In this method, the choice of the array size is important, as is the hashing function. 
For instance, what if the hashing function produces the same value for two different keys? 
This is called a collision. 
One way to handle collisions is to just store both key-value pairs at that index. 
Then, upon lookup of either, you would have to iterate through the bucket of items to find the key you are looking for. 
A good hashing function will minimize collisions to maintain efficient search time.

Here, we won't be concerned with the details of hashing or hash table implementation, we will just try to get a general sense of how they work.

Let's create the basic functionality of a hash table. 
We've created a naive hashing function for you to use. 
You can pass a string value to the function hash and it will return a hashed value you can use as a key for storage. 
Store items based on this hashed value in the this.collection object. 
Create these three methods: add, remove, and lookup. 
The first should accept a key value pair to add to the hash table. 
The second should remove a key-value pair when passed a key. 
The third should accept a key and return the associated value or null if the key is not present.

Be sure to write your code to account for collisions!

Note: The remove method tests won't pass until the add and lookup methods are correctly implemented.

Tests:
Waiting:1. The hash function should be valid.
Waiting:2. The HashTable data structure should exist.
Waiting:3. The HashTable should have an add method.
Waiting:4. The HashTable should have a lookup method.
Waiting:5. The HashTable should have a remove method.
Waiting:6. The add method should add key value pairs and the lookup method should return the values associated with a given key.
Waiting:7. The remove method should accept a key as input and should remove the associated key value pair.
Waiting:8. The remove method should only remove the correct key value pair.
Waiting:9. Items should be added using the hash function.
Waiting:10. The hash table should handle collisions."""


class HashTable():

    def __init__(self):
        # Creamos la coleccion de datos inicial vacía
        self._dict = {}

    # Función que creará el NºHash
    def HashFunc(self, key=str):
        # El criterio sera, dado un string, el valor del hash sera la suma del valor unicode de cara caracter
        # La funcion ord() nos da el valor unicode de cada caracter
        hash_value = 0
        for item in key:
            hash_value += ord(item)
        
        return hash_value

    def add(self,key,value):
        
        # Se obtiene el valor hash para la clave añadida
        hasheo = self.HashFunc(key)
        # Hasheo será el Key de la tabla hash, el valor sera el diccionario con el par key-value añadidos
        addict = {key:value}
        # Si no está en el dict, se añade el par key:value
        if hasheo not in self._dict:
            self._dict.update({hasheo:addict})
        else:
            # Si el hash value se encuentra en la tabla, se anida el nuevo par key-value en ese punto
            self._dict[hasheo][key] = value
            # Se puede buscar la posicion adyacente libre mas cercana
        
        return self._dict
        

    def remove(self,key):
        # hash de la clave para ver si esta en la tabla
        hasheo = self.HashFunc(key)
        if hasheo in self._dict:
            # Si está, se busca la clave 'key' pasada al metodo
            if key in self._dict[hasheo]:
                del(self._dict[hasheo][key])
                print(f"Key: {key} deleted successfully")
        else:
            print(f"Key: {key} does not exist")
        
        return self._dict

    def lookup(self,key):
        # hash de la clave primero
        hasheo = self.HashFunc(key)
        # Si está en la tabla hash, mostrar que hay en ese punto
        if hasheo in self._dict:
            if key in self._dict[hasheo]:
                return self._dict[hasheo][key]
            else:
                print(f"No Key-Value pair found associated with key: {key}")
        else:
            print(f"Key: {key} does not exist")   

    def __str__(self):
        return str(self._dict)
    

hashme = HashTable()

print("Nº Hash para 'tarantula':",hashme.HashFunc('tarantula'))

print(hashme.add('tarantula',8))

print(hashme.add('rantulata','patas'))

print(hashme.add('ropero','con puertas'))

print(hashme.lookup('ropero'))

print(hashme.lookup('muestra'))

print(hashme.lookup('peroro'))

print(hashme.remove('rantulata'))