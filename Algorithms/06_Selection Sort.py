"""Implement Selection Sort
Here we will implement selection sort. Selection sort works by selecting the minimum value in a list and swapping it with the first value in the list.
It then starts at the second position, selects the smallest value in the remaining list, and swaps it with the second element. 
It continues iterating through the list and swapping elements until it reaches the end of the list. Now the list is sorted. 
Selection sort has quadratic time complexity in all cases.

Instructions: Write a function selectionSort which takes an array of integers as input and returns an array of these integers in sorted order from least to greatest.

1. selectionSort should be a function.
2. selectionSort should return a sorted array (least to greatest).
3. selectionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]) should return an array that is unchanged except for order.
4. selectionSort should not use the built-in .sort() method.
"""

array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

arrayt = [1,4,5,9,78,3,6]

def selection_sort(arr):

    # Ciclo externo, cada valor se compara con el resto de la lista para saber si es el mas pequeño
    for i in range(len(arr)):
        
        min_index = i # indice a comparar con el resto de la lista

        for j in range(i+1 , len(arr)): # resto de la lista, la parte menor que i ya no se toca porque esta ordenada

            if arr[j] < arr[min_index]: # si un elemento de la derecha es menor que el que hemos escogido como minimo

                min_index = j # sustituimos el valor minimo

        # y se swapea

        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr            
        
    

            
print(selection_sort(arrayt))
print(selection_sort(array))
