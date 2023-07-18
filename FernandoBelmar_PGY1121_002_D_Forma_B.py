import numpy as np

filas=10
columnas=4

listaRuts=[]
lista_departamentos=[]
listaTipos=["A","B","C","D"]

for i in range(filas):
    for j in listaTipos:
        lista_departamentos.append(f"{filas-i}{j}")

matriz_departamentos=np.array(lista_departamentos).reshape(filas,columnas)

listaVentas=[0,0,0,0] #[A][B][C][D]
cantidadVentas=[0,0,0,0] #[A][B][C][D]

def mensaje_error():
    print("El dato que ha ingresado es inválido o se han cometido demasiados errores. Por favor inténtelo de nuevo. ")

def print_matriz(filas,columnas,matriz):
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i][j]:>3s}", end= ' ')
        print()

def marcar_departamento(matriz,departamento):
    indices=np.where(matriz == departamento)
    fila=indices[0][0]
    columna=indices[1][0]
    matriz[fila][columna]="X"

def set_price(index):
    global listaVentas,cantidadVentas
    precios=np.array([3800,3000,2800,3500])
    precioDepartamento=precios[index]
    listaVentas[index]+=precioDepartamento
    cantidadVentas[index]+=1

def calculo_venta(eleccion):
    global listaTipos
    if listaTipos[0] in eleccion:
        set_price(0)
    elif listaTipos[1] in eleccion:
        set_price(1)
    elif listaTipos[2] in eleccion:
        set_price(2)
    elif listaTipos[3] in eleccion:
        set_price(3)

def validacion_datos():
    global matriz_departamentos,listaRuts
    contadorError=0
    while contadorError<3:
        rut=int(input("Ingrese su rut sin puntos ni guion ni dígito verificador. Ej: 12345678:\n"))
        if (1000000<rut<30000000 and rut not in listaRuts):
            return True
        else:
            print("El rut es inválido o ya ha sido registrado.")
            contadorError+=1
    return False

def venta(matriz_departamentos):
    global filas,columnas,listaRuts
    try:
        if validacion_datos():
            contadorError=0
            while contadorError<3:
                print_matriz(filas,columnas,matriz_departamentos)
                eleccion=input("Elija su departamento a comprar:\n")
                for j in eleccion:
                    if j.isalpha() and j.islower():
                        index=eleccion.index(j)
                        eleccion=eleccion[:index] + j.upper()
                if not (eleccion in matriz_departamentos):
                    print("Departamento no existe o ya está ocupado.")
                    contadorError+=1
                else:
                    marcar_departamento(matriz_departamentos,eleccion)
                    calculo_venta(eleccion)
                    listaRuts.append(rut)
                    print(f"Ha comprado con éxito su departamento {eleccion}.")
                    return
            mensaje_error()
            return
    except Exception as e:
        print(f"Se ha capturado el error: {e}")

def listado_compradores(matriz_ruts):
    matrizRuts=np.sort(matriz_ruts)
    if len(matrizRuts)>0:
        print("Estos son los ruts que han hecho compras:")
        for i in matrizRuts:
            print(i)
    else:
        print("Aún no se han hecho compras.")

def printTabla(indice):
    global cantidadVentas,listaVentas,listaTipos
    print(f"    Tipo {listaTipos[indice]}:              {cantidadVentas[indice]}                {listaVentas[indice]}")


def ventasTotales():
    global cantidadVentas,listaVentas
    print("Tipo de Departamento    Cantidad       Total")
    for i in range(len(cantidadVentas)):
        printTabla(i)
    print(f"TOTAL                    {sum(cantidadVentas)}               {sum(listaVentas)}")
    
#Menu

menuActivo= True
print("Bienvenido a la inmobiliaria Casa Feliz. Estas son sus opciones:\n")
while menuActivo:
    print("1) Comprar departamento\n2) Mostrar departamentos disponibles\n3) Ver listado de compradores\n4) Mostrar ganancias totales\n5) Salir")
    try:
        opcion=int(input("Su opción:\n"))
        match opcion:
            case 1:
                venta(matriz_departamentos)
            case 2:
                print_matriz(filas,columnas,matriz_departamentos)
            case 3:
                listado_compradores(listaRuts)
            case 4:
                ventasTotales()
            case 5:
                print("Ha salido del sistema. Fernando Belmar 12/07/2023")
                menuActivo=False
            case _:
                mensaje_error()
    except Exception as e:
        print(f"Se ha capturado el error: {e}")