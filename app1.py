#Ejercicio 1

def suma_elementos(lista):

    suma = 0
    
    for numero in lista:

        suma += numero
    
    return suma

mi_lista = [1, 2, 3, 4, 5]
resultado = suma_elementos(mi_lista)
print(resultado)  

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2

def contar_pares(lista):
    
    pares = 0

    for numero in lista:

        if numero % 2 == 0:

            pares += 1

    return pares

resultado2 = contar_pares(mi_lista)
print(resultado2)

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3

def elemento_mas_grande(lista):

    if not lista:
        return None
    
    max_elemento = lista[0]
    
    # Recorre cada elemento de la lista a partir del segundo
    for numero in lista[1:]:
        if numero > max_elemento:
            max_elemento = numero
    
    return max_elemento

mi_lista3 = [3, 1, 4, 1, 5, 9, 2]
resultado3 = elemento_mas_grande(mi_lista3)
print(resultado3) 

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 4

def multiplicar_elementos(lista):

    nueva_lista = []

    for numero in lista:

        nueva_lista.append(numero * 2)

    return nueva_lista

mi_lista4 = [1, 2, 3, 4]
resultado4 = multiplicar_elementos(mi_lista4)
print(resultado4)

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 5

def invertir_lista(lista):
    
    lista_copia = lista.copy()

    lista_copia.reverse()

    return lista_copia

mi_lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
resultado5 = invertir_lista(mi_lista5)
print(resultado5)


