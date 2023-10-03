from ConacytScraper import ConacytScraper
from OWDScraper import OWDScraper
from SemaforoScraper import SemaforoScraper
import boto3

# definimos los scrapers
conascraper = ConacytScraper()
owdscraper = OWDScraper()
semscraper = SemaforoScraper()

# obtenemos los datos de cada uno de ellos
conacytdata = conascraper.datosCovidPorEstado()
owddata = owdscraper.datosVacunacionPorEstado()
semdata = semscraper.datosSemaforo()

# pasar los datos a csv
conacytdata.to_csv("conacytdata.csv", sep=",")
owddata.to_csv("owddata.csv", sep=",")
semdata.to_csv("semdata.csv", sep=",")

# conectar con el bucket s3
s3 = boto3.resource()

# pasar los datos crudos al s3

s3.Bucket('cheez-willikers').upload_file(Filename='conacytdata.csv', Key='conacytdata.csv')
s3.Bucket('cheez-willikers').upload_file(Filename='owddata.csv', Key='owddata.csv')
s3.Bucket('cheez-willikers').upload_file(Filename='semdata.csv', Key='semdata.csv')
