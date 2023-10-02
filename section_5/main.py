from utils import ItamScrapper, RevisorITAM
import json

# para revisar la documentacion de las clases principales 
# help(RevisorITAM)
# help(ItamScrapper)


# para probar el scrapper se descomenta esta seccion

##########
# carreras = ["economía", "matemáticas aplicadas", "actuaría", "derecho", "relaciones internacionales"]

# si se desea hacer el scrapeo este driverpath debe ser cambiado por el path donde esté su chromedriver
# además se necesita instalar el chromdriver de la versión que se tenga de chrome que se puede encontrar en el siguiente link: 
# https://chromedriver.chromium.org/downloads
# scrapper = ItamScrapper(driverpath="/Users/cerivera/Documents/examen_driver/chromedriver")
# scrapper.obtenerDatosItamDeCarreras(carreras)
##########


# esta seccion es para las pruebas del resultado

# se lee el diccionario que contiene la información verídica, scrapeada, del itam y sus titulados
with open("datosItam.json", "r") as ofile: 
    data = json.load(ofile)

# inicializamos el revisor de las informacion
sheriff = RevisorITAM(data)
# se revisa la información de un csv dado
df = sheriff.veracidadInfo("fileprueba.csv")
# y regresamos la respuesta de dos maneras, imprimiendo el dataframe o exportándolo a un csv listo para regresarlo al cliente
print(df)
df.to_csv("deep_diverresp.csv", sep=",", encoding="utf-8", index=False)


