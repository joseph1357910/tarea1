numeroUsuarios = input("Indique la cantidad de usuarios que va a ingresar al sistema: ")
columnas = 4

matInfoPersonal=[]
for i in range(int(numeroUsuarios)):
    matInfoPersonal.append([0] * columnas)

listaInfoPersonal=[]
for i in range(int(numeroUsuarios)):

    cedula = input(f"Ingrese el numero de cedula del usuario {i+1}: ")
    while cedula.isdigit() == False:
        print("El numero de cedula no debe contener letras")
        cedula = input(f"Ingrese el numero de cedula del usuario {i+1}: ")
    matInfoPersonal[i][0] = cedula

    nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
    while nombre.isalpha() == False:
        print("El nombre no debe contener numeros")
        nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
    matInfoPersonal[i][1] = nombre

    apellido1 = input(f"Ingrese el apellido 1 del usuario {i+1}: ")
    while apellido1.isalpha() == False:
        print("El apellido 1 no debe contener numeros")
        apellido1 = input(f"Ingrese el apellido 1 del usuario {i+1}: ")
    matInfoPersonal[i][2] = apellido1

    
    apellido2 = input(f"Ingrese el apellido 2 del usuario {i+1}: ")
    while apellido2.isalpha() == False:
        print("El apellido 2 no debe contener numeros")
        apellido2 = input(f"Ingrese el apellido 2 del usuario {i+1}: ")
    matInfoPersonal[i][3] = apellido2



matInfoCuentas=[]
for i in range(int(numeroUsuarios)):
    matInfoCuentas.append([0] * 3)

listaInfoCuentas=[]
for i in range(int(numeroUsuarios)):

    numerodecuenta = input(f"Ingrese el numero de cuenta del usuario {i+1}: ")
    while numerodecuenta.isdigit() == False:
        print("El numero de cuenta no debe contener letras")
        numerodecuenta = input(f"Ingrese el numero de cuenta del usuario {i+1}: ")
    matInfoCuentas[i][0] = numerodecuenta

    montodisponibleenlacuenta = input(f"Ingrese el monto disponible en la cuenta {i+1}: ")
    while  montodisponibleenlacuenta.isdigit() == False:
        print("El monto disponible en la cuenta no debe contener letras")
        montodisponibleenlacuenta = input(f"Ingrese el monto disponible en la cuenta {i+1}: ")
    matInfoCuentas[i][1] =  montodisponibleenlacuenta

    estadodelacuenta = input(f"ingrese el estado de la cuenta del usuario {i+1} (activa o inactiva): ")
    while estadodelacuenta.isalpha() == False:
        print("El estado de la cuenta no debe contener numeros")
        estadodelacuenta = input(f"ingrese el estado de la cuenta {i+1} (activa o inactiva: ")
    matInfoCuentas[i][2] = estadodelacuenta
    


print(matInfoPersonal)
print(matInfoCuentas)

def depositar(self, monto)
    if monto > 0:
        self.saldo =+ monto
        self.movimientos.append(f"Deposito: +{monto}")
    else:
        print("El monto de deposito debe ser mayor a 0")


def retirar(self, monto)
    if monto <= 0:
        print("El monto de retiro debe ser mayor a 0")
    elif monto > self.saldo
        print("Saldo insuficiente")
    else:
        self.saldo -= monto
        self.movimientos.append(f"Retiro: -{monto}")


def consulta(self)
    return self.saldo

def obtener_movimientos(self)
    return self.movimientos

matMovimientos=[]
for i in range(int(numeroUsuarios)):
    matInfoPersonal.append([0] * 1)
