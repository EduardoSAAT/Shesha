# Archivo para el manejo de numeros



def isNumber(data):
    # Comprobar si un dato recibido es un tipo de dato Numerico

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = False

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        if (type(data) == int) or (type(data) == float):
            salida=True


        return salida
    else:
        # Mensaje de Error
        print("ERROR en isNumber motivo:" + motivo)
        return salida



def to_Int(value,error):
    # Convertir un Tipo de dato a Entero
    # value - Valor a convertir
    # error - Valor de salida en caso de error

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        try:
            salida = int(value)
        except:
            salida = error

        return salida
    else:
        # Mensaje de Error
        print("ERROR en to_Int motivo:" + motivo)
        return salida



def to_float(value,error):
    # Convertir un tipo de dato a Entero
    # value - Valor a convertir
    # error - Valor de salida en caso de error

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        try:
            salida = float(value)
        except:
            salida = error

        return salida
    else:
        # Mensaje de Error
        print("ERROR en to_float motivo:" + motivo)
        return salida
