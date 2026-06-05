"""Given an array arr, find element pairs whose sum equal the second argument arg and return the sum of their indices.

You may use multiple pairs that have the same numeric elements but different indices. Each pair should use the lowest possible available indices. 
Once an element has been used it cannot be reused to pair with another element. For instance, pairwise([1, 1, 2], 3) creates a pair [2, 1] using the 1 at index 0 
rather than the 1 at index 1, because 0+2 < 1+2.

For example pairwise([7, 9, 11, 13, 15], 20) returns 6. The pairs that sum to 20 are [7, 13] and [9, 11]. We can then write out the array with their indices and values.

Index	0	1	2	3	4
Value	7	9	11	13	15
Below we'll take their corresponding indices and add them.

7 + 13 = 20 → Indices 0 + 3 = 3
9 + 11 = 20 → Indices 1 + 2 = 3
3 + 3 = 6 → Return 6

1. pairwise([1, 4, 2, 3, 0, 5], 7) should return 11.
2. pairwise([1, 3, 2, 4], 4) should return 1.
3. pairwise([1, 1, 1], 2) should return 1.
4. pairwise([0, 0, 0, 0, 1, 1], 1) should return 10.
5. pairwise([], 100) should return 0.

"""

arr0 = [7, 9, 11, 13, 15]
tg0 = 20
arr1 = [1, 4, 2, 3, 0, 5]
tg1 = 7
arr2 = [1, 3, 2, 4]
tg2 = 4
arr3 = [1, 1, 1]
tg3 = 2
arr4 = [0, 0, 0, 0, 1, 1]
tg4 = 1
arr5 = []



def pairs(arr,target):
    
    # Dos partes, al menos
    # Encontrar pares que sumen = target, no se pueden volver a usar
    # Sumar los indices en los que estan los numeros usados, siempre los mas bajos, el resultado es la suma total de los indices usados
    usados = set() 
    soluciones = []
    sum_index = []
    sumas = 0
    print(f"Para un target de {target} se tienen indices-valores como:")
    for i in range(len(arr)):        
        if i in usados:
            continue        
        for j in range(i+1,len(arr)):
            if j in usados:
                continue
            
            if arr[i]+arr[j]==target:
                usados.add(i)
                usados.add(j)
                sumas += i+j
                sum_index.extend([i,j])
                soluciones.append((arr[i],arr[j]))
                break                
                   
    
    print("Values",arr)
    print("Suma indices",sum_index) 
    
    

    return f"Resultado → {sumas}"
    

print(pairs(arr0,tg0))
print("\n")
print(pairs(arr1,tg1))
print("\n")
print(pairs(arr2,tg2))
print("\n")
print(pairs(arr3,tg3))
print("\n")
print(pairs(arr4,tg4))
print("\n")
print(pairs(arr5,100))


"""Usando diccionarios"""
print("\n")
print("\n")

def pairwise(arr,target):
    seen = {}    # valor -> índice (el primero disponible)
    used = set()
    total = 0
    
    print(f"Array: {arr}\n")
    for i,num in enumerate(arr):
        if i in used:
            continue

        # Por cada valor del array, el numero que necesito es target-valor, compruebo si lo he visto o no
        # En lugar de buscar todas las combinaciones
        comp = target - num 
        
        print(f"El compuesto: {comp}\nResta de {target}-{num}\n")

        if comp in seen:
            j = seen[comp]
            print(comp,seen,j)

            if j not in used:
                print("Se suman indices", i,j)
                total += i+j
                used.add(i)
                used.add(j)
                del seen[comp] # evita reutilizacion
                continue
        print("Indices usados:",used)
        if num not in seen:
            seen[num] = i

    return total
        

print(pairwise(arr0,tg0))