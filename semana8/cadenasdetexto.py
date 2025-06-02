imple = "hola mundo" 
print(imple)

#h 0
#o 1
#l 2
#a 3 
# 4
#m 5
#u 6 
#n 7
#d 8
#o 9 

holamundo = "' hola mundo'"
print(holamundo) 

#si queremos imprimir una cadena de texto con comillas dobles
# y que el resultado sea una cadena de texto con comillas simples
#se debe hacer lo siguiente "'hola mundo'"

holamundo = "'hola mundo'"
print(holamundo)

#\n salto de linea 
#\t tabulador
#\b retroceso
#\r retorno de carro
#\f santo de pagina
#\v tabulador vertical
#\\ diagonal invertida

salto2 = """hola mundo 

segunda linea"""
print(salto2)

holamundo = '"hola mundo"' + "desde mi casa"

holamundo[5]
print(holamundo[2 ])
for temp in holamundo:
	print(temp)
	if len(holamundo) != 0:
		print("la cadena de texto no esta vacia")
	else:
		print("la cadena de texto esta vacia")