# Libreria para el menejo de Tiempo y Fechas
from datetime import datetime
import Data_Types.Strings as SStrings
import Data_Types.Numbers as SNumbers
import Data_Types.Vector as SVector


def getActualTime_Year():
    now = datetime.now()
    return now.year

def getActualTime_Mes():
    now = datetime.now()
    return now.month

def getActualTime_Dia():
    now = datetime.now()
    return now.day

def getActualTime_Hora():
    now = datetime.now()
    return now.hour

def getActualTime_Mins():
    now = datetime.now()
    return now.minute

def getActualTime_Segundo():
    now = datetime.now()
    return now.second


def getActualTime_Microsecond():
    now = datetime.now()
    return now.microsecond




def getFecha():
    # Obtener la fecha en un formato sencillo
    # Formato dd/mm/aaaa

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = str(getActualTime_Dia())+"/"+str(getActualTime_Mes())+"/"+str(getActualTime_Year())
        return salida
    else:
        # Mensaje de Error
        print("ERROR en getFecha motivo:" + motivo)
        return salida


def getTime():
    # Obtener la Hora actual en un formato sencillo
    # hh formato de 24 horas
    # Formato hh:mm:ss:ms

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = str(getActualTime_Hora())+":"+str(getActualTime_Mins())+":"+str(getActualTime_Segundo())+":"+str(getActualTime_Microsecond())
        return salida
    else:
        # Mensaje de Error
        print("ERROR en getTime motivo:" + motivo)
        return salida




def convert_Time(medida):
    # Convertir un Tiempo a una mediad en horas, minutos, segundos, microsegundos
    # Float con valor numerico
    # Formato hh:mm:ss:ms
    # None en caso de error

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------



    # ---------------- Proceso  ---------------
    if condiciones == True:


        return salida
    else:
        # Mensaje de Error
        print("ERROR en getTime motivo:" + motivo)
        return salida




def valideTimeFormat(timeFormat):
    # Validar si una fecha cumple con el formato hh:mm:ss:ms
    # hh formato de 24 horas
    # Formato hh:mm:ss:ms

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = True

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        v = SStrings.toVector(timeFormat,":")

        # Comprobar que existan la cantidad de elementos requeridos
        if SVector.lengFix(v)!=4:
            salida=False
        else:
            # Comprobar que todos los elementos sean numericos
            for x in range(0,len(v)):
                if SNumbers.isNumber(v[x],True) == False:
                    salida=False

                # Comprobar el rango de los Numeros
                if x == 0:
                    if SNumbers.inRange(0,v[x],24) == False:
                        salida=False

                if (x == 1) or (x == 2):
                    if SNumbers.inRange(0,v[x],60) == False:
                        salida=False

                if (x == 3) :
                    if SNumbers.to_float_Force(v[x],0)<0:
                        salida=False

        return salida
    else:
        # Mensaje de Error
        print("ERROR en valideTimeFormat motivo:" + motivo)
        return salida



def calculeTime(timeA,operation,timeB):
    # Realizar una operacion entre el tiempoA y el tiempoB
    # hh formato de 24 horas
    # Formato hh:mm:ss

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    if valideTimeFormat(timeA)==False:
        condiciones=False
        motivo="timeA no tiene formato correcto"

    if valideTimeFormat(timeB)==False:
        condiciones=False
        motivo="timeB no tiene formato correcto"


    # ---------------- Proceso  ---------------
    if condiciones == True:



        return salida
    else:
        # Mensaje de Error
        print("ERROR en getTime motivo:" + motivo)
        return salida
