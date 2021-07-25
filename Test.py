import Data_Types.Strings as SStrings
import Data_Types.Vector as SVector
import Files.Text as Shesha_Text
import VisionArtificial.Images_Algoritms as VA
import System.Systems_Scripts as Sys
import Data_Types.Numbers as SNumbers
import Data_Types.Experiment as SExp
import Data_Types.Time as STime
import System.Systems_Scripts as SSystem
import System.Email as SEmail
import pyautogui as pyautogui
import Robots.Whatsapp as WhatsBot



#print(Shesha_Strings.Like("Hola Mundo Hola","#Musndo#","#",True))


#archivo = Shesha_Text.Text("Prueba.txt")
#print(archivo.getLineLikeN("#Hola#Mundo#","#",3))
#print(archivo.posLineLikeN("#Hola#Mundasdo#","#",3))


#print(VA.getSize("C:\TODO\MiScreenShotActual.png"))
#VA.getSubImage("C:\TODO\MiScreenShotActual.png","C:\TODO\Recorte.png",300,325,380,755)
#print(VA.getText_Image("C:\TODO\Recorte.png"))

#Sys.setMouse_Position(10,10,1)
#Sys.Mouse_LeftClick()


#Sys.Keyboard_write("Hola Mundo 19258")


vector = SVector.Vector()

vector.addRigth("20")
vector.addLeft("a")
vector.addRigth("18")
vector.addRigth("19")
vector.addRigth("Hola")
vector.addRigth("A")
vector.addRigth("21")
vector.addRigth("$1,0345.52")
vector.addRigth("A")
vector.addRigth("200")
vector.addRigth("A")

timeA = "1:10:20:1000"
timeB = "2:20:11:12"

condicion=""
operadores=","


v = SVector.Vector()
v.addRigth(33135)
v.addRigth(3313)

#print(SStrings.numOfContains__Str_IN_Conjunt(condicion,operadores,","))
#SVector.detele_Element_ALL_byCondition(v,"<=",33000).print(",")


# bot = WhatsBot.Whatsapp_bot("C:\TODO\DESARROLLO TECNICO\D_Programacion\Python\Librerias\Shesha\Robots\Config_Whatsapp.txt")

# bot.sendMessage("Technotitlan","Apurate, el tiempo es ahora!")




#result = STime.calculeTime_FormatxFormat(timeA,"-",timeB)

#SVector.getSubVector_PosA_PosB(vector,0,12).print(",")

#print(STime.calculeTime("1:20:10:100","+","0:10:5:150"))

#print(STime.setTime(timeA,"5","ss"))


#print(SNumbers.porcentax_relax(200,0.2))



