# Scripts para el manejo del Sistema Operativo
# Control de Mouse, teclado, etc
from ctypes import py_object

import pyautogui



def setMouse_Position(ancho,alto,time):
    # Esto posiciona el mouse en un lugar de la pantalla
    # alto y ancho indican las cooredenadas hasta n-1
    # time indica el tiempo que debe tomar para llegar a ese punto indicado

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

    # ---------------- Proceso  ---------------
    if condiciones == True:
        pyautogui.click()
    else:
        # Mensaje de Error
        print("ERROR en numOfContains motivo:" + motivo)
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






