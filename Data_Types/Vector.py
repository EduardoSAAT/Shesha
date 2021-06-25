# Clase Avanzada para el manejo de Vectores
import Data_Types.Numbers as SNumbers
import Data_Types.Strings as SStrings



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








class Vector():
    vRaiz = []

    def __init__(self):
        pass


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
        # Agregar un elemento a la Derecha del Vector

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

            salida = suma/numElementsNumerics
            return salida
        else:
            # Mensaje de Error
            print("ERROR en getPromedio motivo:" + motivo)
            return salida



    def to_OnlyNumbers(self):
        # Convertir el vector a uno con solo valores numericos

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
                value = SNumbers.to_float(self.vRaiz[x], None)
                if SNumbers.isNumber(value) == False:
                    self.vRaiz.pop(x)
                    x=x-1

                x=x+1

        else:
            # Mensaje de Error
            print("ERROR en to_OnlyNumbers motivo:" + motivo)





