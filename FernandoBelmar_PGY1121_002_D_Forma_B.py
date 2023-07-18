import numpy as np

filas = 10
columnas = 4

lista_ruts = []
lista_departamentos = []
lista_tipos = ["A", "B", "C", "D"]

for i in range(filas):
    for j in lista_tipos:
        lista_departamentos.append(f"{filas - i}{j}")

matriz_departamentos = np.array(lista_departamentos).reshape(filas, columnas)

lista_ventas = [0, 0, 0, 0]  # [A][B][C][D]
cantidad_ventas = [0, 0, 0, 0]  # [A][B][C][D]

def mensaje_error():
    print("El dato que ha ingresado es inválido o se han cometido demasiados errores. Por favor inténtelo de nuevo. ")

def print_matriz(filas, columnas, matriz):
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i][j]:>3s}", end=' ')
        print()

def marcar_departamento(matriz, departamento):
    indices = np.where(matriz == departamento)
    fila = indices[0][0]
    columna = indices[1][0]
    matriz[fila][columna] = "X"

def set_price(index):
    global lista_ventas, cantidad_ventas
    precios = np.array([3800, 3000, 2800, 3500])
    precio_departamento = precios[index]
    lista_ventas[index] += precio_departamento
    cantidad_ventas[index] += 1

def calculo_venta(eleccion):
    global lista_tipos
    if lista_tipos[0] in eleccion:
        set_price(0)
    elif lista_tipos[1] in eleccion:
        set_price(1)
    elif lista_tipos[2] in eleccion:
        set_price(2)
    elif lista_tipos[3] in eleccion:
        set_price(3)

def validacion_datos():
    global matriz_departamentos, lista_ruts
    contador_error = 0
    while contador_error < 3:
        rut = int(input("Ingrese su rut sin puntos ni guion ni dígito verificador. Ej: 12345678:\n"))
        if 1000000 < rut < 30000000 and rut not in lista_ruts:
            return rut
        else:
            print("El rut es inválido o ya ha sido registrado.")
            contador_error += 1
    return None

def venta(matriz_departamentos):
    global filas, columnas, lista_ruts
    try:
        rut = validacion_datos()
        if rut is not None:
            contador_error = 0
            while contador_error < 3:
                print_matriz(filas, columnas, matriz_departamentos)
                eleccion = input("Elija su departamento a comprar:\n")
                eleccion = eleccion.upper()
                if eleccion not in matriz_departamentos:
                    print("Departamento no existe o ya está ocupado.")
                    contador_error += 1
                else:
                    marcar_departamento(matriz_departamentos, eleccion)
                    calculo_venta(eleccion)
                    lista_ruts.append(rut)
                    print(f"Ha comprado con éxito su departamento {eleccion}.")
                    return
            mensaje_error()
    except ValueError:
        print("El rut ingresado es inválido.")
    except Exception as e:
        print(f"Se ha capturado el error: {e}")

def listado_compradores(lista_ruts):
    matriz_ruts = np.sort(lista_ruts)
    if len(matriz_ruts) > 0:
        print("Estos son los ruts que han hecho compras:")
        for rut in matriz_ruts:
            print(rut)
    else:
        print("Aún no se han hecho compras.")

def print_tabla(indice):
    global cantidad_ventas, lista_ventas, lista_tipos
    print(f"    Tipo {lista_tipos[indice]}:              {cantidad_ventas[indice]}                {lista_ventas[indice]}")

def ventas_totales():
    global cantidad_ventas, lista_ventas
    print("Tipo de Departamento    Cantidad       Total")
    for i in range(len(cantidad_ventas)):
        print_tabla(i)
    print(f"TOTAL                    {sum(cantidad_ventas)}               {sum(lista_ventas)}")

# Menu

menu_activo = True
print("Bienvenido a la inmobiliaria Casa Feliz. Estas son sus opciones:\n")
while menu_activo:
    print("1) Comprar departamento\n2) Mostrar departamentos disponibles\n3) Ver listado de compradores\n4) Mostrar ganancias totales\n5) Salir")
    try:
        opcion = int(input("Su opción:\n"))
        match opcion:
            case 1:
                venta(matriz_departamentos)
            case 2:
                print_matriz(filas, columnas, matriz_departamentos)
            case 3:
                listado_compradores(lista_ruts)
            case 4:
                ventas_totales()
            case 5:
                print("Ha salido del sistema. Fernando Belmar 12/07/2023")
                menu_activo = False
            case _:
                mensaje_error()
    except ValueError:
        print("Opción inválida. Ingrese un número válido.")
    except Exception as e:
        print(f"Se ha capturado el error: {e}")
