# Archivo para el manejo de numeros
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Data_Types'))
import Strings as SStrings
from math import floor,ceil



def isNumber(data,Tranformable):
    # Comprobar si un dato recibido es un tipo de dato Numerico o si puede ser convertido a numerico
    # Transformable True si se contemplan string que se pueden transformar a numeros, False no incluye eso

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = False

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        # Comprobar si es Numerico Puro
        if (type(data) == int) or (type(data) == float):
            salida=True

        # Comprobar si es Transformable a Numerico
        if Tranformable:
            number = to_float(data,None)
            if number != None:
                salida = True

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
    salida = error

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


def inRange(valMin, value, valMax):
    # Comprobar si un numero esta dentro de un rango
    # valMin - Valor Minimo inclusive
    # valMax - Valor Maximo inclisive

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = False

    # ----- Comprobar condiciones Inciales ------

    if isNumber(valMin,True) == False:
        condiciones=False
        motivo="valMin no es Numerico"

    if isNumber(value,True) == False:
        condiciones=False
        motivo="valMin no es Numerico"

    if isNumber(valMax,True) == False:
        condiciones=False
        motivo="valMin no es Numerico"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        vMin = to_float_Force(valMin,0)
        v = to_float_Force(value,0)
        vMax = to_float_Force(valMax,0)


        if (v>=vMin) and (v<=vMax):
            salida=True

        return salida
    else:
        # Mensaje de Error
        print("ERROR en inRange motivo:" + motivo)
        return salida



def porcentax_value(number, porcent):
    # Obtener el porcentaje de un numero

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    if isNumber(number,True) and isNumber(porcent,True):
        pass
    else:
        condiciones =False
        motivo="Los datos recibidos no son numericos"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = number/100*porcent

        return salida
    else:
        # Mensaje de Error
        print("ERROR en porcentax_value motivo:" + motivo)
        return salida


def porcentax_relax(sizeTotal, sizeSubtotal):
    # Calcular la relacion de porcentaje entre un conjunto total y un subconjunto
    # sizeTotal: Conjunto total de elementos
    # sizeSubtotal: Numero del subtotal de elementos
    # Resultado relacion del porcentaje
    # Error return 0

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0

    # ----- Comprobar condiciones Inciales ------

    if isNumber(sizeTotal,False)==False:
        condiciones = False
        motivo = "sizeTotal no es un numero"

    if isNumber(sizeSubtotal,False)==False:
        condiciones=False
        motivo = "sizeSubtotal no es un numero"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = (100*sizeSubtotal)/sizeTotal
        return salida
    else:
        # Mensaje de Error
        print("ERROR en porcentax_relax motivo:" + motivo)
        return salida




def to_float_Force(value,error):
    # Convertir un numero a float de forma forzada
    # Si es un strings con caracteres eliminarlos ejemplo
    # $520     ->   520
    # 1,250.50  -> 1250.50
    # 1252. -> 1252

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = error

    # ----- Comprobar condiciones Inciales ------

    if type(value)==str:
        if len(value)==0:
            return salida

    # ---------------- Proceso  ---------------
    if condiciones == True:
        # Si la entrada es un String, purificarlo -> eliminar caracteres excepto el . decimal
        if type(value)==str:
            # Eliminar todo elemento que no sea .
            x = 0
            while x<len(value)-1:
                caracter = value[x:x + 1]

                # Si no es un numero entonces eliminar ese elemento
                if isNumber(caracter, True) == False and caracter!="." and caracter!="-":
                    value = SStrings.deleteSubStr_posA_posB(value, x, x + 1)
                    x = x - 1
                x=x+1

            # Eliminar los . en caso de que esten al principio y al final, en ese caso no sirven
            if value[0:1] == ".":
                value = SStrings.deleteSubStr_posA_posB(value,0,1)

            if (value[len(value)-1:len(value)] == "."):
                value = SStrings.deleteSubStr_posA_posB(value, len(value)-1, len(value))

            # Comprobar si despues del proceso de purificar el String, este puede ser transformable
            if isNumber(value,True):
                return float(value)
            else:
                return salida
        else:
            #En otro caso simplemente transformar
            return to_float(value,error)
    else:
        # Mensaje de Error
        print("ERROR en to_float_Force motivo:" + motivo)
        return salida




def to_Int_Force(value,error,rounder):
    # Convertir un numero a float de forma forzada
    # Si es un strings con caracteres eliminarlos ejemplo
    # $520     ->   520
    # 1,250.50  -> 1250 o 1251 dependiendo el redondeo
    # 1252. -> 1252

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = error

    # ----- Comprobar condiciones Inciales ------
    redondeos = "UP,DOWN,CLOSE"
    if SStrings.numOfContains__Conjunt_IN_Str(redondeos,",",rounder)!=1:
        condiciones=False
        motivo="Metodo de redondeo no valido, metodos valido: "+redondeos

    # ---------------- Proceso  ---------------
    if condiciones == True:

        # Si la entrada es un String eliminar caracteres excepto el . decimal
        if type(value)==str:
            # Eliminar todo elemento que no sea .
            x = 0
            while x<len(value)-1:
                caracter = value[x:x + 1]

                # Si no es un numero entonces eliminar ese elemento
                if isNumber(caracter, True) == False and caracter!="." and caracter!="-":
                    value = SStrings.deleteSubStr_posA_posB(value, x, x + 1)
                    x = x - 1
                x=x+1

            # Eliminar los . en caso de que esten al principio y al final, en ese caso no sirven
            if value[0:1] == ".":
                value = SStrings.deleteSubStr_posA_posB(value,0,1)

            if (value[len(value)-1:len(value)] == "."):
                value = SStrings.deleteSubStr_posA_posB(value, len(value)-1, len(value))
        else:
            #En otro caso simplemente transformar
            value = to_float(value,error)
            return roundInteger(value,rounder)

        value = to_float(value,error)
        return roundInteger(value,rounder)
    else:
        # Mensaje de Error
        print("ERROR en to_float_Force motivo:" + motivo)
        return salida




def roundInteger(value,mode):
    # Redonder un numero a Entero
    # Modos "UP" "DOWN" "CLOSE"

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    if ((mode=="UP") or (mode=="DOWN") or (mode=="CLOSE")) == False:
        condiciones=False
        motivo="Modo de operacion no soportado -> modos de operacion: UP or DOWN or CLOSE"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        if mode == "CLOSE":
            salida = round(value)

        if mode == "UP":
            salida = ceil(value)

        if mode == "DOWN":
            salida = floor(value)


        return salida
    else:
        # Mensaje de Error
        print("ERROR en roundInteger motivo:" + motivo)
        return salida
