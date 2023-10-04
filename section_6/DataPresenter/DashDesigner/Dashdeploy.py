from dash import Dash
import pandas as pd
from SQLreader import SQLreader



class DashDeployer():
    """ Una clase para levantar la app de dash

    Metodos 
    -------

    solicitarDatos():
        Regresa un dataframe con los datos en general de la base de datos sql

    publicarDashboard():
        No regresa nada, pero publica y se encarga de levantar la dash app
    """

    def __init__(self) -> None:
        pass

    def solicitarDatos(self) -> pd.DataFrame: 
        """ Regresa un dataframe con los datos para el dashboard que deseamos presentar

        Esta funcion es la que usar el SQLreader para acceder a la base de datos aplicando
        queries y solicitando la información en general


        """

        return pd.DataFrame


    def publicarDashboard(self) -> None: 
        """ Levanta la dash app
        Esta funcion se encarga de llamar a la funcion solicitarDatos y con base en 
        este resultado levanta la dash app que verá el cliente

        """

        pass

# se levanta el dashboard correspondiente 

deploy = DashDeployer()

deploy.publicarDashboard()

    