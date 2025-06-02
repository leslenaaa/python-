# 50  5
#100 10
#200 12
#100 20 

compra = float(input("ingrese el monto de la compra:"))
unidades = int(input("ingrese la cantidad de productos:"))
descuento = 0
impuesto = 0 
if compra < 0 :
	print("el monto de la compra no puede ser negativo")
if unidades < 12 : descuento = 0
if unidades >= 12 : descuento = 0.02
if compra >=10 and compra < 50: impuesto = 0.05
if compra >50 and compra < 100: impuesto = 0.10
if compra >100 and compra < 200: impuesto = 0.20
if compra > 200 : impuesto = 0.20


resultado = compra * impuesto
montototal = compra + resultado - (descuento * compra )
print(descuento)
print("el impuesto a pagar es de:", montototal)

# pedir desde consola un monto de si compran 12 unidades 10% de descuento
# si compra 20 unidades 10% de descuento




