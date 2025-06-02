
usuario = list()

usuario.append("leslena hernandez")  # string str 
usuario.append("54321")          #string str
usuario.append(1000)            #int

recibo = list()
recibo.append(["350", 756]) 
recibo.append(["351", 775]) 
recibo.append(["352",  88]) 
recibo.append(["353", 850]) 
recibo.append(["354", 170]) 
recibo.append(["355", 1000]) 

acciones = list()
acciones.append("consulta tu saldo")
acciones.append("pago de recibo")
acciones.append("Retirar")

usuario2 = list()
usuario2.append(" leslenaa")
usuario2.append("12345")          
usuario2.append(1500)           

def registrar():
    usuarioRegistrado = list()
    usuarioC = input("Ingrese su nombre: ")
    usuarioRegistrado.append("Ingrese su password: ")

    if usuarioC == usuario[0] and usuarioRegistrado == usuario[1]:
        print("Bienvenido al cajero automatico")

def main():
    cajero = Cajero()
    if cajero.iniciar_sesion():
        cajero.menu()

if __name__ == "__main__":
    main()
