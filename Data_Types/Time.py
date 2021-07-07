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



def convertTime_Medida2Medida(time,medidaIN,medidaOUT):
    # Convertir tiempo de un formato a otro
    # time valor Entero numerico del tiempo
    # formatIN formato de entrada: nanosegundos, milisegundos, segundos, minutos, horas, dias
    # formatOUT  formato de salida: nanosegundos, milisegundos, segundos, minutos, horas, dias
    # EXITO return valorEntero en formato hh,mm,ss,ms
    # ERROR return 0

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0
    formatos = "hh,mm,ss,ms"

    # ----- Comprobar condiciones Inciales ------

    if SStrings.numOfContains_Conjunt(medidaIN,formatos,",")!=1:
        condiciones = False
        motivo="Formato de entrada no reconocido, formatos valido: " + formatos

    if SStrings.numOfContains_Conjunt(medidaOUT,formatos,",")!=1:
        condiciones = False
        motivo="Formato de salida no reconocido, formatos valido: " + formatos


    # ---------------- Proceso  ---------------
    if condiciones == True:


        # Convertir el formato de entrada a microsegundos
        msIN = SNumbers.to_Int_Force(time,0,"DOWN")
        if medidaIN == "ms":
            # Formato actual
            pass

        if medidaIN == "ss":
            msIN = time*1000000

        if medidaIN == "mm":
            msIN = time*1000000*60

        if medidaIN == "hh":
            msIN = time*1000000*60*60


        # Convertir los msIN en el formato de salida
        if medidaOUT == "ms":
            # Formato actual
            pass

        if medidaOUT == "ss":
            msIN = msIN/1000000

        if medidaOUT == "mm":
            msIN = msIN/1000000
            msIN = msIN/60

        if medidaOUT == "hh":
            msIN = msIN/1000000
            msIN = msIN/60
            msIN = msIN/60


        return msIN
    else:
        # Mensaje de Error
        print("ERROR en convert_Time motivo:" + motivo)
        return salida





def convertTime_Format2Medida(time, medida):
    # Convertir un Tiempo a una mediad en horas, minutos, segundos, microsegundos
    # Float con valor numerico
    # Formato hh:mm:ss:ms
    # 0 en caso de error

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0
    medidas = "hh,mm,ss,ms"

    # ----- Comprobar condiciones Inciales ------

    if valideTimeFormat(time)==False:
        condiciones=False
        motivo="time no valido en formato: hh:mm:ss:ms"

    if SStrings.numOfContains_Conjunt(medida,medidas,",")!=1:
        condiciones=False
        motivo="Medida no valida, medidas validas: "+medidas

    # ---------------- Proceso  ---------------
    if condiciones == True:
        # Separar tiempo en sus medidas
        v = SStrings.toVector(time,":")
        hora = v[0]
        mins = v[1]
        segs = v[2]
        micr = v[3]

        # Convertir a numeros

        hora = SNumbers.to_Int(hora,0)
        mins = SNumbers.to_Int(mins,0)
        segs = SNumbers.to_Int(segs,0)
        micr = SNumbers.to_Int(micr,0)

        # Calcular todo a la unidad de medida dada

        if medida == "hh":
            salida = SNumbers.to_float(hora,0)
            salida = salida + (mins/60)
            salida = salida + (segs/3600)
            salida = salida + (micr/3600000000)
            pass

        if medida == "mm":
            salida = SNumbers.to_float(mins,0)
            salida = salida + (hora*60)
            salida = salida + (segs/60)
            salida = salida + (micr/60000000)
            pass

        if medida == "ss":
            salida = SNumbers.to_float(segs,0)
            salida = salida + (hora*3600)
            salida = salida + (mins*60)
            salida = salida + (micr/1000000)
            pass

        if medida == "ms":
            salida = SNumbers.to_Int(micr,0)
            salida = salida + (hora*60*60*1000000)
            salida = salida + (mins*60*1000000)
            salida = salida + (segs*1000000)
            pass

        return salida
    else:
        # Mensaje de Error
        print("ERROR en convert_Time motivo:" + motivo)
        return salida



