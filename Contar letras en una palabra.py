palabra = input("Ingresa una palabra: ")
contador = 0

for letra in palabra:
    if letra.isalpha():  # Verifica si el carácter es una letra
        contador += 1

print(f'La palabra "{palabra}" tiene {contador} letras.')