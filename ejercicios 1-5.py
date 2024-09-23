#Ejercicio 1
# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ")

# Convertir la letra a minúscula
letra = letra.lower()

# Mostrar el resultado
print("La letra en minúscula es:", letra)

#Ejercicio 2
def obtener_entrada():
    entrada = input("Por favor, ingresa solo letras: ")
    
    # Verificamos que la entrada sea solo letras
    while not entrada.isalpha():
        print("Entrada inválida. Asegúrate de que solo ingresas letras.")
        entrada = input("Por favor, ingresa solo letras: ")
    
    print(f"Has ingresado: {entrada}")

obtener_entrada()

#Ejercicio 3
def obtener_entrada():
    contador_invalidos = 0  # Inicializamos el contador de entradas inválidas
    entrada = input("Por favor, ingresa solo letras: ")

    # Verificamos que la entrada sea solo letras
    while not entrada.isalpha():
        contador_invalidos += 1  # Incrementamos el contador por entrada inválida
        print("Entrada inválida. Asegúrate de que solo ingresas letras.")
        entrada = input("Por favor, ingresa solo letras: ")

    print(f"Has ingresado: {entrada}")
    print(f"Entradas inválidas: {contador_invalidos}")

obtener_entrada()


#Ejercicio 4
def validar_letra():
    contador_invalidos = 0  # Inicializamos el contador de entradas inválidas

    while True:
        entrada = input("Por favor, ingresa solo letras: ")
        
        # Verificamos que la entrada sea solo letras
        if entrada.isalpha():
            return entrada  # Devuelve la letra válida
        else:
            contador_invalidos += 1  # Incrementamos el contador por entrada inválida
            print("Entrada inválida. Asegúrate de que solo ingresas letras.")

    # Este print nunca se ejecutará, pero se podría usar si se desea mostrar las entradas inválidas al final
    print(f"Entradas inválidas: {contador_invalidos}")

def main():
    letra_valida = validar_letra()  # Llamamos a la función de validación
    print(f"Has ingresado: {letra_valida}")

main()


#Ejercicio 5
import re

def validar_letra():
    contador_invalidos = 0  # Inicializamos el contador de entradas inválidas
    patron = r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+$'  # Expresión regular para letras españolas

    while True:
        entrada = input("Por favor, ingresa solo letras (incluyendo ñ y tildes): ")
        
        # Verificamos que la entrada coincida con el patrón
        if re.fullmatch(patron, entrada):
            return entrada  # Devuelve la letra válida
        else:
            contador_invalidos += 1  # Incrementamos el contador por entrada inválida
            print("Entrada inválida. Asegúrate de que solo ingresas letras.")

def main():
    letra_valida = validar_letra()  # Llamamos a la función de validación
    print(f"Has ingresado: {letra_valida}")

main()
