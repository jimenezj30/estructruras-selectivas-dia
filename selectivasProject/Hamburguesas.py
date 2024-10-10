#caso de estudio

#DEFINIR CONSTANTES
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

#FUNCION PARA CALCULAR EL PRECIO
def calcular_precio(tipo_hamburguesa, medio_pago, cantidad):

    #DEFINIR PRECIOS SEGUN EL TIPO DE HAMBURGUESA
    if tipo_hamburguesa == 1:
        precio = PRECIO_SENCILLA
        descripcion = "Sencilla"
    elif tipo_hamburguesa == 2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hamburguesa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None #Tipo de hamburguesa invalido


    #CALCULAR TOTAL SIN CARGOS
    total_sin_cargo = precio*cantidad


    #APLICAR IMPUESTO SI EL MEDIO DE PAGO ES TARJETA
    if medio_pago == 1:
       impuesto = round(total_sin_cargo*IMPUESTO_TARJETA)
    else:
        impuesto = 0
    total = round(total_sin_cargo+impuesto)

    #RETORNAR DATOS RELEVANTES
    return descripcion,precio,cantidad,impuesto,total

#FUNCION PARA GENERAR MENSAJE
def generar_mensaje(descripcion,precio,cantidad,impuesto,total):
    return(f"Tipo de hamburguesa {descripcion}\n"
           f"Precio {precio}\n"
           f"Cantidad {cantidad}\n"
           f"Impueso {impuesto}\n"
           f"Total {total}\n")

#FUNCION PARA VALIDAR LOS DATOS
def validar_datos(tipo_hamburguesa,medio_pago,cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado = calcular_precio(tipo_hamburguesa,medio_pago,cantidad)
        #print("Resultado: ",resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje( descripcion, precio, cantidad, impuesto, total)
        print("----------------------------------------------------\n"+mensaje)
    else:
        print("verifique las opciones ingresadas")

#ENTRADAS
tipo_hamburguesa = int(input("Ingrese tipo de hamburguesa \n1. Sencilla\n2. Doble\n3. Triple\n"))
medio_pago = int(input("Ingrese medio de pago \n1. Tarjeta\n2. Otro\n. "))
cantidad = int(input("Ingrese la cantidad: "))

#SALIDAS
validar_datos(tipo_hamburguesa,medio_pago,cantidad)


