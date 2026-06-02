"""Find the Symmetric Difference
The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both. 
For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.

Symmetric difference is a binary operation, which means it operates on only two elements. So to evaluate an expression involving 
symmetric differences among three elements (A △ B △ C), you must complete one operation at a time. Thus, for sets A and B above, 
and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

Create a function that takes two or more arrays and returns an array of their symmetric difference. 
The returned array must contain only unique values (no duplicates)."""



# *args permite que una funcion use un número variable de entradas
# **kwargs si quiero que la función reciba argumentos de tipo clave=valor
    #Resumen rápido
        # a, b → número fijo
        # b=valor → opcional
        # *args → muchos argumentos (posición)
        # **kwargs → muchos argumentos (nombre)

A = [1, 2, 3, 3]
B = [5, 2, 1, 4]

def sim(*args):
    
    print("Symmetric Diffrence between:\n",args)
    # Dict para obtener el numero de elementos de cada lista, un conteo de cada uno de ellos
    conteo = {}
    
    for item in args:
        # Lista de unicos, lo que haría un set()
        unicos = []
        for elem in item:
            # Por cada elemento en cada lista que pase como argumento
            # Si ese elemento no esta en la lista de unicos, no se ha añadido antes, se añade
            if elem not in unicos:
                unicos.append(elem)
                # Vamos al Dict para saber si ese elemento ya se encuentra añadido para sumar 1 a su conteo, o añadirlo como elemento nuevo
                if elem in conteo:
                    conteo[elem] += 1
                else:
                    conteo[elem] = 1
    
    # Lista con el resultado de la operacion de diferencia simétrica
    resultado = []
    # Recorremos el dict para observar que elementos son pares o impares, nos quedamos con los impares
    for key,value in conteo.items():
        if value % 2 == 1:
            # Si el numero de veces que aparece el elemento es impar, añadimos la key, que es el valor que aparece en las listas pasadas como argumento
            resultado.append(key)
    print("Results in:")
    return resultado


print(sorted(sim(A,B)))

print(sim([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))

print(sorted(sim([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])))

print(sorted(sim([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])))
