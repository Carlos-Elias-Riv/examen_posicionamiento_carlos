from SQLreader import SQLreader
import sendgrid
import datetime
import pandas as pd

class EmailSender():
    """ Una clase que manda el reporte del día anterior, con base en que día es hoy

    calcularReporte()
        Regresa un dataframe con los datos deseados en el reporte

    mandarReporte(dest)
        No regresa nada, pero manda el reporte al destinatario dado

    """

    def __init__(self) -> None:
        """ Inicialización de la clase, con el valor del día que sea hoy

        """

        self.dia = datetime.date()
        pass

    def calcularReporte(self) -> pd.DataFrame:
        """ Regresa un dataframe de la siguiente manera: 

        {estado: values, contagios: values, semaforo: values, indicador: values}

        La idea es que esta funcion llame al sqlreader para pedir los queries 
        correspondientes para generar el anterior dataframe
        """

        pass

    def mandarReporte(self, dest: str)-> None:
        """ No regresa nada, pero manda el correo con el reporte solicitado
        al destinatario dest

        Haciendo uso de la libreria sendgrid y llamando a calcularReporte()
        
        """

        pass
# se manda el reporte
sender = EmailSender()
sender.mandarReporte("correejemplo@gmail.com")