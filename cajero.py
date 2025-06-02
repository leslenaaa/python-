
class Cajero:
	def __init__(self):
		self.usuarios = {"vilma hernandez": "1234", "leslena hernandez": "5678"}  # Ejemplo de usuarios y PINs
		self.intentos = 3
		self.saldo = 1000.0  # Saldo inicial

	def iniciar_sesion(self):
		while self.intentos > 0:
			usuario = input("Ingrese su usuario: ")
			pin = input("Ingrese su PIN: ")
			if usuario in self.usuarios and self.usuarios[usuario] == pin:
				print("Inicio de sesión exitoso.\n")
				return True
			else:
				self.intentos -= 1
				print(f"Credenciales incorrectas. Intentos restantes: {self.intentos}\n")
		print("Demasiados intentos fallidos. Cuenta bloqueada.")
		return False

	def mostrar_saldo(self):
		print(f"Su saldo actual es: ${self.saldo}\n")

	def realizar_retiro(self):
		try:
			monto = float(input("Ingrese el monto a retirar: "))
			if monto <= 0:
				print("El monto debe ser mayor que 0.\n")
			elif monto > self.saldo:
				print("Saldo insuficiente.\n")
			else:
				self.saldo -= monto
				print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}\n")
		except ValueError:
			print("Entrada inválida. Por favor ingrese un número válido.\n")

	def menu(self):
		while True:
			print("\n Menú ")
			print("1. Consultar saldo")
			print("2. Retirar dinero")
			print("3. Salir")
			opcion = input("Seleccione una opción: ")
			if opcion == "1":
				self.mostrar_saldo()
			elif opcion == "2":
				self.realizar_retiro()
			elif opcion == "3":
				print("Gracias por usar el cajero automático.")
				break
			else:
				print("Opción no válida. Intente de nuevo.\n")

# main.py
# from cajero import Cajero # type: ignore

def main():
	cajero = Cajero()
	if cajero.iniciar_sesion():
		cajero.menu()

if __name__ == "__main__":
	main()