def getMedida(time,medida):
    # Obtener un elemento del time
    # hh formato de 24 horas
    # Formato hh:mm:ss:ms
    # Salida en error None

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None
    medidas = "hh,mm,ss,ms"

    # ----- Comprobar condiciones Inciales ------

    if valideTimeFormat(time) == False:
        condiciones = False
        motivo = "Time no valido, formato: hh:mm:ss:ms"

    if SStrings.numOfContains_Conjunt(medida,medidas,",")!=1:
        condiciones=False
        motivo = "La medida a obtener no es valida, medidas valida: " + medidas

    # ---------------- Proceso  ---------------
    if condiciones == True:
        v = SStrings.toVector(time,":")

        if medida == "hh":
            return v[0]

        if medida == "mm":
            return v[1]

        if medida == "ss":
            return v[2]

        if medida == "ms":
            return v[3]

        return salida
    else:
        # Mensaje de Error
        print("ERROR en getTime motivo:" + motivo)
        return salida




def convertTime_Medida2Format(time,medida):
    # Convertir un Tiempo a una mediad en horas, minutos, segundos, microsegundos
    # Float con valor numerico
    # Formato hh:mm:ss:ms
    # Error return 00:00:00:0000

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = 0
    medidas = "hh,mm,ss,ms"

    # ----- Comprobar condiciones Inciales ------

    if SStrings.numOfContains_Conjunt(medida,medidas,",")!=1:
        condiciones=False
        motivo="Medida no valida, medidas validas: "+medidas


    # ---------------- Proceso  ---------------
    if condiciones == True:
        # Convertir el tiempo en Microsegundos como unidad basica
        msT = convertTime_Medida2Medida(time,medida,"ms")

        # Obtener los tiempos
        hh = convertTime_Medida2Medida(msT,"ms","hh")
        hh = SNumbers.to_Int(hh,0)
        mm = convertTime_Medida2Medida(msT,"ms","mm") - convertTime_Medida2Medida(hh,"hh","mm")
        mm = SNumbers.to_Int(mm,0)
        ss = convertTime_Medida2Medida(msT,"ms","ss") - convertTime_Medida2Medida(hh,"hh","ss") - convertTime_Medida2Medida(mm,"mm","ss")
        ss = SNumbers.to_Int(ss,0)
        ms = convertTime_Medida2Medida(msT,"ms","ms") - convertTime_Medida2Medida(hh,"hh","ms") - convertTime_Medida2Medida(mm,"mm","ms") - convertTime_Medida2Medida(ss,"ss","ms")
        ms = SNumbers.to_Int(ms,0)

        # Convertir en formato de salida
        salida = SStrings.to_String(hh)
        salida = salida + ":" + SStrings.to_String(mm) + ":" + SStrings.to_String(ss) + ":" + SStrings.to_String(ms)

        return salida
    else:
        # Mensaje de Error
        print("ERROR en convertTime_Medida2Format motivo:" + motivo)
        return salida






def calculeTime(timeA,operation,timeB):
    # Realizar una operacion entre el tiempoA y el tiempoB
    # hh formato de 24 horas
    # Formato hh:mm:ss:ms
    # Resultado en Formato hh:mm:ss:ms
    # Error return None

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

    if SStrings.numOfContains_Conjunt(operation,"+,-,*,/",",")!=1:
        condiciones=False
        motivo="Operador no valido, operadores validos: +,-,*,/"


    # ---------------- Proceso  ---------------
    if condiciones == True:
        # Obtener los datos en ms
        a = convertTime_Format2Medida(timeA,"ms")
        b = convertTime_Format2Medida(timeB,"ms")

        # Hacer la operacion entre los dos valores
        result = 0
        if operation == "+":
            result = a+b

        if operation == "-":
            result = a-b

        if operation == "*":
            result = a*b

        if operation == "/":
            result = a/b


        # Darle formato al resultado
        salida = convertTime_Medida2Format(result,"ms")

        return salida
    else:
        # Mensaje de Error
        print("ERROR en calculeTime motivo:" + motivo)
        return salida
