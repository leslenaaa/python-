class Programa:
	def __init__(self):
		"""funcion principal del programa"""
		self.saldo = 1000  # Saldo inicial
		self.usuarios = {"leslena": "54321"}  # Usuario y PIN
		self.intentos = 3

def main():
	programa = Programa()
	print("1, menu principal")
	print("2, consultar saldo")
	print("3, retirar dinero")
	print("4, salir")

	opcion = int(input("ingrese una opcion: "))
	if opcion == 1:
		print(f"su saldo actual es de {programa.saldo:.2f}")
	elif opcion == 2:
		print(f"su saldo actual es de {programa.saldo:.2f}")
	elif opcion == 3:
		monto = float(input("ingrese la cantidad a retirar: "))
		if programa.saldo >= monto:
			programa.saldo -= monto
			print(f"retiro realizado con exito. su saldo nuevo es de {programa.saldo:.2f}")
		else:
			print("saldo insuficiente")
	elif opcion == 4:
		print("saliendo del programa")
	else:
		print("opcion no valida")

if __name__ == "__main__":
	main()