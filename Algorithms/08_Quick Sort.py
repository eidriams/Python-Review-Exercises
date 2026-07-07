"""Implement Quick Sort
Here we will move on to an intermediate sorting algorithm: quick sort. Quick sort is an efficient, recursive divide-and-conquer approach to sorting an array. 
In this method, a pivot value is chosen in the original array. 
The array is then partitioned into two subarrays of values less than and greater than the pivot value. 
We then combine the result of recursively calling the quick sort algorithm on both sub-arrays. 
This continues until the base case of an empty or single-item array is reached, 
which we return. The unwinding of the recursive calls return us the sorted array.

Quick sort is a very efficient sorting method, providing O(nlog(n)) performance on average. It is also relatively easy to implement. 
These attributes make it a popular and useful sorting method.

Instructions: Write a function quickSort which takes an array of integers as input and returns an array of these integers in sorted order from least to greatest. 
While the choice of the pivot value is important, any pivot will do for our purposes here. For simplicity, the first or last element could be used.

Tests:
1. quickSort should be a function.
2. quickSort should return a sorted array (least to greatest).
3. quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]) should return an array that is unchanged except for order.
4. quickSort should not use the built-in .sort() method.
"""

array1 = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
array2 = [5, 4, 33, 2, 8]

def quicksort(arr):

    
    lesser = []
    higher = []
    pivot = []

    # array con elementos ordenados
    sorted_arr = []

    # Caso base, lista de un solo elemento
    if len(arr) <= 1:
        return arr
    
    i = 0

    while i < len(arr):

        # elemento desde el que vamos a hacer las divisiones en listas, dentro del bucle para que reinicie con cada recursion
        # mayores y menores tendran recursion, los elementos iguales al pivote no

        pivote = arr[-1]

        # comparamos cada elemento con el de pivote y lo asignamos a la lista correspondiente
        if arr[i] < pivote:
            lesser.append(arr[i])
            i += 1
        
        elif arr[i] == pivote:
            pivot.append(arr[i])
            i += 1

        else:
            higher.append(arr[i])
            i += 1
    
    # cuando se han creado las listas con elementos mayores y menores que el pivote, hacemos la recursion de las listas
    print(f"○ Sale del bucle y queda\n  • lesser → {lesser}\n  • pivot → {pivot}\n  • higher → {higher}")
    print(f"  → Recursion a listas lesser y higher\n")
    less = quicksort(lesser)
    high = quicksort(higher)
    

    # Cuando todas las listas queden reducidas al caso base, construimos el el array ordenado con cada una, en orden, lesser,pivot,higher
    print(f"Evolucion de listas:\n  • less= {less}\n  • pivot={pivot}\n  • high={high}\n")
    sorted_arr.extend(less)
    sorted_arr.extend(pivot)
    sorted_arr.extend(high)

    return sorted_arr


print(quicksort(array1))
print(quicksort(array2))





