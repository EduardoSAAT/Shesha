# Robot para la automatizacion y el manejo de whatsapp
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Data_Types'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'System'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Files'))
import Text as SFiles
import Strings as SStrings
import Numbers as SNumbers
import Systems_Scripts as SSystem

class Whatsapp_bot():
    # Definir Varibales de Esta Clase
    pathFileConfig = ""

    # Coordenadas de funcionamiento

    # Abrir navegador Web
    Step1_alto = 0
    Step1_ancho = 0
    Step1_time = 0

    # Abrir pestaña en navegador
    Step2_alto = 0
    Step2_ancho = 0
    Step2_time = 0

    # Buscar persona o grupo
    Step3_alto = 0
    Step3_ancho = 0
    Step3_time = 0

    # Escribir en cuadro de chat
    Step4_alto = 0
    Step4_ancho = 0
    Step4_time = 0

    # Darle a boton enviar
    Step5_alto = 0
    Step5_ancho = 0
    Step5_time = 0

    # Darle a boton AddArchivo
    Step6_alto = 0
    Step6_ancho = 0
    Step6_time = 0



    # Constructor del Objeto, usando metodo especial __init__
    def __init__(self,fileConfig):
        # Comprobar si el archivo de configuracion existe
        if SFiles.existsFile(fileConfig):
            self.pathFileConfig = fileConfig
            self.cargar_config()
        else:
            print("Error en construir Whatsapp_bot()")
            print("No existe el archivo de configuracion: "+fileConfig)



    def cargar_config(self):
        # Mostrar la informacion de uso de este robot

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            file = SFiles.Text(self.pathFileConfig)

            posCoordenades = file.posLineLike("#Coordenadas(Start)#","#")

            # Obtener datos Paso1: Abrir Navegador Web
            line = file.getLine(posCoordenades+1)
            self.Step1_alto = SStrings.getSubStr_StrA_StrB(line,"alto(",")")
            self.Step1_alto = SNumbers.to_Int_Force(self.Step1_alto,0,"CLOSE")
            self.Step1_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step1_ancho = SNumbers.to_Int_Force(self.Step1_ancho, 0, "CLOSE")
            self.Step1_time = SStrings.getSubStr_StrA_StrB(line,"time(",")")
            self.Step1_time = SNumbers.to_Int_Force(self.Step1_time,0,"CLOSE")

            # Obtener datos Paso1: Abrir pestaña del navegador
            line = file.getLine(posCoordenades + 2)
            self.Step2_alto = SStrings.getSubStr_StrA_StrB(line, "alto(", ")")
            self.Step2_alto = SNumbers.to_Int_Force(self.Step2_alto, 0, "CLOSE")
            self.Step2_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step2_ancho = SNumbers.to_Int_Force(self.Step2_ancho, 0, "CLOSE")
            self.Step2_time = SStrings.getSubStr_StrA_StrB(line, "time(", ")")
            self.Step2_time = SNumbers.to_Int_Force(self.Step2_time, 0, "CLOSE")

            # Obtener datos Paso1: Buscar persona o grupo
            line = file.getLine(posCoordenades + 3)
            self.Step3_alto = SStrings.getSubStr_StrA_StrB(line, "alto(", ")")
            self.Step3_alto = SNumbers.to_Int_Force(self.Step3_alto, 0, "CLOSE")
            self.Step3_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step3_ancho = SNumbers.to_Int_Force(self.Step3_ancho, 0, "CLOSE")
            self.Step3_time = SStrings.getSubStr_StrA_StrB(line, "time(", ")")
            self.Step3_time = SNumbers.to_Int_Force(self.Step3_time, 0, "CLOSE")

            # Obtener datos Paso1: Escribir en cuadro de chat
            line = file.getLine(posCoordenades + 4)
            self.Step4_alto = SStrings.getSubStr_StrA_StrB(line, "alto(", ")")
            self.Step4_alto = SNumbers.to_Int_Force(self.Step4_alto, 0, "CLOSE")
            self.Step4_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step4_ancho = SNumbers.to_Int_Force(self.Step4_ancho, 0, "CLOSE")
            self.Step4_time = SStrings.getSubStr_StrA_StrB(line, "time(", ")")
            self.Step4_time = SNumbers.to_Int_Force(self.Step4_time, 0, "CLOSE")

            # Obtener datos Paso1: Darle al boton Enviar
            line = file.getLine(posCoordenades + 5)
            self.Step5_alto = SStrings.getSubStr_StrA_StrB(line, "alto(", ")")
            self.Step5_alto = SNumbers.to_Int_Force(self.Step5_alto, 0, "CLOSE")
            self.Step5_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step5_ancho = SNumbers.to_Int_Force(self.Step5_ancho, 0, "CLOSE")
            self.Step5_time = SStrings.getSubStr_StrA_StrB(line, "time(", ")")
            self.Step5_time = SNumbers.to_Int_Force(self.Step5_time, 0, "CLOSE")

            # Obtener datos Paso1: Darle al boton AddArchivo
            line = file.getLine(posCoordenades + 6)
            self.Step6_alto = SStrings.getSubStr_StrA_StrB(line, "alto(", ")")
            self.Step6_alto = SNumbers.to_Int_Force(self.Step6_alto, 0, "CLOSE")
            self.Step6_ancho = SStrings.getSubStr_StrA_StrB(line, "ancho(", ")")
            self.Step6_ancho = SNumbers.to_Int_Force(self.Step6_ancho, 0, "CLOSE")
            self.Step6_time = SStrings.getSubStr_StrA_StrB(line, "time(", ")")
            self.Step6_time = SNumbers.to_Int_Force(self.Step6_time, 0, "CLOSE")
        else:
            # Mensaje de Error
            print("ERROR en cargar_config motivo:" + motivo)
            return salida



    def info(Str):
        # Mostrar la informacion de uso de este robot

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            print("----------- Robot de Whatsapp -----------")
            print("Modelo: TTT_1.0")
            print("Info  : Roboto diseñado con Visicn Aritificlal")
            print("        Esto significa que requiere un entorno grafico")
            print("        Requisitos Entorno Grafico:")
            print("        -Navegador de Internet, cualquiera")
            print("        -Tener Whatsapp web previamente abierto")
            print("        -Espacio en pantalla disponible para ver el WebBrowser")
            print("        -Tener un navegador web no predeterminado exclusivo para whatsapp")
            print("        -Tener en la primer pestaña del navegador al whatsapp web")
            print("")
            print("Proceso de Ejecucion")
            print("1.- Ejecutar movimientos de mouse para abrir o posicionar Whatsapp en la pantalla")
            print("2.- Ejecutar movimientos de mouse y teclado para enviar mensaje o archivos")
            print("----------- ----------------- -----------")
        else:
            # Mensaje de Error
            print("ERROR en info motivo:" + motivo)
            return salida



    def sendMessage(self,destino,mensaje):
        # Enviar mensaje con este robot
        # El tiempo minimo de ejecucion es de 40 segundos para las operaciones

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            # Reload la pagina web por si acaso se cerro la secion
            SSystem.setMouse_Position(self.Step1_ancho,self.Step1_alto,self.Step1_time)
            SSystem.Mouse_LeftClick()
            SSystem.sleep_time(3)
            SSystem.setMouse_Position(self.Step2_ancho,self.Step2_alto,self.Step2_time)
            SSystem.sleep_time(3)
            SSystem.Keyboard_press("f5")
            SSystem.sleep_time(25)

            # Seleccionar a la persona o grupo a enviar mensaje
            SSystem.setMouse_Position(self.Step3_ancho,self.Step3_alto,self.Step3_time)
            SSystem.Mouse_LeftClick()
            SSystem.sleep_time(3)
            SSystem.Keyboard_write(destino)
            SSystem.sleep_time(3)
            SSystem.Keyboard_press("enter")

            # Enviar el mensaje
            SSystem.setMouse_Position(self.Step4_ancho,self.Step4_alto,self.Step4_time)
            SSystem.Mouse_LeftClick()
            SSystem.sleep_time(3)
            SSystem.Keyboard_write(mensaje)
            SSystem.Keyboard_press("enter")
        else:
            # Mensaje de Error
            print("ERROR en sendMessage motivo:" + motivo)
            return salida






