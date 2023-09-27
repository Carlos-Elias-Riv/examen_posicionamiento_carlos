# Examen de admisión a deep_dive

El presente examen es para ingresar a **Deep Dive Data Science S.A.P.I. de C.V.** Como una empresa comprometida con la innovación tecnológica y social nos gustaría conocerte un poco más y para ello elaboramos este examen en donde no hay respuestas incorrectas ni límite de tiempo para resolverlo.

**Recuerda:** Puedes tomarte el tiempo necesario para resolverlo, argumenta y explica tus respuestas a tu manera. Lo que evaluaremos es tu capacidad para poder dar solución a lo que se te pregunta y tu capacidad de análisis.

El examen consta de 6 secciones:

- Análisis.
- Habilidades básicas de programación.
- Desarrollo de algoritmos.
- Análisis de datos.
- Arquitectura de software.
- Arquitectura de soluciones.

La primera sección es escrita y tiene como objetivo analizar tu capacidad para expresar ideas complejas de forma clara y consisa.

El resto de secciones requieren de programación, las puedes resolver en el lenguaje de programación de tu elección pero recomendamos que sea en python -dado que es el lenguaje que utilizamos internamente en deep_dive-.

Para realizar la entrega del examen debes de **crear un repositorio privado de github**
El repositorio debe tener la siguiente estructura:

```shell
.
├── README.md # El Examen sin contestar
├── requirements.txt
├── seccion_1
│   ├── README.md # Tus respuestas a la sección 1
└── seccion_2
    └── README.md # Explicación respuesta sección 2
    └── main.py # Código respuesta sección 2
...
```

Mucha suerte!

---

## Sección A) Análisis

###### Caso 1

En los últimos años, el gobierno mexicano ha intentado incorporar algoritmos, aprendizaje de máquina (_machine learning_) y las mejores prácticas en ciencia de datos dentro de su política digital. En la Ciudad de México, la Agencia Digital de Innovación Pública ha impulsado una serie de proyectos con el objetivo de utilizar la tecnología y los datos para mejores políticas públicas en la ciudad. En el siguiente [enlace](https://adip.cdmx.gob.mx/proyectos), puedes encontrar la lista de iniciativas y proyectos que se han llevado a cabo los últimos meses (sobretodo fijate en los proyectos del 2020).

**a)** ¿Cuáles proyectos crees que causarían un mayor impacto en la sociedad mexicana? ¿Por qué?

**b)** Además de las propuestas, ¿qué otro problema del gobierno consideras se debería atacar utilizando herramientas de aprendizaje de máquina y ciencia de datos? ¿Cómo diseñarías la solución y cómo medirías su impacto como propuesta para el gobierno actual (ya sea local o federal)?

---

###### Caso 2

El manejo de grandes cantidades de datos nos ha permitido diseñar mecanismos de predicción y aprendizaje a partir de experiencias pasadas para poder actuar conforme. No obstante, los resultados indican que el uso de inteligencia artificial y modelos de aprendizaje de máquina comúnmente incorporan sesgos humanos a los modelos, lo que podría estar perpetuando estereotipos y dinámicas sociales no deseables. ¿Qué casos consideras son los más representativos de dicho problema? Si tuvieras la oportunidad de generar políticas que contrarrestaran esto, ¿cuáles medidas tomarías, cómo las implementarías y qué resultados esperarías?

---

## Sección B) Habilidades básicas de programación

###### Encriptación y manejo de cadenas

El objetivo de esta sección es **evaluar tus habilidades básicas de programación**.

Todo mundo conoce contraseñas. Uno puede escoger contraseñas de poemas, canciones, películas, películas, etc. Pero estas frecuentemente pueden ser adivinadas por referencias culturales comunes. Puede hacer tu contraseñas mas sólidas de diferentes maneras, una de ellas es la siguiente.

Escoge un texto en letras mayúsculas que incluya o no dígitos o no caracteres numéricos.

