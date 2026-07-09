"""Implement Merge Sort
Another common intermediate sorting algorithm is merge sort. Like quick sort, merge sort also uses a divide-and-conquer, recursive methodology to sort an array. 
It takes advantage of the fact that it is relatively easy to sort two arrays as long as each is sorted in the first place. 
But we'll start with only one array as input, so how do we get to two sorted arrays from that? 
Well, we can recursively divide the original input in two until we reach the base case of an array with one item. 
A single-item array is naturally sorted, so then we can start combining. This combination will unwind the recursive calls that split the original array, 
eventually producing a final sorted array of all the elements. 

The steps of merge sort, then, are:

1) Recursively split the input array in half until a sub-array with only one element is produced.

2) Merge each sorted sub-array together to produce the final sorted array.

Merge sort is an efficient sorting method, with time complexity of O(nlog(n)). This algorithm is popular because it is performant and relatively easy to implement.

As an aside, this will be the last sorting algorithm we cover here. However, later in the section on tree data structures we will describe heap sort, 
another efficient sorting method that requires a binary heap in its implementation.

Instructions: Write a function mergeSort which takes an array of integers as input and returns an array of these integers in sorted order from least to greatest. 
A good way to implement this is to write one function, for instance merge, which is responsible for merging two sorted arrays, and another function, for instance mergeSort, 
which is responsible for the recursion that produces single-item arrays to feed into merge. Good luck!

Tests:
1. mergeSort should be a function.
2. mergeSort should return a sorted array (least to greatest).
3. mergeSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]) should return an array that is unchanged except for order.
4. mergeSort should not use the built-in .sort() method.
"""


array1 = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
array2 = [5, 4, 33, 2, 8]

def mergesort(arr, depth=0):
    # añadiendo depth se puede ver en forma de diagrama de niveles, que va entrando en la recursion
    print("  " * depth + f"♦ Entrando: {arr}")

    if len(arr) <= 1:
        print("  " * depth + f"• Base: {arr}")
        return arr
    
    # En este caso, no hay pivote, dividimos la lista en dos de manera continua hasta llegar al caso base

    # Usamos mid como punto medio entre listas izda y dcha, a la que se le hara la recursion, que consistirá en dividirlas continuamente
    mid = len(arr) // 2
    
    # print(f"Izda y Dcha, se lesace recursion, dividiendo hasta llegar al caso base de un solo elemento\n→{arr[:mid]}\n→{arr[mid:]}\n")
    
    izda = mergesort(arr[:mid], depth + 1)
    dcha = mergesort(arr[mid:], depth + 1)
    
    print("  " * depth + f"→ Mergeando: {izda} + {dcha}")

    sorted_arr = []

    i = 0
    j = 0
    
    while i < len(izda) and j < len(dcha):

        # segun que elemento sea mas pequeño se añade uno a uno en la lista sorted_arr

        if izda[i] <= dcha[j]:
            sorted_arr.append(izda[i])
            
            # avanza en la lista izda
            i += 1
        else:
            sorted_arr.append(dcha[j])
            
            # avanza en la lista dcha
            j += 1
        
    
    sorted_arr.extend(izda[i:])
    sorted_arr.extend(dcha[j:])

    print("  " * depth + f">>> Resultado: {sorted_arr}")

    return sorted_arr


mergesort(array1)