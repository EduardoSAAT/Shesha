# Archivo de Clase experimental
# Para probar funcionalidades de python
import Data_Types.Time as STime
import time as time

state = True



def miFuncion():
    a = 2



    while True:
        global state

        if True == state:
            print("Es True")
        else:
            print("Es False")

        state = False


        if STime.getActualTime_Segundo()>30 and STime.getActualTime_Segundo()<59:
            # state = False
            #print("El estado esta Desactivo")
            pass
        else:
            # state = True
            #print("El estado esta Activo")
            pass

        time.sleep(1)