1. Mueve cada letra por un determinado numero de veces pero la letra debe de seguir siendo una letra (circular shift) Ej. $A + 2 = C$, $Z+1 = A$
2. Reemplaza cada digito por su complemento a 9.
3. Mantén los caracteres no alfabéticos y que no son digitos
4. Haz letra minúscula cada letra en una posición impar y mayúscula cada letra en una posición par (the first character is in position 0),
5. Invierte todo el resultado.

**Ejemplo**:

Tu texto: "BORN IN 2015!", shift 1 y complemento a 9 -> "CPSO JO 7984!"

En paso 4: "CpSo jO 7984!"

En paso 5: "!4897 Oj oSpC"

---

## Sección C) Desarrollo de algoritmos

###### Recursión y combinatoria.

El objetivo de esta sección es **evaluar tu capacidad para plantear y resolver un problema** que requiere el uso de algorimos complejos.

¿Cómo podemos obtener anagramas a partir de secuencias de operaciones realizadas por una pila?

Por ejemplo, existen dos posibles secuencias de operaciones que nos permiten transformar TROT en TORT:

- `i i i i o o o o `
- `i o i i o o i o `

Donde `i` implica realizar la operación Push en la pila y `o` la operación Pop. El programa a realizar tiene como objetivo, dado un par de palabras, producir todas las posibles secuencias de operaciones que nos permitan transformar la primer palabra en la segunda.

(Hay un video que se llama muestra_pila.mp4 donde se explica)

**Proceso:**

Una pila es una estructura de datos que realiza las siguientes operaciones:

- **Push** — Insertar un elemento.
- **Pop** — Regresa y elimina el último elemento que fue insertado en la pila.

Usaremos el símbolo `i` (in) para la operación push y `o` (out) para pop para una pila inicialmente vacía de caracteres. Dada una palabra de Input, decimos que una secuencia de operaciones push y pop es válida si cada caracter de la palabra es, en algún momento, insertado y eliminado. Asimismo, nunca se intenta realizar la operación pop con la pila vacía, por ejemplo, si la palabra de input es FOO, entonces la secuencia:

- `i i o i o o` Es valida
- `i i o` No es válida (muy corta)
- `i i o o o i` Tampoco es válida (operación ilegal)

Las secuencias validas producen un nuevo arreglo de las letras en la palabra de input. Por ejemplo, con la palabra FOO y la secuencia `i i o i o o` producimos el anagrama ‘OOF’.

**Input**: El programa debe recibir una pareja de palabras, donde la primera es la palabra base y debe ser transformada a la segunda.

**Output**: El programa debe regresar una lista ordenada con todas las posibles secuencias de ‘i’ y ‘o’ que llevan de la primer palabra a la segunda.

**Input de muestra:**

```python
a) madam, adamm
b) bahama, bahama
c) eric, rice
d) aaaabbb, ababaab
```

**Output de muestra:**

```python
a. [ i i i i o o o i o o,
         i i i i o o o o i o,
         i i o i o i o i o o,
         i i o i o i o o i o ]

b. [ i o i i i o o i i o o o,
         i o i i i o o o i o i o,
         i o i o i o i i i o o o,
         i o i o i o i o i o i o ]

c. [ i i o i o i o o ]

d. [ i i i i o i o o i o o o i o,
         i i i o i i o o i o o o i o,
         i i o i i i o o i o o o i o,
         i o i i i i o o i o o o i o ]
```

---

## Sección D) Análisis de datos

El objetivo de esta sección es **evaluar tu capacidad para entender un conjunto de datos y utilizarlos para contar una historia fidedigna**.

El archivo `datos_admisiones.csv` contiene un conjunto de datos que muestra las estadísticas de admisiones a una universidad mexicana agregadas por sexo y facultad a la que la persona aplió.

¿Existe algún sesgo hacia algún genero en particular? ¿Por qué?

Redacta una breve respuesta a dichas preguntas, justifica tu respuesta con un conjunto de gráficas y estadísticas relevantes.

---

## Sección E) Arquitectura de software

El objetivo de esta sección es **evaluar tu capacidad para organizar software** en clases y módulos diseñados para que tu programa sea fácil de entender, mantener y cambiar. También nos interesa evaluar tu capacidad para documentar código y para escribir funciones compactas y eficientes.

