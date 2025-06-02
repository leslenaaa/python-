import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
intentos_realizados = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He generado un número entre 1 y 100. ¡Adivina cuál es!")

while True:
    intento = input("Ingresa tu número: ")
    
    # Verificar si el intento es un número válido
    if not intento.isdigit():
        print("Por favor, ingresa un número válido.")
        continue

    intento = int(intento)
    intentos_realizados += 1

    # Comparar el intento con el número aleatorio
    if intento < numero_aleatorio:
        print("Más alto. ¡Intenta de nuevo!")
    elif intento > numero_aleatorio:
        print("Más bajo. ¡Intenta de nuevo!")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
        break
    intentos = 4  # Número de intentos permitidos