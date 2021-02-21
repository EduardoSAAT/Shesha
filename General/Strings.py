class Strings:
    #   Clase para el manejo de Strings en python
    #   Technotitlan
    #   v 0.1



    @staticmethod
    def isNull_Empty(cad):
        # Comprobar si una cadena es null o empty

        if len(cad) == 0:
            return True
        else:
            return False



    @staticmethod
    def contains(cad, subcad):
        # Metodo para ver se una subcadena se encuentra en una Cadena
        if cad.find(subcad)>=0:
            return True
        else:
            return False


    @staticmethod
    def posContains(cad, subcad):
        #Obtener la posicon de una subcadena

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(cad):
            return -1
        else:
            if len(cad)>=1 and len(subcad)==0:
                return -1


        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Metodo para obtener la posicion de una Subcadena
            return cad.find(subcad)
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)




    @staticmethod
    def getSubStr_posA_posB(cad, posA, posB):
        # Obtener una subcadena entre una posicionA y una posicionB
        # ERROR return none

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True


        # ----- Comprobar condiciones Inciales ------
        if posB < posA:
            condiciones = False
            motivo = "PosA es mayor a posB"

        if posB > len(cad) or posB < 0:
            condiciones = False
            motivo = "PosB fuera de la Cadena"

        if posA < 0 or posA > len(cad):
            condiciones = False
            motivo = "PosA fuera de la Cadena"


        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Obtener la subcadena
            return cad[posA:posB]
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
        posA = Strings.posContains(cad,StrA)
        if posA==-1:
            condiciones = False
            motivo = StrA+" no encontrada en: "+cad

        if posA+len(StrA)>posB:
            condiciones=False
            motivo="PosB antes de posicion Inicial"

        if (posB<0) or (posB>len(cad)) :
            condiciones=False
            motivo="PosB fuera de Cadena"


        # ---------------- Proceso  ---------------
        if condiciones == True:
            posA=posA+len(StrA)
            return Strings.getSubStr_posA_posB(cad,posA,posB)
        else:
            # Mensaje de Error
            print("ERROR en getSubStr_StrA_posB motivo:"+motivo)
            return




    @staticmethod
    def getSubStr_posA_StrB(cad, posA, StrB):
        # Obtener una subcadena entre una PosicionA y una CadenaB
        # Error Cadena Vacia

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida=""

        # ----- Comprobar condiciones Inciales ------
        if (posA>len(cad)) or (posA<0):
            condiciones=False
            motivo="PosA fuera de: "+ cad

        # ---------------- Proceso  ---------------
        if condiciones == True:
            cadAux=Strings.getSubStr_posA_posB(cad,posA,len(cad))
            posCadF=Strings.posContains(cadAux,StrB)

            if posCadF>=0:
                salida = Strings.getSubStr_posA_posB(cad,posA,(posCadF+posA))
                return salida
            else:
                motivo = "Subcad:"+StrB+" no encontrada en:"+cadAux
                print("ERROR en getSubStr_posA_StrB motivo:" + motivo)
        else:
            # Mensaje de Error
            print("ERROR en getSubStr_posA_StrB motivo:" + motivo)
            return salida






    @staticmethod
    def getSubStr_StrA_StrB(cad, StrA, StrB):
        # Obtener una subcadena entre una CadenaA y una CadenaB
        # return none No hay subcadena ERROR  "" No hay nada entre cadenas o "cadena" lo que encontro

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        if(Strings.isNull_Empty(StrA)):
            condiciones = False
            motivo = "StrA es null o vacio"

        if(Strings.isNull_Empty(StrB)):
            condiciones = False
            motivo = "StrB es null o vacio"


        # ---------------- Proceso  ---------------
        if condiciones == True:
            posA = Strings.posContains(cad,StrA)

            if posA>=0:
                subCadRestante = Strings.getSubStr_posA_posB(cad,posA+len(StrA),len(cad))
                posB = Strings.posContains(subCadRestante,StrB)

                if posB==0:
                    # Significa que no hay nada entre las dos cadenas
                    return ""
                else:
                    if posB>0:
                        return Strings.getSubStr_posA_posB(subCadRestante,0,posB)
            else:
                #No existe cadena
                return salida
        else:
            # Mensaje de Error
            print("ERROR en getSubStr_StrA_StrB motivo:" + motivo)
            return



    @staticmethod
    def numOfContains(Str, subStr, ignoreCase):
        # Obtener el numero de veces que un subCadena se encuentra en una Cadena

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        contador = 0

        # ----- Comprobar condiciones Inciales ------

        if (ignoreCase==True):
            Str = Str.upper()
            subStr = subStr.upper()

        if (Strings.isNull_Empty(Str) or Strings.isNull_Empty(subStr)):
            return 0

        if (len(Str)>=1 and len(subStr)==0):
            return 0

        # ---------------- Proceso  ---------------
        if condiciones == True:
            inicio=0
            fin = len(subStr)

            continuar = True
            while continuar:
                if fin <= len(Str):
                    cadAux = Strings.getSubStr_posA_posB(Str,inicio,fin)

                    if cadAux == subStr:
                        contador = contador+1
                else:
                    continuar = False

                inicio=inicio+1
                fin=inicio+len(subStr)
            return contador
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)
            return contador




    @staticmethod
    def subStr_Before_Str(Str, subStr):
        # Obtener una subcadena antes de una cadena
        # ERROR entrega none

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            posicion = Strings.posContains(Str,subStr)

            if posicion>=0:
                return Strings.getSubStr_posA_posB(Str,0,posicion)
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)
            return



