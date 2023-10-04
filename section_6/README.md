## Respuesta sección 6

Para esta sección se propuso una arquitectura de componentes, en la propia arquitectura se indicaron los scripts que serían encargados
de orquestar la organización de la solución al problema [pdf de la arquitectura](https://github.com/Carlos-Elias-Riv/examen_posicionamiento_carlos/blob/main/section_6/arquitecturapropuesta.pdf). 
La solución a grandes rasgos propone scrapear los datos de las páginas dadas poner los datos crudos en un amazon s3 bucket. Luego limpiarlos
con otro script, luego este pasa los resultados a un script que se encarga de escribir estos datos a la base de datos sql que está en un 
AWS EC2 instance, de forma que queden acorde al modelo relacional propuesto [pdf modelo relacional](https://github.com/Carlos-Elias-Riv/examen_posicionamiento_carlos/blob/main/section_6/modelorelacional.pdf). 
Luego, dentro de la carpeta de datapresenter se encuentran los componentes encargados de presentar el dashboard y el reporte a los clientes finales. 
El reporte se siguió de acuerdo a las especificaciones pedidas y el dashboard se presenta con las siguientes gráficas [pdf dashboard](https://github.com/Carlos-Elias-Riv/examen_posicionamiento_carlos/blob/main/section_6/dashboardproject%20.pdf). 

# Supuestos

Hay varios supuestos importantes en esta solución al problema. La primera de ellas es que ourworldindata proporciona más información de la que sale en su página. 
En particular que contiene los datos de cuantas vacunas fueron administradas por estado en México. A su vez, creo que la página del conacyt ha cambiado, 
puesto que el semáforo por estado ya no se encuentra en esa página, es por esto que también se scrapea la página oficial del covid-19 y el semáforo. 
