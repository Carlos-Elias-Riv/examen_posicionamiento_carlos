import selenium
import pandas as pd

class ConacytScraper():
    """
    Una clase para hacer webscraping de la pagina del concacyt "https://datos.covid-19.conacyt.mx/#DOView"

    Metodos 
    -------
    datosCovidPorEstado(pagina):
        Regresa un pandas dataframe que contiene los confirmados del dia anterior, 
        los confirmados de los 7 días antes y defunciones
    """

    def __init__(self, driver_path:str) -> None: 
        """
        Parametros
        ----------
        driver_path: 
            path de donde esta el chromedriver, accesible para hacer el webscraping
        
        """
        pass

    def datosCovidPorEstado(self, pagina="https://datos.covid-19.conacyt.mx/#DOView") -> pd.Dataframe:
        """ Regresa un dataframe con los confirmados de covid del dia anterior, 
        confirmados de los 7 días anteriores y las defunciones

        El dataframe regresado debe tener la fecha del día anterior, 
        el numero de muertes, el numero de contagiados y los confirmados de los 7 días anteriores

        
        """
        return pd.DataFrame()

    