Supongamos que el ITAM está preocupado porque de repente ha surgido una epidemia de “falsos itamitas”, personas que dicen que ya se titularon pero que todavía no lo han hecho. Magdalena Barba, la directora de servicios escolares, contacta a deep_dive para que desarrolle unas funciones diseñadas para evaluar si un itamita ya se tituló o no.

La única información con la que contamos es el sitio oficial del itam para enlistar a los titulados: http://escolar1.rhon.itam.mx/titulacion/programas.asp

Como puedes ver, en esa página puedes seleccionar distintas carreras y así obtener los nombres de todas las personas que se han titulado de esa carrera, así como el año en que lo hicieron. Por simplicidad, asume que solo nos interesa enfocarnos en las carreras de economía, matemáticas aplicadas, actuaría, derecho y relaciones internacionales (asume que las demás no existen).

Es evidente que este mini proyecto requiere que uses web scraping (si nunca lo has usado, revisa las librerías de _beautifulsoup_ y _requests_). Sin embargo, el reto principal está en que desarrolles el proyecto de forma organizada y eficiente. Imagina que después de que tú completes este proyecto tus jefes te enviarán a otro proyecto y que nuevos divers se encargarán de mantener y mejorar tu código. Nos interesa evaluar tu capacidad para diseñar código y no solo para implementarlo.

Dicho esto, asume que tenemos los siguientes requerimientos:

- Vamos a recibir un csv con tres columnas, el nombre, la carrera y el año de titulación. deep_dive tiene que entregar ese mismo csv con una columna adicional que indique si esa persona sí se tituló de esa carrera ese año (se muestra un ejemplo en la tabla de abajo).
- Si la persona sí se tituló de esa carrera pero se tituló en otro año, la columna debe decir “Titulado, año incorrecto”
- Si la persona no se tituló de esa carrera, la columna debe decir (“No titulado”). (Nota: No tienes que buscar en las demás carreras para ver si esa persona se tituló del ITAM, solo concéntrate en la que dice el csv)
- Si la persona sí se tituló de esa carrera en el año indicado, la columna debe decir “Información válida”.

> **TIP:** al hacer el web scraping, se sugiere eliminar acentos y poner todos los nombres en minúsculas para compararlos con el csv

Por ejemplo:

| Nombre                   | Carrera               | Año  | deep_dive_response       |
| ------------------------ | --------------------- | ---- | ------------------------ |
| Abadi Cherem Elias       | Economía              | 2011 | Información Válida       |
| Abad Lopez Carlos Adrian | Matemáticas Aplicadas | 2002 | Titulado; año incorrecto |
| Miguel Bosé              | Economía              | 1900 | No titulado              |

> **Nota:**
> 
> No te preocupes por los inputs, asume que los años están en el formato correcto y que los nombres de las carreras están escritos así: ‘Economía’, ‘Matemáticas Aplicadas’, ‘Actuaría’, ‘Derecho’ y ‘Relaciones Internacionales’.
> 
> Asume que los nombres en el csv vienen en minúsculas y sin acentos ni caracteres extraños.
> 
> Por lo pronto imagina que el output final es un dataframe.

###### **Notas y sugerencias acerca del diseño de tu código:**

