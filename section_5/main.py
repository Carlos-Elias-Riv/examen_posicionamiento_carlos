from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from joblib import Parallel, delayed
import pandas as pd
import pickle
import json
website = "http://escolar1.rhon.itam.mx/titulacion/programas.asp"

def quitarAcentosyenie(cad):
    cad = cad.replace('á', 'a')
    cad = cad.replace('é', 'e')
    cad = cad.replace('í', 'i')
    cad = cad.replace('ó', 'o')
    cad = cad.replace('ú', 'u')
    cad = cad.replace('Á', 'A')
    cad = cad.replace('É', 'E')
    cad = cad.replace('Í', 'I')
    cad = cad.replace('Ó', 'O')
    cad = cad.replace('Ú', 'U')
    cad = cad.replace('Ñ', 'N')
    cad = cad.replace('ñ', 'n')

    return cad.lower()


def obtenerDatosItam():

    path = "/Users/cerivera/Documents/examen_driver/chromedriver"

    driver = webdriver.Chrome(path)
    driver.get(website)

    # economia, mates aplicadas, actuaria, derecho y relaciones internacionales
    predf = {15:[], 21: [], 2: [], 
            13: [], 22: []}
    interes = [15, 21, 2, 13, 22]
    for i in interes:
        carr = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[{i}]/td/a')
        carr.click()
        alumno = 2
        respnames = []
        respanios = []
        hayalums = True
        while hayalums: 
            try:
                name = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{alumno}]/td[1]')
                # si el nombre viene con acentos se los quitamos
                name = quitarAcentosyenie(name.text)
                anio = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{alumno}]/td[2]')
                anio = anio.text
                alumno += 1
                respnames.append(name)
                respanios.append(anio)
                print(name, anio)
            except: 
                
                hayalums = False
                pass

        predf[i].append(respnames)
        predf[i].append(respanios)

        driver.back()
    


    driver.close()

    ## este predf va a servir para checar si la informacion es correcta

    return predf

class RevisorITAM():
    def __init__(self, dict):
        self.datos = dict
    
    def limpiarNombresCSV(self, namecsv):
        df = pd.read_csv(namecsv)
        df["Nombre"]=df["Nombre"].apply(lambda x: quitarAcentosyenie(x))
        df["Nombre"] = df["Nombre"].apply(lambda x: x.lower())

        return df

    def veracidadInfo(self, namecsv):
        # recibimos el csv
        df = self.limpiarNombresCSV(namecsv)
        # recibimos las verificaciones
        verify = self.verificaciones(df)
        # hacemos la nueva columna
        df["deep_dive_response"] = verify
        # regresamos el dataframe
        return df
        
    

    def verificaciones(self, df):
        rows = df.shape[0]
        consultdict = {"Matemáticas Aplicadas": "21", "Actuaría": "2",
                        "Economía": "15", "Relaciones Internacionales": "22",
                        "Derecho": "13"}

        resp = []
        for row in range(rows):
            name = df.iloc[row, 0]
            carr = df.iloc[row, 1]
            anio = str(df.iloc[row, 2])
            # los nombres de la carrera
            if name in self.datos[consultdict[carr]][0]:
                anioindex = self.datos[consultdict[carr]][0].index(name)
                # los años de cada alumno
                if anio in self.datos[consultdict[carr]][1][anioindex]:
                    resp.append("Información Válida")
                else: 
                    resp.append("Titulado; año incorrecto")

            else: 
                resp.append("No titulado")

        return resp

# solo la primera vez
# datos = obtenerDatosItam()
# with open("datosItam.json", "w") as ofile:
#     json.dump(datos, ofile)

with open("datosItam.json", "r") as ofile: 
    data = json.load(ofile)


sheriff = RevisorITAM(data)
df = sheriff.veracidadInfo("fileprueba.csv")
print(df)
df.to_csv("deep_diverresp", sep=",", encoding="utf-8")