import random

def juego_adivinanza():
	# Genera un número secreto aleatorio entre 1 y 50
	numero_secreto = random.randint(1, 50)
	intentos = 4  # Número de intentos permitidos
	
	print("Bienvenido al juego de adivinanza!")
	print("Debes adivinar un número entre 1 y 50. Tienes 4 intentos.")
	print("Escribe 'salir' en cualquier momento para terminar el juego.")
	
	while intentos > 0:  # Mientras queden intentos
		entrada = input("Ingresa tu número: ")
		
		# Permite al usuario salir del juego escribiendo "salir"
		if entrada.lower() == "salir":
			print("Juego terminado. ¡Hasta la próxima!")
			return  # Termina la función
		
		# Verifica si la entrada es un número válido
		if not entrada.isdigit() or not (1 <= int(entrada) <= 50):
			print("Por favor, ingresa un número válido entre 1 y 50.")
			continue  # Pide otro número
		
		numero_ingresado = int(entrada)  # Convierte la entrada a entero
		
		# Compara el número ingresado con el número secreto
		if numero_ingresado == numero_secreto:
			print("¡Felicidades! Has adivinado el número secreto.")
			return  # Termina el juego si adivina correctamente
		elif numero_ingresado < numero_secreto:
			print("Intenta con un número mayor.")
		else:
			print("Intenta con un número menor.")
		
		intentos -= 1  # Resta un intento
		print(f"Intentos restantes: {intentos}")
	
	# Si se agotan los intentos, revela el número secreto
	print(f"Se han agotado los intentos. El número secreto era {numero_secreto}.")

# Llama a la función para iniciar el juego
juego_adivinanza()
