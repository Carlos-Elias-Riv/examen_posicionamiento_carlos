from selenium import webdriver
import pandas as pd
import json


class LimpiadorPalabras():
    def __init__(self):
        pass

    def quitarAcentosyenie(self, cad: str):
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



class ItamScrapper():

    def __init__(self, website="http://escolar1.rhon.itam.mx/titulacion/programas.asp", driverpath=""):
        self.website = website
        self.path = driverpath



    def obtenerDiccionarioCarreras(self):
        resp = {}
        cleaner = LimpiadorPalabras()
        driver = webdriver.Chrome(self.path)
        driver.get(self.website)
        for i in range(2, 23):
            carr = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[{i}]/td/a')
            resp[i] = cleaner.quitarAcentosyenie(carr.text)
        driver.close()

        return resp

    def obtenerDatosItamDeCarreras(self, carreras: list): 
        cleaner = LimpiadorPalabras()
        carreras = [cleaner.quitarAcentosyenie(carr) for carr in carreras]
        
        
        dictcarr = self.obtenerDiccionarioCarreras()

        # economia, mates aplicadas, actuaria, derecho y relaciones internacionales
        driver = webdriver.Chrome(self.path)
        driver.get(self.website)

        resp = {}
        interes = []
        for elem in dictcarr:
            # significa que es de las carreras de interes
            if dictcarr[elem] in carreras: 
                resp[dictcarr[elem]] = []
                interes.append(elem)

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
                    name = cleaner.quitarAcentosyenie(name.text)
                    anio = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{alumno}]/td[2]')
                    anio = anio.text
                    alumno += 1
                    respnames.append(name)
                    respanios.append(anio)
                    
                except: 
                    
                    hayalums = False
                    pass
            resp[dictcarr[i]].append(respnames)
            resp[dictcarr[i]].append(respanios)
            

            driver.back()
        


        driver.close()
        with open("datosItam.json", "w") as ofile:
            json.dump(resp, ofile)

        

        return resp




class RevisorITAM():
    """
    Una clase para revisar las titulaciones de itamitas

    ...

    Metodos
    -------

    limpiarNombresCSV(namecsv): 
        Regresa un dataframe a partir del csv, con la columna "Nombre" limpia y sin acentos ni enies

    verificaciones(df):
        Regresa una lista (ordenada) con las respuestas por fila del dataframe dado por limpiarNombresCSV

    veracidadInfo(namecsv)
        Regresa un dataframe con la respuesta de deep_dive a cada uno de los renglones dado en el csv


    
    """

    def __init__(self, dict):
        """
        Parametros
        ----------
        dict: dictionary
            diccionario con los datos obtenidos del scraper
        """

        self.datos = dict
    
    def limpiarNombresCSV(self, namecsv):
        """ Regresa un dataframe limpio a partir de un csv

        Parametros
        ----------
        namecsv: str
            Se espera que el csv sea accesible a pandas.read_csv()
            Documentacion sobre pandas.read_csv(): https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

        
        """

        cleaner = LimpiadorPalabras()
        df = pd.read_csv(namecsv)
        df["Nombre"]=df["Nombre"].apply(lambda x: cleaner.quitarAcentosyenie(x))

        return df

    def verificaciones(self, df):
        """ Regresa una lista con las respuestas de deep_dive

        Parametros
        ----------

        df: pandas.Dataframe
            Este dataframe tiene que ser un dataframe que ya paso por limpiarNombresCSV() 
            o que este limpio
        
        """

        # sobre cuantos renglones vamos a iterar
        rows = df.shape[0]
        cleaner = LimpiadorPalabras()
        
        # inicializamos la columna de respuestas deep_dive
        resp = []

        # para cada row va a haber una respuesta
        for row in range(rows):
            name = df.iloc[row, 0]
            carr = df.iloc[row, 1]
            # quitamos caracteres raros de las carreras
            carr = cleaner.quitarAcentosyenie(carr)
            anio = str(df.iloc[row, 2])
            # checamos si el nombre de la persona esta en la carrera que dice
            if name in self.datos[carr][0]:
                # obtenemos la posicion que le corresponde
                anioindex = self.datos[carr][0].index(name)
                # verificamos que el año coincida a partir del índice que conseguimos arriba
                if anio in self.datos[carr][1][anioindex]:
                    resp.append("Información Válida")
                else: 
                    resp.append("Titulado; año incorrecto")

            else: 
                resp.append("No titulado")

        return resp

    def veracidadInfo(self, namecsv):
        """ Regresa un dataframe con la respuesta de deep_dive

        Parametros
        ----------
        namecsv: str
            El csv debe ser accesible a la funcion pandas.read_csv()
            Documentacion sobre pandas.read_csv(): https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
        
        """

        # limpiamos los nombres del csv
        df = self.limpiarNombresCSV(namecsv)
        # hacemos la nueva columna a partir de las verificaciones necesarias
        df["deep_dive_response"] = self.verificaciones(df)
        # regresamos el dataframe
        return df