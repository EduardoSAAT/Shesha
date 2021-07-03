# Clase Avanzada para el manejo de Vectores
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Data_Types'))
import Numbers as SNumbers
import Strings as SStrings
from copy import deepcopy


# Clase con sus Metodos
class Vector():
    vRaiz = []

    def __init__(self):
        self.vRaiz = []



    def lengFix(self):
        # Obtener la longitud del Vector

        if self.vRaiz == None:
            return 0
        else:
            return len(self.vRaiz)



    def addRigth(self,element):
        # Agregar un elemento a la Derecha del Vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            self.vRaiz.append(element)
        else:
            # Mensaje de Error
            print("ERROR en addRigth motivo:" + motivo)
            return salida


    def addLeft(self,element):
        # Agregar un elemento a la Derecha del Vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            self.vRaiz.insert(0,element)
        else:
            # Mensaje de Error
            print("ERROR en addLeft motivo:" + motivo)
            return salida


    def inset(self,element,position):
        # Agregar un elemento a la Derecha del Vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            self.vRaiz.insert(position,element)
        else:
            # Mensaje de Error
            print("ERROR en inset motivo:" + motivo)
            return salida


    def print(self):
        # Imprimir el objeto vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            print(self.vRaiz)
        else:
            # Mensaje de Error
            print("ERROR en print motivo:" + motivo)
            return salida


    def print(self,separador):
        # Imprimir los elementos del vector con un separador

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            for x in range(0,self.lengFix()):
                element = self.getItem_index(x)
                print(element,end=separador)
        else:
            # Mensaje de Error
            print("ERROR en print motivo:" + motivo)
            return salida




    def getItem_index(self,index):
        # Agregar un elemento a la Derecha del Vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        if index<0 or index>=self.lengFix():
            condiciones=False
            motivo="Posicion: "+str(index)+" fuera del vector"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            return self.vRaiz[index]
        else:
            # Mensaje de Error
            print("ERROR en getItem_index motivo:" + motivo)
            return salida



    def getMin_Numeric(self,error):
        # Obtener el numero mas pequeño del vector
        # error Si no encuentra Numeros

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()==0:
            condiciones=False
            motivo="No hay elementos en el vector"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            #Obtener un primer valor inicial minimo
            actual_min = salida
            firstFound = True
            for x in range(0,self.lengFix()):
                dato = self.vRaiz[x]
                try:
                    valor = float(dato)

                    # Si se pudo convertir a Numero entonces operar
                    if firstFound:
                        actual_min = valor
                        firstFound = False
                    else:
                        if valor < actual_min:
                            actual_min = valor
                except:
                    pass


            return actual_min
        else:
            # Mensaje de Error
            print("ERROR en getMin_Numeric motivo:" + motivo)
            return salida




    def getMax_Numeric(self,error):
        # Obtener el numero mas grande del vector
        # error Si no encuentra Numeros

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()==0:
            condiciones=False
            motivo="No hay elementos en el vector"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            #Obtener un primer valor inicial minimo
            actual_max = salida
            firstFound = True
            for x in range(0,self.lengFix()):
                dato = self.vRaiz[x]
                try:
                    valor = float(dato)

                    # Si se pudo convertir a Numero entonces operar
                    if firstFound:
                        actual_max = valor
                        firstFound = False
                    else:
                        if valor > actual_max:
                            actual_max = valor
                except:
                    pass


            return actual_max
        else:
            # Mensaje de Error
            print("ERROR en getMax_Numeric motivo:" + motivo)
            return salida







    def getMin_AlfaNumeric(self,error):
        # Obtener el valor mas pequeño alfanumericamente
        # error Valor de salida en caso de error

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()==0:
            condiciones=False
            motivo="No hay elementos en el vector"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            #Obtener un primer valor inicial minimo
            actual_min = self.vRaiz[0]
            for x in range(0,self.lengFix()):
                dato = self.vRaiz[x]

                if dato < actual_min:
                    actual_min = dato

            return actual_min
        else:
            # Mensaje de Error
            print("ERROR en getMin_AlfaNumeric motivo:" + motivo)
            return salida

    def getMax_AlfaNumeric(self, error):
        # Obtener el valor mas pequeño alfanumericamente
        # error Valor de salida en caso de error

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix() == 0:
            condiciones = False
            motivo = "No hay elementos en el vector"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Obtener un primer valor inicial minimo
            actual_max = self.vRaiz[0]
            for x in range(0, self.lengFix()):
                dato = self.vRaiz[x]

                if dato > actual_max:
                    actual_max = dato

            return actual_max
        else:
            # Mensaje de Error
            print("ERROR en getMax_AlfaNumeric motivo:" + motivo)
            return salida



    def getPromedio(self,error):
        # Obtener el promedio de unicamente los datos numericos del vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()<=0:
            condiciones=False
            motivo="Vector vacio"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            suma = 0
            numElementsNumerics = 0
            for x in range(0,self.lengFix()):
                try:
                    valor = float(self.vRaiz[x])
                    suma = suma+valor

                    numElementsNumerics = numElementsNumerics+1
                except:
                    pass


            if numElementsNumerics<=0:
                salida=0
            else:
                salida = suma/numElementsNumerics


            return salida
        else:
            # Mensaje de Error
            print("ERROR en getPromedio motivo:" + motivo)
            return salida



    def getModaDiferencial(self,error,Diferencial):
        # Obtener la moda diferencial del vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = error

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()<=0:
            condiciones=False
            motivo="Vector vacio"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Bandera de la moda, inicialmente el elemento 1
            pos = 0
            countModa = 0


            #Para cada elemento comprobar sus repeticiones
            countActual = 0
            for x in range(0,self.lengFix()):
                elementActual = SNumbers.to_float(self.vRaiz[x],0)
                min = elementActual - Diferencial
                max = elementActual + Diferencial

                #Contar las repeticiones del elemento actual
                for y in range(0,self.lengFix()):
                    if y==x:
                        # Si es el mismo elemento, no contarlo 2 veces
                        pass
                    else:
                        # Obtener el elemento a contabilizar
                        value = SNumbers.to_float(self.vRaiz[y],0)

                        # Si el elemento esta en el rango
                        if SNumbers.inRange(min,value,max):
                            countActual = countActual+1

                # Finalmente comprobar si el elemento actual es la nueva moda
                if countActual>countModa:
                    pos = x
                    countModa=countActual


            # Finalmente entregar la moda
            return self.vRaiz[pos]
        else:
            # Mensaje de Error
            print("ERROR en getPromedio motivo:" + motivo)
            return salida



    def is_OnlyNumbers(self):
        # Comprobar si este vector contiene elementos solo Numericos

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()<=0:
            condiciones=False
            motivo="Vector vacio"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            correct = True

            x = 0
            while x<self.lengFix():
                if SNumbers.isNumber(self.vRaiz[x],True) == False:
                    correct=False
                    x = self.lengFix()

                x = x+1

            return correct
        else:
            # Mensaje de Error
            print("ERROR en is_OnlyNumbers motivo:" + motivo)
            return False



    def to_OnlyNumbers(self):
        # Convertir este vector a uno con solo valores numericos

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        if self.lengFix()<=0:
            condiciones=False
            motivo="Vector vacio"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            x=0
            while x < self.lengFix():
                value = SNumbers.to_float_Force(self.vRaiz[x], None)
                if SNumbers.isNumber(value,True) == False:
                    self.vRaiz.pop(x)
                    x=x-1

                x=x+1
        else:
            # Mensaje de Error
            print("ERROR en to_OnlyNumbers motivo:" + motivo)










