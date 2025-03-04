#un cajero automatico
Usuario = list()

Usuario.append("leslena")
Usuario.append("1234")
Usuario.append(1000)

recibo= list()
recibo.append(["123",600])
recibo.append(["124",845])
recibo.append(["125",67])
recibo.append(["126",500])
recibo.append(["127",100])
recibo.append(["128",1000])

#git push -u origin main


acciones = list()
acciones.append("Depositar")
acciones.append("pago de resibo")
acciones.append("Retirar")


Usuario2 = list()
Usuario2.append("leslenaa")
Usuario2.append("12345")
Usuario2.append(1500)

def registrar():
    UsuarioRegistrado = list()
    usuarioc = input("Ingrese su nombre: ")
    UsuarioRegistrado.append(input("Ingrese su password"))

    if usuarioc == Usuario[0] and UsuarioRegistrado[0] == Usuario[1]:
        print("Bienvenido al cajero automatico")
    else:
        print("Usuario o contraseña incorrecta")
        return registrar()
