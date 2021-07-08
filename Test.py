import Data_Types.Strings as SStrings
import Data_Types.Vector as SVector
import Files.Text as Shesha_Text
import VisionArtificial.Images_Algoritms as VA
import System.Systems_Scripts as Sys
import Data_Types.Numbers as SNumbers
import Data_Types.Experiment as SExp
import Data_Types.Time as STime



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
vector.addRigth("100")
vector.addRigth("200")
vector.addRigth("1")

timeA = "1:10:20:1000"
timeB = "2:20:11:12"

valor = 20000

print(STime.calculeTime_FormatxMedida(timeA,"-",55,"hh"))

#print(STime.calculeTime("1:20:10:100","+","0:10:5:150"))

#print(STime.setTime(timeA,"5","ss"))


