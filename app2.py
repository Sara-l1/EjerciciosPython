import random

#WHILE Y COLECCIONES

#Ejercicio 1

def eliminar_duplicados(lista):

    conjunto_unico = set(lista)

    lista_sin_duplicados = list(conjunto_unico)

    return lista_sin_duplicados

lista_con_duplicados = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 1]
resultadoWhile = eliminar_duplicados(lista_con_duplicados)
print(resultadoWhile)

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2

def juego_aleatorio():

    numero_secreto = random.randint(1, 100)
    intentos_maximos = 7
    intentos_restantes = intentos_maximos

    print("He pensado en un numero del 1 al 100")
    print(f"tienes {intentos_maximos} intentos para adivinar el numero")

    while intentos_restantes > 0:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))

        except ValueError:
            print("Por favor, ingresa un numero valido")
            continue

    if adivinanza == numero_secreto:
         print("¡Felicidades! Adivinaste el numero")
            

    elif adivinanza < numero_secreto:
        print("El numero es menor al numero secreto")

    else:
        print("El numero es mayor al numero secreto")

        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos para adivinar.")

    if intentos_restantes == 0:
        print(f"Lo siento, te quedaste sin mas intentos. El numero secreto es {numero_secreto}.")

juego_aleatorio()

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3

frase = input("Ingresa una frase: ").lower()  # Convertir a minúsculas
contador = 0  # Inicializar el contador
i = 0  # Inicializar el índice

while i < len(frase):
    if frase[i] in "aeiou":  # Si el carácter es una vocal
        contador += 1  # Aumentar el contador
    i += 1  # Avanzar al siguiente carácter

print(f"La frase contiene {contador} vocales.")

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 4

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Salir")

# Bucle principal
while True:
    mostrar_menu()
    
    opcion = input("Elige una opción (1-5): ")

    if opcion == '5':  # Opción para salir
        print("¡Gracias por usar la calculadora!")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == '4':
        if num2 != 0:  # Verificar que no haya división por cero
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre 0.")
    else:
        print("Opción inválida. Por favor, elige una opción válida.")


#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 5

        # Inicializar la lista para almacenar los números pares
numeros_pares = []

# Inicializar el contador
contador = 1

while contador <= 100:
    if contador % 2 == 0:  # Verificar si el número es par
        numeros_pares.append(contador)  # Agregar el número par a la lista
    contador += 1  # Incrementar el contador

print("Números pares entre 1 y 100:", numeros_pares)




