import Data_Types.Vector as Sesha_Vector

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
            print("ERROR en subStr_Before_Str motivo:" + motivo)
            return



    @staticmethod
    def subStr_After_Str(Str, subStr):
        # Obtener una subcadena Despues de una subcadena
        # ERROR entrega none

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            posicion = Strings.posContains(Str,subStr)

            if posicion>=0:
                return Strings.getSubStr_posA_posB(Str,posicion+len(subStr),len(Str))
        else:
            # Mensaje de Error
            print("ERROR en subStr_After_Str motivo:" + motivo)
            return




    @staticmethod
    def equals_IgnoreCase(StrA,StrB):
        # Comprobar si una cadea es igual a otra ignorando case

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = False

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(StrA):
            return salida

        if Strings.isNull_Empty(StrB):
            return salida


        # ---------------- Proceso  ---------------
        if condiciones == True:
            StrA = StrA.upper()
            StrB = StrB.upper()

            if StrA == StrB:
                return True
            else:
                return False
        else:
            # Mensaje de Error
            print("ERROR en equals_IgnoreCase motivo:" + motivo)
            return salida




    @staticmethod
    def posContains_Num(Str, subStr, numN, ignoreCase):
        # Encontrar la posicion de la Coincidencia Numero N de una subCad en una Cad
        # Error = -1   otro caso return 0 a len(Str)

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = -1

        # ----- Comprobar condiciones Inciales ------
        numContains=0
        cadAux=Str

        if ((numN<=0) or (numN>Strings.numOfContains(Str,subStr,ignoreCase))):
            condiciones=False
            motivo = "el valor de numM no es Correcto"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            for i in range(0,len(Str)+1):
                if len(subStr)+i<=len(Str):
                    cadAux = Strings.getSubStr_posA_posB(Str,i,i+len(subStr))

                    if ignoreCase:
                        if Strings.equals_IgnoreCase(cadAux,subStr):
                            numContains=numContains+1
                            if numContains==numN:
                                salida = i
                    else:
                        if cadAux==subStr:
                            numContains=numContains+1
                            if numContains==numN:
                                salida = i

            return salida
        else:
            # Mensaje de Error
            print("ERROR en posContains_Num motivo:" + motivo)
            return salida






    @staticmethod
    def replace_SubString_NUM(Str, subStr, StrNew, numConteins):
        # Remplazar una subcadena de coincidencia numero N encontrada en una Cad

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = ""

        # ----- Comprobar condiciones Inciales ------
        posConteins = Strings.posContains_Num(Str,subStr,numConteins,False)
        if posConteins<=-1:
            condiciones=False
            motivo=subStr+" numero:"+str(numConteins)+" no encontrada en:"+Str
            salida=Str

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Concatenar del inicio de la cadena Original Hasta la posicion del Contenido
            salida = salida + Strings.getSubStr_posA_posB(Str,0,posConteins)

            # Concatenar el remplazo
            salida = salida + StrNew

            # concatenar el resto de la cadena Original
            salida = salida + Strings.getSubStr_posA_posB(Str,posConteins+len(subStr),len(Str))

            return salida
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)
            return salida




    @staticmethod
    def replace_SubString_ALL(Str, subStr, StrNew):
        # Remplazar todas la coincidencias de una subcadena por un remplazo en una Cad

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida=Str

        # ----- Comprobar condiciones Inciales ------
        numConteins = Strings.numOfContains(Str,subStr,False)
        if (numConteins<=0) and (len(subStr)>0):
            condiciones=False
            motivo=subStr+" No encontrada en:"+Str

        # ---------------- Proceso  ---------------
        if condiciones == True:
            for x in range(0,numConteins):
                salida = Strings.replace_SubString_NUM(Str,subStr,StrNew,1)
                Str = salida

            return salida
        else:
            # Mensaje de Error
            print("ERROR en replace_SubString_ALL motivo:" + motivo)
            return salida



    @staticmethod
    def toVector(Str, separator):
        # Convertir una cadena a un vector de subcadenas
        # RETURN None error, otro caso vector

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        posVector=0
        temp=""

        # ----- Comprobar condiciones Inciales ------
        if (separator==None) or (Str==None):
            condiciones=False
            motivo="Cadena o Separador None"
        else:
            if len(separator)>len(Str):
                condiciones=False
                motivo="Separador mas grande que cadena a separar"
            else:
                # Normalizar Cadena

                # Si no hay caracter Final Agregarlo
                if (Strings.getSubStr_posA_posB(Str, len(Str) - len(separator), len(Str)) != separator):
                    Str = Str + separator

                # Si hay caracter al Inicio quitarlo a excepcion que sea el unico caracter
                if (len(Str) != len(separator)):
                    if (Strings.getSubStr_posA_posB(Str, 0, len(separator)) == separator):
                        Str = Strings.getSubStr_posA_posB(Str, len(separator), len(Str))

                # Obtener entonces el numero de elementos
                numElements = Strings.numOfContains(Str, separator, False)

                if numElements >= 1:
                    # Inicializar el Vector
                    salida = [None] * numElements
                    for i in range(0, numElements):
                        salida[i] = ""
                else:
                    condiciones = False
                    motivo = "La cadena no contiene Elementos"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            for i in range(0,len(Str)-1):
                # Obtener subcadena a evaluar si es Separador
                if i+len(separator)<=len(Str):
                    temp = Strings.getSubStr_posA_posB(Str,i,i+len(separator))

                # Si se encontro el separdor
                if temp == separator:
                    # No concatenar y saltar el separador
                    i = i+len(separator)-1
                    posVector = posVector+1
                else:
                    salida[posVector]=salida[posVector]+Strings.getSubStr_posA_posB(Str,i,i+1)

            return salida
        else:
            # Mensaje de Error
            print("ERROR en toVector motivo:" + motivo)
            return salida




    @staticmethod
    def Like(StrA, StrSimilar, pointVar,ignoreCase):
        # Descripcion: Comparar si una cadena se parece a otra con ciertos puntos de Variacion
        #   Ejemplo: "hola como estas amigo", "hola$estas$" = true
        #
        # @param StrA Cadena a Comparar
        # @param StrSimilar Cadena con puntos de variacion
        # @param pointVar Caracter de variacion
        # @param ignoreCase Ignorar Mayusculas de Minusculas
        # @return	valores de retorno



        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida=True

        vecFragmentCadParecida=None

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(StrA):
            condiciones = False
            motivo= "StrA es null o Empty"
            salida=False

        if Strings.isNull_Empty(StrSimilar):
            condiciones=False
            motivo="StrSimilar es null o Empty"
            salida=False


        if Strings.isNull_Empty(pointVar):
            condiciones=False
            motivo="pointVar es null o Empty"
            salida=False


        # ---------------- Proceso  ---------------
        if condiciones == True:
            #Si hay que ignorar mayusculas o minusculas
            if ignoreCase:
                StrA = StrA.upper()
                StrSimilar = StrSimilar.upper()
                pointVar=pointVar.upper()

            # Eliminar puntos de variacion Repetidos de la Cadena Parecida EJM: ho$$la -> ho$la
            while Strings.numOfContains(StrSimilar,pointVar+pointVar,False)>=2:
                StrSimilar = Strings.replace_SubString_ALL(StrSimilar,pointVar+pointVar,pointVar)


            # Convertir en fragmentos la cadena Parecida
            vecFragmentCadParecida=Strings.toVector(StrSimilar,pointVar)
            vecFragmentCadParecida=Sesha_Vector.Vector.delete_Element_ALL(vecFragmentCadParecida,"")

            # Buscar la posicion de cada framento de CadParecida en cadOriginal
            posFound=0          # posicion donde se encuentra el fragmento
            posInicio=0         # Posicion de Inicio de busqueda en cadena Original, esto es para hacer una busqueda progresiva
            posFin = len(StrA)  # y asi evitar el error de fragmentos repetidos obtener la misma posicion

            subCadProgresiva = StrA  # Ir avanzando conforme se encuentran fragmentos
            i=0
            while i<Sesha_Vector.Vector.lenFix(vecFragmentCadParecida):
                subCadProgresiva = Strings.getSubStr_posA_posB(subCadProgresiva, posInicio, posFin)
                posFound = Strings.posContains(subCadProgresiva, vecFragmentCadParecida[i])

                if posFound >= 0:
                    posInicio = posFound + len(vecFragmentCadParecida[i])
                    posFin = len(subCadProgresiva)
                else:
                    # Terminar porque no se encontro un fragmento y eso significa que no son parecidas
                    i = len(vecFragmentCadParecida)
                    salida = False

                i=i+1

            # Finalmente comprobar que los extremos inicio y fin se cumplan
            # para solucionar el error que si existen los fragmentos pero no deberian terminar o iniciar asi
            # EJM: "(INICIO/1/1)","(INICIO/$/"    o    "a(INICIO/1/1)","(INICIO/$/$)

            # Si no tienen punto de variacion Inicial entonces Primer fragmento debe ser el inicio de CadOriginal
            if (pointVar==Strings.getSubStr_posA_posB(StrSimilar,0,len(pointVar)))==False:
                if (vecFragmentCadParecida[0]==Strings.getSubStr_posA_posB(StrA,0,len(vecFragmentCadParecida[0])))==False:
                    salida=False

            # Si no tienen punto de variacion Final entonces Ultimo fragmento debe ser el fin de CadOriginal
            posA=len(StrA)-len(vecFragmentCadParecida[len(vecFragmentCadParecida)-1])
            posB=len(StrA)
            if (pointVar==Strings.getSubStr_posA_posB(StrSimilar,len(StrSimilar)-len(pointVar),len(StrSimilar)))==False:
                if (vecFragmentCadParecida[len(vecFragmentCadParecida)-1] == Strings.getSubStr_posA_posB(StrA,posA,posB)) == False:
                    salida=False

            return salida
        else:
            # Mensaje de Error
            print("ERROR en Like motivo:" + motivo)
            return salida





