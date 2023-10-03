import boto3
import pandas as pd

class DataCleaner():
    """
    Una clase para limpiar los datos que están en el s3

    conacytCleaner(filename):
        Regresa un dataframe con los datos limpios del conacyt

    owdCleaner(filename):
        Regresa un dataframe con los datos limpios de owd

    semCleaner(filename):
        Regresa un dataframe con los datos limpios del semaforo de cada estado

    dataObtainer(s3):
        Regresa una lista de dataframes limpios del conacyt, owd y semaforos

    sqlTablesCreator(dfs):
        Regresa los dataframes que van de acuerdo al modelo relacional de la BD
    """

    def __init__(self):
        pass

    def conacytCleaner(self, filename:str) -> pd.DataFrame:
        """ Regresa un dataframe limpio con los datos del conacyt de la siguiente manera
        {estado: values, contagios: values, defunciones: values, 7dias: values, fecha: values}

        Parametros
        ----------
            filename (str): nombre del csv con los datos crudos del conacyt
        """

        return pd.DataFrame

    def owdCleaner(self, filename: str) -> pd.DataFrame: 
        """ Regresa un dataframe limpio con los datos de our world in data 
        de la siguiente manera: 
        {estado: values, numvacunas: values, fecha: values}

        Parametros
        ----------
            filename (str): nombre del csv con los datos crudos de owd
        """


        return pd.DataFrame

    def semCleaner(self, filename: str) -> pd.DataFrame: 
        """ Regresa un dataframe limpio con los datos del semaforo por estado
        de la siguiente manera: 

        {estado: values, color_sem: values, fecha: values}

        Parametros
        ----------
            filename (str): nombre del csv con los datos crudos del semaforo
        """

        return pd.DataFrame

    def dataObtainer(self, s3: boto3.resource) -> list: 
        """ Regresa una lista de dataframes, listos para ser pasados
        a dataframes que iran en la base de datos (todavía no estan en el formato del modelo relacional)
        Itera sobre todos los objetos en el s3 y aplica su correspondiente cleaner

        Parametros
        ----------
            s3: un boto3.resource listo para iterar sobre los objetos guardados
            y aplicar un cleaner
        """


        return list

    def sqlTablesCreator(self, dfs: list)  -> list:
        """ Regresa una lista de dataframes, listos para ser insertados a la BD
        Los dataframes se tienen que ver asi: 

        Contagio: 
        {fecha: values, numero: values, nomestado: values}
        
        Defuncion: 
        {fecha: values, numero: values, nomestado: values}

        Semaforo: 
        {fecha: values, color: values, nomestado: values}

        Vacunacion: 
        {fecha: values, numero: values, nomestado: values}

        Estado: 
        {nomestado: values}

        """


        return list



