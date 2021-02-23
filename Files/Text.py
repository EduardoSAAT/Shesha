import General.Strings as Shesha
import os
class Text():
    # Clase para el manejo de Archivos de Texto
    # Conteo desde 0 en adelante

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
        if Shesha.Strings.isNull_Empty(nameFile):
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
        if Shesha.Strings.isNull_Empty(nameFile):
            condiciones = False
            motivo = "Nombre de Archivo none o Empty"

        # ---------------- Proceso  ---------------
        if condiciones == True:
            os.remove(nameFile)
        else:
            # Mensaje de Error
            print("ERROR en DeleteFile motivo:" + motivo)


    @staticmethod
    def existsFile(nameFile):
        # Eliminar un Archivo

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True

        # ----- Comprobar condiciones Inciales ------
        if Shesha.Strings.isNull_Empty(nameFile):
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
        # None en caso de Error

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            f = open(self.pathName, "r")
            content = f.readlines()
            return content.__getitem__(index)
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

        # ---------------- Proceso  ---------------
        if condiciones == True:
            f = open(self.pathName, "r")
            content = f.readlines()
            content.pop(index)

            f = open(self.pathName, "w")
            content = "".join(content)
            f.write(content)
            f.close()
        else:
            # Mensaje de Error
            print("ERROR en deleteLine motivo:" + motivo)