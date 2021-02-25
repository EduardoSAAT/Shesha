class Vector():

    @staticmethod
    def lenFix(vector):
        # Obtener el numero de veces que un subCadena se encuentra en una Cadena
        # return 0 o si hay valores entonces de 1 a n

        if vector==None:
            return 0
        else:
            return len(vector)





    @staticmethod
    def delete_Element_ALL(array,element):
        # Elimina todos los Elementos X de un Vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------
        if array==None:
            condiciones=False
            motivo="Vector es None"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            salida=array

            i=0
            while i<len(salida):
                if salida[i]==element:
                    salida.__delitem__(i)
                    i=i-1
                i=i+1

            return salida
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)
            return salida

