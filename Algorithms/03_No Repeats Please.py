"""No Repeats Please
Return the number of total permutations of the provided string that don't have repeated consecutive letters. 
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), 
but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating."""

str0 = 'abc'
str1 = 'aab'
str2 = 'aabb'
str3 = 'aaabb'
str4 = 'abfdefa'
str5 = 'abcdefa'

"""Diferentes métodos de hacerlo: recursion o backtracking, inserción progresiva, y generadores"""

# Recursion

def recur_permut(cadena):
    if len(cadena) == 1:
        # print(f"\nBase: {cadena}\n")
        return [cadena]
    
    resultado = []
    # Para cada valor del string
    for i in range(len(cadena)):
        # Se van fijando en posición, y se permuta todo lo demás
        fijo = cadena[i]
        # El resto es todo excepto donde esté i, hasta i -> [:i] y despues de i -> [i+1:]
        resto = cadena[:i] + cadena[i+1:]
        # print(f"\nFijo: {fijo}, Resto: {resto}")

        # Realizamos las permutaciones de la lista "resto" por cada elemento fijo
        for r in recur_permut(resto):
            # Con este if se filtra si el primer caracter de r es igual a fijo
            if fijo == r[0]:
                continue
            # print(f"Combinando: {fijo} + {r}")         
            resultado.append(fijo + r)
            # print(f"Resultando: {resultado}")
          
    # print("\nSoluciones posibles:",len(resultado))
    return resultado

print("RECURSIÓN")
print("----------")
print(f"\nLista de resultados:\n\n{recur_permut(str2)}\n")
print(f"Soluciones: {len(recur_permut(str2))}")

# Backtracking

def back_permut(letras):
    # Convertimos el string en lista para hacerlo mutable, y hacer los swaps, que no se podrían hacer 
    lista = list(letras)
    resultado = []

    # Se define la función de backtracking
    def backtrack(i):
        # Cuando i tenga la longitud de la lista añadimos el resultado 
        if i == len(lista):            
            print(f"\n♦ Se añade: {lista}")
            # Se añade al resultado con join los elementos de la lista
            resultado.append(''.join(lista))
            print(f"♦ Resultado: {resultado}\n")
            return
        
        # Para cada elemento al que le haremos swap en el rango i (que será 0 al inicio) hasta la longitud de la lista
        for j in range(i,len(lista)):
            
            # Hacemos swap, intercambio de posiciones entre i, la que pasa a la funcion backtrack y j, el elemento de la lista
            # print(f"Posiciones i={i} → {lista[i]} - j={j} → {lista[j]}")
            # print(f"Se hace swap {lista[i]} - {lista[j]}")
            print(f"lista={lista}\n")
            lista[i],lista[j] = lista[j],lista[i]

            # Se filtra a medida que se añaden valores para ver si cumplimos la condición, sino se cumple, para y pasa a la siguiente permutacion
            if i == 0 or lista[i] != lista[i-1]:                
                # Pasaremos al siguiente elemento siempre que sea el primero, o elementos consecutivos no sean iguales, sino se para y no añade elresultado
                backtrack(i+1)
            # Se deshace el swap
            lista[i],lista[j] = lista[j],lista[i]

    # Primera llamada a backtrack para que entre al bucle, al inicio solo se crea la lista y resultado, cuando llega al final llama a backtrack(0), solo se ejecuta una vez
    # Al final del ciclo i = longitud de la lista, lo que hara que se cierre el bucle
    # Es como un stack con tantas llamadas a backtrack como longitud tiene la lista → stack = [backtrack(0),backtrack(1),backtrack(2),backtrack(3)] cuando se vacía, se acaba.
    backtrack(0)
    return resultado
    

print("\n")
print("BACKTRACKING")
print("------------")
# print(f"\nLista de resultados:\n\n{back_permut(str0)}\n")
print(f"Soluciones: {len(back_permut(str1))}")


# Inserción progresiva

def prog_permut(string):
    # La lista de resultados empieza con un elemento que es un string vacio
    resultado = ['']
    
    for char in string:
        # Lista en la que se irán construyendo soluciones
        nuevo = []
        
        for p in resultado:
            print(f"p es {p}")
            for i in range(len(p) + 1):
                # Si filtramos aqui parariamos el proceso pq no permitiria seguir si hay dos iguales, y eso no nos interesa, hay que filtrar despues
                permutacion = p[:i] + char + p[i:]
                print(f"Nueva permutación: {permutacion}")
                nuevo.append(permutacion)
        resultado = nuevo
    
    print("Sin filtro, los resultados son: ",resultado)

    resultado_filtrado = []
    # Recorremos la lista de resultados y elegimos aquellos que cumplen la condicion
    for p in resultado:
        valido = True
        # Se recorrde en cada indice de la lista resultados, la cadena de caracteres que lo componen para ver si hay dos iguales seguidos p[i] == p[i-1]
        # Si es asi se descarta esa solucion (break) y se pasa al siguiente indice
        # Si una vez recorrido todos los caracteres son validos, pasa al siguiente if, y añade la solucion
        for i in range(1, len(p)):
            if p[i] == p[i-1]:
                valido = False
                break
        if valido:
            resultado_filtrado.append(p)
    
    print("Aplicando filtro, los resultados son: ",resultado_filtrado)

    return resultado_filtrado

print("\n")
print("INSERCIÓN PROGRESIVA")
print("--------------------")
print(f"Soluciones: {len(prog_permut(str1))}")


