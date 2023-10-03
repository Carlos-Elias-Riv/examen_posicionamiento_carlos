import selenium
import pandas as pd

class OWDScraper():
    """
    Una clase para hacer webscraping de la pagina "https://ourworldindata.org/covid-vaccinations?country=MEX"
    
    Metodos
    -------
    datosVacunacionPorEstado(website):
        Regresa un dataframe con los datos de las vacunas aplicadas por Estado
    
    """

    def __init__(self, driver_path: str) -> None:
        """
        Parametros
        ----------
        driver_path: 
            path de donde esta el chromedriver, accesible para hacer el webscraping
        
        """

        pass

    def datosVacunacionPorEstado(self, website= "https://ourworldindata.org/covid-vaccinations?country=MEX") -> pd.DataFrame:
        """ Regresa un dataframe con los datos de vacunacion realizados por Estado

        El dataframe regresado debe contener la fecha, 
        el estado y el numero de vacunas aplicadas
        
        """

        return pd.DataFrame()