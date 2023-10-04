import psycopg2
import pandas as pd


class SQLreader():
    """ Una clase que lee los datos de la base de datos en EC2

    Metodos
    -------
    allDataSemaforo():
        Regresa todos los datos de la tabla Semaforo

    allDataVacunacion():
        Regresa todos los datos de la tabla Vacunacion

    allDataContagio():
        Regresa todos los datos de la tabla Contagio

    allDataDefuncion():
        Regresa todos los datos de la tabla Defuncion

    getQuery(query):
        Regresa la respuesta al query solicitado

    calculaMediaMovil():
        Regresa la media movil de los ultimos 7 días
    
    """

    def __init__(self) -> None: 
        """
        En la inicializacion se hace la conexión a la base de datos usando psycopg2
        
        """

        pass


    def allDataSemaforo(self) -> pd.DataFrame:
        """ Regresa todos los datos guardados en la tabla semaforo

        Esta funcion, usando la conexión de psycopg2, obtiene los datos guardados
        en la base de datos y los pasa a un pd.DataFrame
        
        """

        return pd.DataFrame

    
    def allDataVacunacion(self) -> pd.DataFrame:
        """ Regresa todos los datos guardados en la tabla vacunacion

        Esta funcion, usando la conexión de psycopg2, obtiene los datos guardados
        en la base de datos y los pasa a un pd.DataFrame
        
        """

        
        return pd.DataFrame

    def allDataContagio(self) -> pd.DataFrame:
        """ Regresa todos los datos guardados en la tabla contagio

        Esta funcion, usando la conexión de psycopg2, obtiene los datos guardados
        en la base de datos y los pasa a un pd.DataFrame
        
        """
        
        return pd.DataFrame

    def allDataDefuncion(self) -> pd.DataFrame:
        """ Regresa todos los datos guardados en la tabla defuncion

        Esta funcion, usando la conexión de psycopg2, obtiene los datos guardados
        en la base de datos y los pasa a un pd.DataFrame
        
        """
        
        return pd.DataFrame

    def getQuery(self, query) -> pd.DataFrame: 
        """ Regresa la respuesta de la base de datos al query solicitado

        Esta funcion, usando la conexión de psycopg2, obtiene la respuesta del query
        a la base de datos. El objetivo de esta funcion es que tanto el dashboard, 
        como el emailsender tengan la posibilidad de acceder a datos específicos, 
        solicitados para diferentes escenarios
        
        """

        return pd.DataFrame

    def calculaMediaMovil(self, query) -> float: 
        """Regresa el promedio movil de los ultimos 7 días para compararlo con el día de ayer

        Esta funcion debe hacer un query para obtener los datos de contagio de 
        los ultimos 7 días promediarlos y regresar ese valor
        
        """

        return 0.0



