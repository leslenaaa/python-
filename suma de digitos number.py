numero = input("Ingresa un número: ")

if numero.isdigit():  # Verifica si la entrada es un número válido
    suma = 0
    for digito in numero:
        suma += int(digito)
    print(f"La suma de los dígitos de {numero} es: {suma}")
else:
    print("Por favor, ingresa un número válido.")