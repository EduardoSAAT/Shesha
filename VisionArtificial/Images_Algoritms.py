import pyautogui


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