- Asegúrate de crear clases y no tener solo funciones.
- **Sugerencia:** una clase puede estar encargada de extraer la información desde internet y otra de evaluar la veracidad de la información en el csv y de añadir la columna adicional.
- Crea un archivo, utils.py, en donde almacenes las constantes que no necesitamos ver en el código. (por ejemplo, matemáticas aplicadas tiene el parámetro ‘prog=000169’ y economía ‘prog=000038’ en el url de los titulados).
- ¿De qué manera puedes escribir tus funciones para que el código se reutilice lo más posible y evites tener código duplicado?
- Escribe funciones con nombres claros.
- Asegúrate de documentar tus funciones (revisa: https://realpython.com/documenting-python-code/, pero no te preocupes por todos los detalles, solo detalla qué hace cada función y cuáles son los parámetros de entrada y de salida. **No tienes que documentar todas tus funciones.** Si algunas son muy claras y sencillas, no tienes que hacer esto).

###### Entregable

En palabras de Manuel Aragonés, CEO de deep*dive, \_lo que necesitamos es una función de menos de 4 líneas que reciba el csv, realice las verificaciones necesarias y entregue un pandas dataframe con los resultados.*

(Esa función puede llamar a otras clases y funciones dentro de las 4 líneas!).

---

## Sección F) Arquitectura de soluciones

El objetivo de esta sección es **medir tu capacidad para evaluar un problema, plantear una solución y definir su arquitectura**. También nos interesa evaluar tu capacidad de entendimiento del problema, tu visión para plantear una solución y la manera de organizar dicha solución.

Con el motivo de monitorear la contigencia de COVID-19, un nuevo cliente ha solicitado la posibilidad de crear un sistema de reportes en tiempo real. Se busca recopilar las últimas noticias en cuanto a vacunaciones, contagios, muertes y semáforo por cada estado de la república. Para contagios, muertes y el semáforo se desea obtener la información de la página oficial de datos del conacyt: https://datos.covid-19.conacyt.mx. Para las vacunaciones los datos se obtendrán de Our World In Data: https://ourworldindata.org/covid-vaccinations?country=MEX. Estos datos se obtendrán a traves de webscrappping y los datos crudos se deben de guardar en una _bucket_ en Amazon S3.

Los datos limpios se deben de guardar en una base de datos de SQL y estos alimentaran un dashboard al cual el cliente tendrá acceso para revisar los datos históricos del COVID-19 en México. **(\*)**

El reporte se enviará diario por correo electrónico a las 9:00 am y este solo debe contener los datos del día anterior agrupados por estado, así como un indicador que mostrará si los contagios son superior o inferiores a la media móvil de los últimos 7 días en ese estado. El reporte debe lucir así:

| Vacunaciones     | Contagios | Muertes | Semáforo | Indicador |
| ---------------- | --------- | ------- | -------- | --------- |
| Ciudad de México | 1,256     | 12      | 🔴       | 🔼        |
| Chiapas          | 600       | 7       | 🟢       | 🔽        |

Dicho reporte se enviará a través de Sendgrid, un servicio que facilita el envió de emails y brinda la posibilidad de hacerlo a través de Python.

#### Entregable

**NOTA: en ningún momento se espera que programes nada para resolver el problema planteado. Solamente se desea evaluar tu capacidad de proponer una arquitectura para la solución del problema.**

1. El diagrama de flujo de la solución que propondrá. Se recomienda utilizar los siguientes símbolos para el diagrama.

![image](https://user-images.githubusercontent.com/65791808/169413733-bedabe15-2d69-453f-94df-d90b0271c82d.png)

2. Un árbol que defina la estructura del código a utilizar para el proyecto. Puedes definir la cantidad de scripts necesites, solo es importante indicar qué funciones se encontrarán en cada uno de ellos. El árbol debe lucir así:
   
   ```shell
   |---- folder1
   |        |---- script1.py
   |        |---- script2.py
   |---- folder2
   |        |---- script3.py
   |        |---- folder3
   |        |        |---- script4.py
   |        |---- script5.py
   |---- script6.py
   ```
   
   Para cada script se debe incluir una pequeña definición de las funciones que llevará dentro. Por ejemplo:
   
   ```python
   mail_functions.py:
   
   # IDEA 0
   class Mail()
      def send_mail(mail, recipient):
   ```
   
     def create_mail_content(subject, content):
   
         """
         Args:
             subject (str): bla
             content (str): bla
       
         returns
             str: a string with the content of the mail to be sent
         """
         raise NotImplementedError

```
3. Para la base de datos de SQL **(\*)** se pide que se diseñe el diagrama relacional de las tablas que almacenarán los datos señalando bien las llaves primarias y las llaves foráneas (en caso de contar con alguna).

4. Para el dashboard se pide brindar ejemplos de gráficas e insights que considere importante para el cliente. Los ejemplos pueden realizarse a mano o a computadora, lo relevante es explicar cual la motivación de la visualización ¿Qué pretendemos comunidar?

El nivel de detalle de las respuestas queda a tu consideración. No existen respuestas incorrectas.

---
```
