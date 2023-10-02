from selenium import webdriver
import pandas as pd
import json


class LimpiadorPalabras():
    """
    Una clase para limpiar strings a lo largo de todo el proceso 

    Metodos
    -------

    quitarAcentosyenie(cad):
        Regresa un string en minusculas, limpio de acentos y enies 
    """

    def __init__(self):
        """
        Inicializar la clase
        """

        pass

    def quitarAcentosyenie(self, cad: str):
        """ Regresa un string en minusculas sin acentos ni enies

        Parametros
        ----------
        cad: str
            Un string que contenga acentos o se suponga que tiene acentos o enies

        """

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
    """
    Una clase para scrappear los datos de titulacion de itamitas

    ...

    Metodos
    -------
    obtenerDiccionarioCarreras():
        Regresa un diccionario con las carreras disponibles en la página dada
    
    obtenerDatosItamdeCarreras(carreras)
        Regresa un diccionario con el nombre y el anio de titulacion de los alumnos de las carreas deseadas
    
    """

    def __init__(self, website="http://escolar1.rhon.itam.mx/titulacion/programas.asp", driverpath=""):
        """
        Parametros
        ----------

        website: str
            link de la pagina para scrapear
        
        driverpath: str
            path de donde esta el driver de chrome para hacer el scraping
        
        """

        self.website = website
        self.path = driverpath



    def obtenerDiccionarioCarreras(self) -> dict:
        """ Regresa un diccionario con su posicion en la pagina como llave y valor el nombre de la carrera

        """
        # se inicializa el diccionario de respuesta
        resp = {}
        # un limpiador para el nombre de la carrera
        cleaner = LimpiadorPalabras()
        # se inicializa el driver
        driver = webdriver.Chrome(self.path)
        driver.get(self.website)
        # iteramos sobre todos los elementos posibles de la tabla 
        # NOTA: si se llegan a abrir nuevas carreras este rango debería aumentar a 24
        for i in range(2, 23):
            # se encuentra la carrera y se mapea con su posicion en la pagina
            carr = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[{i}]/td/a')
            resp[i] = cleaner.quitarAcentosyenie(carr.text)
        driver.close()

        return resp

    def obtenerDatosItamDeCarreras(self, carreras: list)-> dict: 
        """ Regresa un diccionario de las carreras deseadas como llave y como valor dos listas 
        una con los nombres de los titulados y otra con los anios en que se titularon los alumnos. 
        Y escribe este diccionario en el workspace como un json 

        Parametros
        ----------
        carreras: list
            Una lista de strings con el nombre de las carreras que se quiere scrappear
        
        """
        # se limpia de caracteres raros la lista dada
        cleaner = LimpiadorPalabras()
        carreras = [cleaner.quitarAcentosyenie(carr) for carr in carreras]
        
        # se obtiene el diccionario de todas las carreras disponibles en la pagina del itam
        dictcarr = self.obtenerDiccionarioCarreras()

        # inicializar el driver para obtener los datos de los alumnos, nombre y anio
        driver = webdriver.Chrome(self.path)
        driver.get(self.website)

        # inicializar la respuesta
        resp = {}
        # un arreglo para iterar sobre la posicion de las carreras que nos interesan
        interes = []
        # para cada una de las carreras posibles obtenemos solamente aquellas que nos interesan
        for elem in dictcarr:
            # significa que es de las carreras de interes
            if dictcarr[elem] in carreras: 
                resp[dictcarr[elem]] = []
                interes.append(elem)

        # iteramos sobre la posicion de las carreras en la pagina del itam
        for i in interes:
            # entramos a la subpagina de las carreras
            carr = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[{i}]/td/a')
            carr.click()
            # los alumnos en la pagina empiezan numerados desde el 2
            alumno = 2
            # inicializamos los arreglos que iran como valor en el diccionario que se regresa
            respnames = []
            respanios = []
            hayalums = True
            # como no sabemos cuantos alumnos hay hacemos un while con un try except dentro, para cuando ya no haya
            while hayalums: 
                try:
                    # obtenemos el nombre del alumno
                    name = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{alumno}]/td[1]')
                    # si el nombre viene con acentos o enies se los quitamos
                    name = cleaner.quitarAcentosyenie(name.text)
                    # obtenemos el anio en que se tituló ese alumno
                    anio = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{alumno}]/td[2]')
                    anio = anio.text
                    alumno += 1
                    # notemos que la posicion del nombre corresponde a la misma posicion del anio
                    # esto implica que si se altera el orden de una lista se debe hacer la misma alteracion a la otra lista
                    respnames.append(name)
                    respanios.append(anio)
                    
                except: 
                    
                    hayalums = False
                    pass
            # mapeamos carrera: [[nombres alumnos], [anios alumnos]]
            resp[dictcarr[i]].append(respnames)
            resp[dictcarr[i]].append(respanios)
            
            # regresamos a la pagina anterior para poder avanzar a la siguiente carrera
            driver.back()
        


        driver.close()

        # para no tener que scrappear cada que se corra el codigo podemos escribir este diccionario en un json
        with open("datosItam.json", "w") as ofile:
            json.dump(resp, ofile)

        
        # regresa el diccionario con carrera: [[nombres alumnos], [anios alumnos]]
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