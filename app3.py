#DICCIONARIO

#Ejercicio 1

# Inicializar el diccionario de alumnos y sus notas
alumnos = {}

# Bucle para seguir ingresando datos
while True:
    # Solicitar el nombre del alumno
    nombre = input("Ingresa el nombre del alumno (o escribe 'salir' para terminar): ")
    
    if nombre.lower() == 'salir':
        break
    
    try:
        nota = float(input(f"Ingresa la nota de {nombre}: "))
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para la nota.")
        continue

    # Almacenar el nombre y la nota en el diccionario
    alumnos[nombre] = nota

print("\nAlumnos y sus notas:")
for alumno, nota in alumnos.items():
    print(f"{alumno}: {nota}")

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2

def promedio_notas(alumnos):
    # Verificar si el diccionario está vacío
    if not alumnos:
        return 0  # Si no hay alumnos, el promedio es 0
    
    suma_notas = 0
    
    for nota in alumnos.values():
        suma_notas += nota  # Sumar cada nota
    
    # Calcular el promedio
    promedio = suma_notas / len(alumnos)
    
    return promedio

alumnos = {'Juan': 4.5, 'Ana': 3.7, 'Pedro': 4.8}
promedio = promedio_notas(alumnos)
print(f"El promedio de las notas es: {promedio}")


#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3

def alumno_con_mejor_nota(alumnos):
    
    if not alumnos:
        return None  # Si no hay alumnos, retornar None
    
    mejor_alumno = None
    mejor_nota = float('-inf')  # Inicializamos con el valor más bajo posible
    
    for alumno, nota in alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno
    
    return mejor_alumno

alumnos = {'Juan': 4.5, 'Ana': 3.7, 'Pedro': 4.8}
mejor_alumno = alumno_con_mejor_nota(alumnos)
print(f"El alumno con la mejor nota es: {mejor_alumno}")


#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 4

# Inicializar el diccionario de palabras y definiciones
diccionario = {}

while True:
    
    palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
    
    if palabra.lower() == 'salir':
        break
    
    definicion = input(f"Ingresa la definición de '{palabra}': ")
    
    diccionario[palabra] = definicion

print("\nDiccionario:")
for palabra, definicion in diccionario.items():
    print(f"{palabra}: {definicion}")


#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 5

def buscar_palabra(diccionario, palabra):
    # Buscar la palabra en el diccionario
    definicion = diccionario.get(palabra)
    
    if definicion:
        return f"La definición de '{palabra}' es: {definicion}"
    else:
        return f"La palabra '{palabra}' no se encontró en el diccionario."

diccionario = {'Python': 'Lenguaje de programacion', 
               'Algoritmo': 'Instrucciones en un sistema para hacer una accion'}

palabra_buscada = input("Ingresa la palabra que deseas buscar: ")
resultado = buscar_palabra(diccionario, palabra_buscada)
print(resultado)

