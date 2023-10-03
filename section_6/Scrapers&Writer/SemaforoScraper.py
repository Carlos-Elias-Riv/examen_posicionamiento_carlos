import selenium
import pandas as pd

class SemaforoScraper():
    """
    Una clase para hacer webscraping de la pagina oficial del semaforo por Estado "https://coronavirus.gob.mx/semaforo/"

    Metodos
    -------
    datosSemaforo(website):
        Regresa un dataframe con los datos, por Estado, de la fecha y su respectivo semaforo
    
    """

    def __init__(self, driver_path) -> None: 
        """
        Parametros
        ----------
        driver_path: 
            path de donde esta el chromedriver, accesible para hacer el webscraping
        """

        pass

    def datosSemaforo(self, website="https://coronavirus.gob.mx/semaforo/") -> pd.DataFrame: 
        """ Regresa un dataframe con los datos de los Estados, fecha y color de semaforo

        El dataframe regresado contiene el nombre del estado la 
        fecha del día anterior y que color de semaforo tenian
        """

        return pd.DataFrame()