"""Implement Insertion Sort
The next sorting method we'll look at is insertion sort. This method works by building up a sorted array at the beginning of the list. 
It begins the sorted array with the first element. Then it inspects the next element and swaps it backwards into the sorted array 
until it is in sorted position. It continues iterating through the list and swapping new items backwards into the sorted portion until 
it reaches the end. This algorithm has quadratic time complexity in the average and worst cases.

Instructions: Write a function insertionSort which takes an array of integers as input and returns an array of these integers 
in sorted order from least to greatest.

Tests:
1. insertionSort should be a function.
2. insertionSort should return a sorted array (least to greatest).
3. insertionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]) should return an array that is unchanged except for order.
4. insertionSort([5, 4, 33, 2, 8]) should return [2, 4, 5, 8, 33].
5. insertionSort should not use the built-in .sort() method."""


array1 = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
array2 = [5, 4, 33, 2, 8]


# print(list(range(len(array2))))
# print(list(range(4,-1,-1)))


def insertionSort(arr):

    # el primer elemento a insertar sera el del indice 1, porque el del indice 0 ya está 'ordenado'

    

    for i in range(1, len(arr)): # lo que este a partir del indice 1 en adelante

        guardo = arr[i] # valor a insertar
        print("Buscando hueco para → ", guardo)
        
        j = i - 1 # comienza desde la izquierda
        print(f"Vamos hacia la izquierda desde i={i} → j={j} ")

        while j >= 0 and arr[j] > guardo:            
            # desplazo arr[j] hacia la derecha
            arr[j+1] = arr[j]
            # me muevo hacia la izquierda para comparar el siguiente elemento
            j -= 1 
        
        
        # inserto
        arr[j + 1] = guardo
        
    
    return arr

            
                      
print(insertionSort(array2))
# print(insertionSort(array1))























print("\n")
def insertion(lista):

    for i in range(len(lista)):

        fijo = i

        for j in range(i+1, len(lista)):

            if lista[j] < lista[i]:
                # si el elemento de la derecha es menor que el fijo de la izquierda lo muevo
                lista[j],lista[i] = lista[i],lista[j]
            else:
                # si no es mayor, o es igual, se queda en la parte derecha del elemento fijo
                continue 

    return lista



print(insertion(array2))
print(insertion(array1))


"""funciona pero esto no es insertionSort"""
