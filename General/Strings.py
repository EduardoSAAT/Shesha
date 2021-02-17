class Strings:
    #   Clase para el manejo de Strings en python
    #   Technotitlan
    #   v 0.1


    @staticmethod
    def contains(cad, subcad):
        # Metodo para ver se una subcadena se encuentra en una Cadena
        if cad.find(subcad)>=0:
            return True
        else:
            return False


    @staticmethod
    def posContains(cad, subcad):
        # Metodo para obtener la posicion de una Subcadena
        return cad.find(subcad)



    @staticmethod
    def numContains(Cad, subcad):
        # Obtener el numero de Subcadenas que hay en una cadena
        pass


    @staticmethod
    def getSubStr_posA_posB(cad, posA, posB):
        # Obtener una subcadena entre una posicionA y una posicionB inclusive
        # ERROR return none

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True


        # ----- Comprobar condiciones Inciales ------
        if posB < posA:
            condiciones = False
            motivo = "PosA es mayor a posB"

        if posB > len(cad) or posB < 0
            condiciones = False
            motivo = "PosB fuera de la Cadena"

        if posA < 0 or posA > len(cad)
            condiciones = false
            motivo = "PosA fuera de la Cadena"


        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Obtener la subcadena
            return cad[posA:posB + 1]
        else:
            # Mensaje de Error
            print("ERROR en getSubStr_posA_posB motivo:" + motivo)
            return




    @staticmethod
    def getSubStr_StrA_posB(cad, StrA, posB):
        # Obtener una subcadena entre una CadenaA y una posicionB
        # ERROR return none

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones=True

        # ----- Comprobar condiciones Inciales ------
        posA = Strings.posContains(cad, StrA)
        if posA >= 0:
            condiciones = True
        else:
            condiciones = False
            motivo = "Cadena:"+StrA+" no se encuentra en:"+cad

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Con la posicion de A previamente obtenida sacar la subcadena
            return Strings.getSubStr_posA_posB(cad,posA,posB)
        else:
            # Mensaje de Error
            print("ERROR en getSubStr_StrA_posB motivo:"+motivo)
            return




    @staticmethod
    def getSubStr_posA_StrB():
        # Obtener una subcadena entre una PosicionA y una CadenaB
        pass


    @staticmethod
    def getSubStr_StrA_StrB():
        # Obtener una subcadena entre una CadenaA y una CadenaB
        pass



