from functools import partial
from pickletools import ArgumentDescriptor
import pyautogui
import Files.Text as Files
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



def takeScreenShot(pathName_Save):
    # Obtener un screenshot de la pantalla completa del PC en png

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(pathName_Save+".png")
    else:
        # Mensaje de Error
        print("ERROR en takeScreenShot motivo:" + motivo)
        return salida




def getSize(pathImage):
    # Obtener el tamaño de una imagen de alto y ancho

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    if Files.Text.existsFile(pathImage) != True:
        condiciones = False
        motivo = "Archivo: "+pathImage+" no existe!"

    # ---------------- Proceso  ---------------
    if condiciones == True:
        imagen = cv2.imread(pathImage)

        salida = imagen.shape
        return salida
    else:
        # Mensaje de Error
        print("ERROR en getSize motivo:" + motivo)
        return salida




def getSubImage(pathImageIN,pathImageOut,altoStart,altoFinish,anchoStart,anchoFinish):
    # Obtener una subimagen de una Imagen, un recorte

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    if Files.Text.existsFile(pathImageIN) != True:
        condiciones = False
        motivo = "Archivo: "+pathImageIN+" no existe!"


    if (altoStart<0) or (altoFinish > getSize(pathImageIN)[0]):
        condiciones = False
        motivo="Posicion alto no valida!"


    if (anchoStart<0) or (anchoFinish > getSize(pathImageIN)[1]):
        condiciones = False
        motivo="Posicion ancho no valida!"


    # ---------------- Proceso  ---------------
    if condiciones == True:
        #Leer la imagen
        imagen = cv2.imread(pathImageIN);

        #Recortar la imagen
        imagenOut = imagen[altoStart:altoFinish,anchoStart:anchoFinish]

        #Guardar la imagen
        cv2.imwrite(pathImageOut,imagenOut)
    else:
        # Mensaje de Error
        print("ERROR en getSubImage motivo:" + motivo)
        return salida



def getText_Image(pathImage):
    # Obtener el texto que tiene una imagen

    # ------- Variables Locales ----------
    motivo = "OK"
    condiciones = True
    salida = None

    # ----- Comprobar condiciones Inciales ------

    # ---------------- Proceso  ---------------
    if condiciones == True:
        img = cv2.imread(pathImage)
        salida = pytesseract.image_to_string(img)

        return salida
    else:
        # Mensaje de Error
        print("ERROR en getText_Image motivo:" + motivo)
        return salida



def getScreenSize():
        # Obtener el tamaño de la pantalla actual

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            return pyautogui.size()
        else:
            # Mensaje de Error
            print("ERROR en getScreenSize motivo:" + motivo)
            return salida



