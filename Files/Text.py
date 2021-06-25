import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Data_Types'))
import Strings



# Funciones Generales

def existsFile(nameFile):
    # Eliminar un Archivo

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True

    # ----- Comprobar condiciones Inciales ------
    if Strings.isNull_Empty(nameFile):
        condiciones = False
        motivo = "Nombre de Archivo none o Empty"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        if os.path.exists(nameFile):
            return True
        else:
            return False
    else:
        # Mensaje de Error
        print("ERROR en DeleteFile motivo:" + motivo)






# Funciones de Objeto

class Text():
    # Clase para el manejo de Archivos de Texto
    # Conteo desde 1 en Adelante

    #Variables Globales de Clase
    pathName = ""  # Nombre y ruta del Archivo



    #Metodo de Construccion
    def __init__(self,nameFile):
        status = False
        self.pathName = nameFile




    @staticmethod
    def CreateNewFile(nameFile):
        # Crear un nuevo Archivo

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(nameFile):
            condiciones=False
            motivo="Nombre de Archivo none o Empty"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            open(nameFile,"w")
        else:
            # Mensaje de Error
            print("ERROR en CreateNewFile motivo:" + motivo)



    @staticmethod
    def DeleteFile(nameFile):
        # Eliminar un Archivo

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(nameFile):
            condiciones = False
            motivo = "Nombre de Archivo none o Empty"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            os.remove(nameFile)
        else:
            # Mensaje de Error
            print("ERROR en DeleteFile motivo:" + motivo)



    def addLine(self,line):
        # Agregar una nueva linea al final de Archivo

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            file_object = open(self.pathName,"a")
            file_object.write("\n"+line)
            file_object.close()
        else:
            # Mensaje de Error
            print("ERROR en numOfContains motivo:" + motivo)




    def insertLine(self,index,line):
        # Agregar una linea en una posicion especifica del Archivo
        # Desde 0 en Adelante posicion Lineal

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            file_object = open(self.pathName,"r")
            contents = file_object.readlines()
            file_object.close()

            contents.insert(index,line+"\n")

            f = open(self.pathName, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        else:
            # Mensaje de Error
            print("ERROR en InsertLine motivo:" + motivo)




    def getLine(self,index):
        # Obtener una linea del Archivo
        # None en caso de Error  Desde 1 hasta N

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            f = open(self.pathName, "r")
            content = f.readlines()
            return content.__getitem__(index-1)
        else:
            # Mensaje de Error
            print("ERROR en getLine motivo:" + motivo)
            return salida




    def deleteLine(self,index):
        # Eliminar una linea de un Archivo

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------
        if index<=0:
            condiciones=False
            motivo="Posicion No Valida"

        if index>self.numLines():
            condiciones=False
            motivo="Posicion no Valida"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            f = open(self.pathName, "r")
            content = f.readlines()
            content.pop(index-1)

            f = open(self.pathName, "w")
            content = "".join(content)
            f.write(content)
            f.close()
        else:
            # Mensaje de Error
            print("ERROR en deleteLine motivo:" + motivo)



    def numLines(self):
        # Obtener el numero de lineas de un Archivo, contando desde 1 hasta N
        # ERROR = -1    Vacio = 0

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = -1

        # ----- Comprobar condiciones Inciales ------
        if Strings.isNull_Empty(self.pathName):
            condiciones=False
            motivo="pathFile no definido"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            f = open(self.pathName, "r")
            count = 0

            for line in f:
                count+=1

            f.close()

            return count
        else:
            # Mensaje de Error
            print("ERROR en numLines motivo:" + motivo)
            return salida






    def getLineLike(self,Patron,pointVar):
        # Obtener la primer Linea que se parece a un Patron especifico
        # None NO encontro o Linea con Text

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------
        if (Patron==None) or (pointVar==None):
            condiciones=False
            motivo="El Patron o PuntoVariacion NULL"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            linea=""
            NumeroLineas = self.numLines()
            i=1
            while i<=NumeroLineas :
                linea= self.getLine(i)

                if Strings.Like(linea,Patron,pointVar,True):
                    salida=linea
                    i=NumeroLineas+1

                i=i+1

            return salida
        else:
            # Mensaje de Error
            print("ERROR en getLineLike motivo:" + motivo)
            return salida



    def posLineLike(Patron,pointVar):
        # Obtener el numero de la Linea que se parece a un Patron
        # -1 en ERROR  0 o mas posicion de linea

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = -1

        # ----- Comprobar condiciones Inciales ------
        if (Patron==None) or (pointVar==None):
            condiciones=False
            motivo="Patron o punto de variacion NULL"
            salida=-1

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # temp=get
            pass
        else:
            # Mensaje de Error
            print("ERROR en posLineLike motivo:" + motivo)
            return salida



    def getLineLikeN(self,Patron,pointVar,numMatch):
        # Obtener la N - esima Linea que se parece a un Patron especifico

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------
        if Patron==None or pointVar==None:
            condiciones=False
            motivo="El patron o punto de variacion es None"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            linea=""
            numMatchTemp=0
            numLines = self.numLines()

            i=1
            while i<=numLines:
                linea=self.getLine(i)

                if Strings.Like(linea,Patron,pointVar,True):
                    numMatchTemp = numMatchTemp+1
                    if numMatchTemp == numMatch:
                        salida=linea
                        i=numLines+1

                i=i+1

            return salida
        else:
            # Mensaje de Error
            print("ERROR en getLineLikeN motivo:" + motivo)
            return salida


    def posLineLikeN(self,Patron,pointVar,numMatch):
        # Obtener la N - esima Linea que se parece a un Patron especifico
        # -1 en ERROR  0 NoFound  Mayor a 1 Linea Correcta Encontrada

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = -1

        # ----- Comprobar condiciones Inciales ------
        if Patron==None or pointVar==None:
            condiciones=False
            motivo="El patron o punto de variacion es None"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            linea=""
            numMatchTemp=0
            numLines = self.numLines()

            i=1
            while i<=numLines:
                linea=self.getLine(i)

                if Strings.Like(linea,Patron,pointVar,True):
                    numMatchTemp = numMatchTemp+1
                    if numMatchTemp == numMatch:
                        salida=i
                        i=numLines+1

                i=i+1

            return salida
        else:
            # Mensaje de Error
            print("ERROR en getLineLikeN motivo:" + motivo)
            return salida







