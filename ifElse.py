# if una opcion
# condicion true o false

if 4==7: 
	print("es igual")

if 4 !=7:
	print("es diferente")

	# numero es par, impar, negativo o positivo

	respuesta = int(input ("ingresa el numero "))

	if respuesta % 2 == 0: 
		respuesta = 15
		print("es par")
	else:
		print("es impar")

	if respuesta < 0 :
		print("negativo")
	else:
		print("positivo")
	
if respuesta == 0 : print("el numero ingresado es 0")


resultado = "es par" if respuesta % 2 == 0 else "es impar"
resultado2 = "negativo" if respuesta < 0 else "positivo"
print(f"{resultado} , {resultado2}")

#definir el numero por
#def nombre ()

def modulo(valor):

	valor = True  if respuesta % 2 == 0 else False
	print(valor)
	return valor

# las funciones son estructuras de codigo que se ejecutan mediante su llamao nombre()
# funcion si es positivo

def signo( valor):
	valor = True if respuesta < 0 else False
	print(valor)
	return valor


def detectarletras(valor):
	if any(c.isalpha()for c in str(valor)):
		print(True)
		return True
	else:
		return False
	
		#any es una funcion que ya trae python
		#si hay un elemento que es true la funcion nos devolvera 
		#true de lo contrario false
		#for c es una variable temporal 
		#for dara las vueltas necesarias para terminar el numero segun sus caracteres
        #isalpha nos indica si todos los caracteres son letras o numeros 

valor = 4 
modulo(valor)
signo(valor)
detectarletras(45)

def ejecutar():
	pedirvalor = int(input("ingrese el numero"))
	if pedirvalor == True:
		ejecutar()
	else:
		mrespuesta = modulo(pedirvalor)
		#valor = True if respuesta < 0 else False
		srespuesta = signo(pedirvalor)
		# valor = True  if respuesta % 2 == 0 else False
		#positivo y par
		
		if mrespuesta and srespuesta == True:
			print("positivo y par")
		if mrespuesta and srespuesta == False:
			print("negativo y impar")
	ejecutar()
		
		