# Funciones de Archivo de Vectores

def delete_Element_ALL(array, element):
    # Elimina todos los Elementos X de un Vector

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------
    if array == None:
        condiciones = False
        motivo = "Vector es None"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = array

        i = 0
        while i < len(salida):
            if salida[i] == element:
                salida.__delitem__(i)
                i = i - 1
            i = i + 1

        return salida
    else:
        # Mensaje de Error
        print("ERROR en numOfContains motivo:" + motivo)
        return salida


def lengFix(vector):
    # Obtener la longitud del Vector

    if vector == None:
        return 0
    else:
        return len(vector)



def clone(SVector):
    # Funcion para clonar un objeto de la clase Vector

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida =  Vector()
        salida.vRaiz = deepcopy(SVector.vRaiz)

        return salida
    else:
        # Mensaje de Error
        print("ERROR en clone motivo:" + motivo)
        return salida



def to_Vector_OnlyNumbers(Svector):
    # Obtener un vector con solo valores numericos

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True

    # ----- Comprobar condiciones Inciales ------

    if Svector.lengFix() <= 0:
        condiciones = False
        motivo = "Vector vacio"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = clone(Svector)

        x = 0
        while x < salida.lengFix():
            value = SNumbers.to_float_Force(salida.vRaiz[x], None)
            if SNumbers.isNumber(value,True) == False:
                salida.vRaiz.pop(x)
                x = x - 1

            x = x + 1

        return salida
    else:
        # Mensaje de Error
        print("ERROR en to_Vector_OnlyNumbers motivo:" + motivo)





def to_Vector_Dx(Svector):
    # Obtener un vector Diferencial
    # Cada elemento es el resultado de la diferencia del valores siguiente menos el anterior
    # En caso de error Resultado: Vector con elementos vacios

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = Vector()

    # ----- Comprobar condiciones Inciales ------

    if Svector.lengFix() <= 0:
        condiciones = False
        motivo = "Vector vacio"

    if Svector.is_OnlyNumbers()==False:
        condiciones = False
        motivo="Vector Con Elementos No Numericos"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = Vector()

        for x in range(0, Svector.lengFix()-1):
            valNext = Svector.vRaiz[x+1]
            valNext = SNumbers.to_float(valNext,0)
            valBefore = Svector.vRaiz[x]
            valBefore = SNumbers.to_float(valBefore,0)

            Dx = valNext-valBefore
            salida.addRigth(Dx)


        return salida
    else:
        # Mensaje de Error
        print("ERROR en to_Vector_Dx motivo:" + motivo)
        return salida








