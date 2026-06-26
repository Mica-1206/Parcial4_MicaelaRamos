vehiculos = []

def mostrar_menu():
    print("--- Menú ---")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehiculos")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Favor ingresar un número entre 1 y 6 ")
        except:
            print("Favor ingresar un numero valido. ")

def validar_modelo(modelo):
    return modelo.strip() != ""

def validar_año(año):
    try:
        año = int(año)
        return año > 1900
    except:
        return False

def validar_precio(precio):
    try:
        precio = float(precio)
        return precio > 0
    except:
        return False

def agregar_vehiculo(lista):
    modelo = input("Ingrese el modelo: ")
    if not validar_modelo(modelo):
        print("Error: el modelo no puede estar vacío")
        return

    año = int(input("Ingrese el año del vehiculo "))
    if not validar_año(año):
        print("Error: el año debe ser mayor a 1900")
        return

    precio = input("Ingrese el precio: ")

    if not validar_precio(precio):
        print("Error: el precio debe ser mayor a 0 ")
        return
    vehiculos = {
        "modelo": modelo, 
        "año": año,
        "precio": float(precio),
        "disponible": False
    }
    lista.append(vehiculos)
    print("Vehiculo agregado correctamente")

def buscar_vehiculo(lista, modelo):
    for i in range(len(lista)):
        if lista[i]["modelo"] == modelo:
                return i
    return -1

def eliminar_vehiculo(lista):
    modelo = input("Ingrese el modelo a eliminar ")
    posicion = buscar_vehiculo(lista, modelo)

    if posicion == -1:
        print(f"El vehiculo {modelo} no se encuentra registrado ")
    else:
        lista.pop(posicion)
        print("Vehiculo eliminado correctamente ")

def actualizar_disponibilidad(lista):
    for vehiculos in lista:
        if vehiculos["año"] >= 2020:
            vehiculos["disponible"] = True
        else:
            vehiculos["disponible"] = False

def mostrar_vehiculos(lista):
    actualizar_disponibilidad(lista)
    if len(lista) == 0:
        print("No hay vehiculos registrados. ")
        return

    print("--Lista de vehiculos--")
    for vehiculos in lista:
        print("modelo: ", vehiculos["modelo"])
        print("año", vehiculos["año"])
        print("precio", vehiculos["precio"])

        if vehiculos["disponible"]:
            print("Estado: Disponible ")
        else:
            print("Estado: No disponible ")

        print("*" * 45)



while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_vehiculo(vehiculos)

    elif opcion == 2:
        modelo = input("ingrese el modelo a buscar: ")
        posicion = buscar_vehiculo(vehiculos, modelo)

        if posicion == -1:
            print("Vehiculo no encontrado ")
        else:
            print("posicion: ", posicion)
            print("modelo:", vehiculos[posicion]["modelo"])
            print("año", vehiculos[posicion]["año"])
            print("precio", vehiculos[posicion]["precio"])
            print("disponible", vehiculos[posicion]["disponible"])

    elif opcion == 3:
        eliminar_vehiculo(vehiculos)
    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("disponibilidad actualizada ")

    elif opcion == 5:
        mostrar_vehiculos(vehiculos)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto ")
        break
