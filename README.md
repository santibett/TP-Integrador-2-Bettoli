# TP-Integrador-2-Bettoli
Estudiante: Santiago Bettoli
# Resumen
En esta etapa se creó la clase Satelite, en la cual se organiza el nombre, catalogo, latitud, longitud y altitud. Se validan los datos, se clasifica cada satelite en un tipo de orbita, y el texto final de cada saltelite es:
```py
ISS (ZARYA) | 25544 | LEO | 419.7 km
```
En catalogo se lee el json recibido por terminal, y se crea un catalogo que contiene lo que pide la clase satelite, (nombre, catalogo, latitud, longitud y altitud). Ahi tambien se arma el resumen y los satelites en zona, para utilizarlo en consultar_satelites.py.
Ahi se ve lo que piden por terminal, tomando el json con los satelites, y la consulta que puede ser resumen o zona con sus respectivas coordenadas.
Luego utilicé pytest y pytest-cov para validar la logica del programa, manejar excepciones y evaluar casos limites.
## REQUISITOS
Python 3.x instalado
```bash
pip install -r requirements.txt
```
ejecutando esto en la terminal se instala skyfield==1.55, pytest y pytest-cov

## Instrucciones de Ejecución
El script `consultar_satelites.py` se ejecuta desde la consola pasando la ruta del .json y su consulta, que puede ser resumen o zona y sus 4 coordenadas

Resumen de satelites en el JSON:
```bash
python consultar_satelites.py datos/satelites.json resumen    
```          

Satelites en la zona indicada por zona long_minima, lat_minima, long_maxima, lat_maxima.
```bash
python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13
```
## Pruebas
Para verificar el funcionamiento del programa, se escribe lo siguiente en terminal
```bash
pytest
```
Para verificar el porcentaje
```bash
pytest --cov=. --cov-report=html 
```