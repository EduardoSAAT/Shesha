# Scripts para el manejo del Sistema Operativo
# Control de Mouse, teclado, etc
from ctypes import py_object
import time
import pyautogui
import os


def setMouse_Position(ancho,alto,time):
    # Esto posiciona el mouse en un lugar de la pantalla
    # alto y ancho indican las cooredenadas hasta n-1
    # time indica el tiempo que debe tomar para llegar a ese punto indicado en segs

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None
    screenSize = pyautogui.size()

    # ----- Comprobar condiciones Inciales ------

    if alto<0 or alto >= screenSize.height:
        condiciones=False
        motivo="Posicion en Alto invalida"

    if ancho<0 or ancho >= screenSize.width:
        condiciones=False
        motivo="Posicion en Ancho invalida"


    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.moveTo(ancho,alto,time)
    else:
        # Mensaje de Error
        print("ERROR en numOfContains motivo:" + motivo)
        return salida



def getMouse_Position():
    # Obtener la posicion actual del mouse

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        salida = pyautogui.position()
        return salida
    else:
        # Mensaje de Error
        print("ERROR en getMouse_Position motivo:" + motivo)
        return salida



def Mouse_LeftClick():
    # Dar un clic izquierdo rapido del mouse

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    posActual=getMouse_Position()
    if posActual[0]==0==posActual[1]:
        condiciones=False
        motivo="No se puede hacer click en la posicion 0,0"


    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.click()
    else:
        # Mensaje de Error
        print("ERROR en Mouse_LeftClick motivo:" + motivo)
        return salida




def Mouse_DragTo(ancho,alto,time):
    # Click Derecho para Arrastar desde la posicion actual hasta la posicion indicada en un tiempo especifico

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.dragTo(ancho,alto,time)
    else:
        # Mensaje de Error
        print("ERROR en Mouse_DragTo motivo:" + motivo)
        return salida



def Mouse_Scroll(numPixeles):
    # Mover la ruedita del mouse una cierta cantidad de pixeles hacia arriba o abajo

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.scroll(numPixeles)
    else:
        # Mensaje de Error
        print("ERROR en Mouse_Scroll motivo:" + motivo)
        return salida



def Keyboard_write(mensaje):
    # Escribir un texto por teclado

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.typewrite(mensaje)
    else:
        # Mensaje de Error
        print("ERROR en Keyboard_write motivo:" + motivo)
        return salida



def Keyboard_show_keyboardNames():
    # Mostrar los nombres de las teclas del teclado

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        print(pyautogui.KEYBOARD_KEYS)
    else:
        # Mensaje de Error
        print("ERROR en Keyboard_write motivo:" + motivo)
        return salida



def Keyboard_press(key):
    # Presionar una tecla del teclado, llamada por su nombre

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.press(key)
    else:
        # Mensaje de Error
        print("ERROR en Keyboard_press motivo:" + motivo)
        return salida



def Keyboard_pressDOWN(key):
    # Mantener presionada una tecla del teclado hasta indicarle su UP

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.keyDown(key)
    else:
        # Mensaje de Error
        print("ERROR en Keyboard_pressDOWN motivo:" + motivo)
        return salida


def Keyboard_pressUP(key):
    # Soltar una tecla que se tenia preionada

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.keyUp(key)
    else:
        # Mensaje de Error
        print("ERROR en Keyboard_pressUP motivo:" + motivo)
        return salida




def getActualPath():
    # Obtener la ruta actual de ejecucion

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        return os.path.abspath(os.getcwd())
    else:
        # Mensaje de Error
        print("ERROR en getActualPath motivo:" + motivo)
        return salida


def sleep_time(segs):
    # Detener el Sistema por un tiempo en segundos

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        time.sleep(segs)
    else:
        # Mensaje de Error
        print("ERROR en sleep_time motivo:" + motivo)
        return salida





def getNomenglature_for_ExecuteInstruccions():
    # Obtener la nomenglatura para usar el ejecutar de instrucciones

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        print("----------- Nomenglatura para usar ExecuteInstruccions -----------")
        print("Info: Sistema para ejecutar instrucciones de PC bien definidas")
        print("      Instrucciones secuenciales, sencillas, sin mucha logica ")
        print("                                                              ")
        print("Type()   Define el tipo de Objeto a Usar")
        print("           Mouse    - Indica ordenes de raton")
        print("           Keyboard - Indica ordenes de Teclado")
        print("           System   - Indica ordenes de Systema")
        print("")
        print("Action() Indica la accion, depende del tipo de objeto")
        print("  Instrucciones para objeto: MOUSE")
        print("     Action(mover)   - Indica mover el raton a un posicion")
        print("         mover[] - Permite indicar los parametros de la instruccion mover, desde esquina superior izq")
        print("                     alto()  Posicion EjeY      ")
        print("                     ancho() Posicion EjeX      ")
        print("                     time()  Tiempo para llegar a esa posicion en segs")
        print("         Ejemplo: Action(mover) mover[alto(100)ancho(200)time(2)]    ")
        print("     Action(Rclick)  - Indica dar click derecho en la posicion actual")
        print("     Action(Lclick)  - Indica dar click izquierdo en la posicion actual")
        print("     Action(LLclick) - Indica dar doble click izquierdo en la posicion actual")
        print("  Instrucciones para objeto: KEYBOARD")
        print("     Action(write)   - Indica escribir un texto")
        print("         write[] - Permite indicar los paramatetros para el write")
        print("                      text() - Texto a escribir  ")
        print("         Ejemplo: Action(write) write[text(mundo loco)]    ")
        print("")
        print("Repeat() Indica las veces que se debe repetir la Action(), si no se especifica solo se hace 1 vez")
        print("         ciclos[] - Permite indicar los parametros de ciclos de repeticion")
        print("                    num()  Numero de ciclos de repeticion")
        print("                    time() Tiempo entre cada repeticion en segs")
        print("   Ejemplo: Repeat(ciclos) ciclos[num(3)time(5)]")
        print("----------- ------------------------------------------ -----------")
    else:
        # Mensaje de Error
        print("ERROR en getNomenglature_for_ExecuteInstruccionsmotivo:" + motivo)
        return salida



def ExecuteInstruccions():
    # Obtener la ruta actual de ejecucion

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        return os.path.abspath(os.getcwd())
    else:
        # Mensaje de Error
        print("ERROR en getActualPath motivo:" + motivo)
        return salida



