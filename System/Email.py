# Scripts para manejo de correos electronicos
import smtplib  # Libreria para el manejo de correos electronicos


# Metodos Generales







# Objeto Main y sus Metodos
class Mail():

    master_email=""
    master_pass=""


    def __init__(self,email,clave):
        self.master_email=email
        self.master_pass=clave

        # Comprobar que este email se puede usar
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(self.master_email,self.master_pass)
            server.quit()
        except Exception as ex:
            print("No se pudo abrir esta cuenta de GMAIL  motivo:",ex)




    def sendGmail(self, destino,subject,mail):
        # Enviar un correo a un destino usando el correo master

        # ------- Variables Locales ----------
        motivo = "OK"
        condiciones = True
        salida = None

        # ----- Comprobar condiciones Inciales ------

        # ---------------- Proceso  ---------------
        if condiciones == True:
            #Abrir una conexion de correo electronico
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.master_email, self.master_pass)

            #Crear el correo electronico con el formato de gmail
            mensaje = "From: {}\nTo: {}\nX-Priority: {}\nSubject: {}\n\n{}".format(self.master_email,destino,1,subject,mail)

            server.sendmail(self.master_email,destino,mensaje)

            #server.quit()
            server.close()
        else:
            # Mensaje de Error
            print("ERROR en sendmail motivo:" + motivo)
            return salida




