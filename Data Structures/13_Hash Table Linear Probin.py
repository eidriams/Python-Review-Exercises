"""Aqui voy a intentar realizar el mismo ejercicio, pero tratando las colisiones en la tabla sin anidar resultados

Lo hago aparte porque cambian algunos aspectos importantes del ejercicio, y hay contras asociados a esta manera de implementacion, como el rehashing, puesto que se trabaja con
arrays de tamaño fijo, una vez que se llenan, hay que redimensionarlos y se producen mas colisiones debido al tamaño del array con que se trabaja"""



# Cogiendo la base de la clashe HashTable de antes, vamos a modificarla

DELETED = object()

class HashTable():

    def __init__(self, size = 10):
        # La primera diferencia va a ser que trabajamos con un array de tamaño fijo
        self.size = size
        # Inicializamos una tabla vacia en la que se indexaran los datos segun el numero hash que produzcan
        self.table = [None] * size

        # Contador que sirva para hacer el rehashing en funcion de los elementos que haya en la tabla
        # El concepto es el factor de carga = elementos / tamaño de la tabla
        # Suele ser conveniente hacer rehashing cuando este valor es mayor a 0.7

        self.count = 0

    # Función que creará el NºHash
    def HashFunc(self, key=str):
        # El criterio sera, dado un string, el valor del hash sera la suma del valor unicode de cara caracter
        # La funcion ord() nos da el valor unicode de cada caracter
        hash_value = 0
        for item in key:
            hash_value += ord(item)
        # El cambio aquí es que el resultado estará asociado al tamaño del array, de manera que produzca la posicion que va a ocupar en el mismo
        # Si es 10 como en este caso, el hash_value tendrá un valor de 0 a 9
        return hash_value % self.size

    def add(self,key,value):

        # Aquí es donde están los cambios mas significativos
        
        # Se obtiene el valor hash para la clave añadida, en lugar de llamarlo 'hasheo' lo llamamos index, que es mas grafico, ya que va a crear la posicion en la que debería
        #estar el elemento
        index = self.HashFunc(key)
        # start_index se usa para evitar bucle infinito
        start_index = index

        # Mientras haya un valor en la posicion generada por index
        while self.table[index] is not None:
            
            # el key,value de la tabla
            stored_key, _  = self.table[index]

            # Si la clave existe, se sobreescribirá el valor
            if stored_key == key:
                self.table[index] = (key,value)
                return
        
            # Se prueba en la siguiente posicion
            index = (index + 1) % self.size

            # Si se llega al final de la lista, quiere decir que está llena
            if index == start_index:
                raise Exception("Hashtable is full")
            
        # Si el index genera una posicion que es None, es decir, que esta vacía, se insertará el par key,value correspondiente
        print(f"Se inserta en posición {index}")
        self.table[index] = (key,value)

        # Cuando se añade un elemento, el contador va sumando
        self.count += 1 

        # Si el valor de factor de carga se cumple, provocamos un rehash
        if self.count / self.size > 0.7:
            self._rehash()    
        
        return self.table
        

    def remove(self,key):

        # La funcion object() devuelve un objeto vacio
        # En lugar de eliminar un valor, ejecutamos esta funcion.
        # Si se cambiase por None al quitar un par key-value romperíamos el bucle
        

        # El uso de object() va a provocar que el hueco en el que se elimine ya no sea None, y se lo salte el futuras adiciones
        # Para corregirlo, hay que recordar la posicion del elemento eliminado y tenerlo en cuenta
        
        # En el metodo add se añadiría esta modificacion

        # first_deleted = None

        # while self.table[index] is not None:
            # if self.table[index] is DELETED:
            #    if first_deleted is None:
            #       first_deleted = index

            # else:
            #     stored_key, _ = self.table[index].... a partir de aqui lo mismo

        # usamos index de nuevo
        index = self.HashFunc(key)

        start_index = index

        while self.table[index] is not None:
            
            # aqui hay dos variales, como en el metodo lookup, stored_key y stored_value
            # como convencion se usa _ para identificar que es una variable que no se va a usar o no se necesita en este metodo
            stored_key, _ = self.table[index]

            # Si la clave coincide, se elimina
            if stored_key == key:

                self.table[index] = DELETED
                print(f"Key: {key} deleted successfully")
                return self.table
            
            # Si no, prueba la siguiente posicion
            index = (index + 1) % self.size

            # Cuando llegue al final de la lista, para el bucle
            if index == start_index:
                print("Key not found")
                break
        
        return self.table

    def lookup(self,key):

        # Volvemos a usar index en lugar de hasheo
        index = self.HashFunc(key)

        start_index = index

        # al igual que antes, si miramos a una posicion que no esté vacía

        while self.table[index] is not None:

            # key,value de la posicion index
            stored_key,stored_value = self.table[index]

            # si la clave existe
            if stored_key == key:
                # Devuelve el valor asociado
                return f"At index: {index}\nHas the value of: '{stored_value}'"
            
            # Si no prueba en la siguiente posicion
            index = (index + 1) % self.size

            # Si llega al final de la lista el bucle se detiente
            if index == start_index:
                
                break
        
        return "Key not found"

    def __str__(self):
        return str(self.table)
    
    # Metodo rehash, que no solo hace el tamaño de la tabla mas grande
    # Implica recalcular las posiciones nuevas en funcion del nuevo tamaño de la tabla
    # Y volver a insertar todos los elementos     
    def _rehash(self):

        old_table = self.table

        # Aumento de tamaño
        self.size *= 2
        self.table = [None] * self.size
        # Reinicia el contador
        self.count = 0

        # Reinsercion de elemetos
        for item in old_table:
            # Tiene en cuenta las posiciones donde habia elementos e ignora si en el hueco hubo un elemento eliminado
            if item is not None and item is not DELETED:
                key,value = item
                self.add(key,value)
    


hashme = HashTable()

print("Nº Hash para 'tarantula':",hashme.HashFunc('tarantula'))

print(hashme.add('tarantula',8))

print("Nº Hash para 'rantulata':",hashme.HashFunc('rantulata'))

print(hashme.add('rantulata','patas'))

print("Nº Hash para 'roperos':",hashme.HashFunc('roperos'))

print(hashme.add('roperos','con puertas'))

print(f"Valor de 'roperos' →  {hashme.lookup('roperos')}")

print(f"Valor de 'muestra' →  {hashme.lookup('muestra')}")

print(f"Valor de 'tarantla' →  {hashme.lookup('tarantula')}")

print(f"Valor de 'rantulata' →  {hashme.lookup('rantulata')}")

print(hashme.add('caca',33))
print(hashme.add('olivilla','terrorista'))
print(hashme.add('kuma','to amor'))
print(hashme.add('bacalao','gordinflas'))
print(hashme.add('vero','churri'))
print(hashme.add('dante','mostruos'))
print(hashme.add('adri','cabesa'))

print(f"Valor de 'roperos' →  {hashme.lookup('roperos')}")

print(f"Valor de 'dante' →  {hashme.lookup('dante')}")

# print(hashme.remove('rantulata'))

# print(hashme)
