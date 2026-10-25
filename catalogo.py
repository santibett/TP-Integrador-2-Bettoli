import json
from satelite import El_Satelite
from funciones_base import obtener_posicion

def leer_json(dato):
    with open(dato, "r") as archivo:
        datos = json.load(archivo)
    return (datos)
def crear_catalogo(datos):
    #recibe la lista de diccionarios del JSON y devuelve una lista de objetos satelites
    catalogo = []
    for registro in datos:
        nombre = registro["OBJECT_NAME"]
        numero_catalogo = registro["NORAD_CAT_ID"]
        latitud, longitud, altitud = obtener_posicion(registro)
        try:
            satelite = El_Satelite(nombre, numero_catalogo, latitud, longitud, altitud) #crea las variables y funciones del satelite
            catalogo.append(satelite) # catalogo guarda todas las variables y funciones de la clase para cada satelite
        except ValueError:
            continue
        #uso try except para que si encuentra algun error como por ejemplo
        #que la altitud es menor a 100, simplemente ignore al satelite y siga con los otros
    return catalogo
def resumir_satelites(catalogo):
    resumen = {}
    for i in catalogo:
        orbita = i.tipo_orbita()
        if orbita not in resumen:
            resumen[orbita] = {
                "cantidad": 0,
                "altitudes": []}
        resumen[orbita]["cantidad"] += 1
        resumen[orbita]["altitudes"].append(i.altitud)
    resultado = {}
    for orbita, valores in resumen.items():
        altitudes = valores["altitudes"]
        resultado[orbita] = {
            "cantidad": valores["cantidad"],
            "minimo": min(altitudes),
            "maximo": max(altitudes),
            "promedio": round(sum(altitudes) / len(altitudes), 2)
        }
    return resultado
def satelites_en_zona(catalogo, long_min, lat_min, long_max, lat_max):
    sat_en_zona = []
    for i in catalogo:
        if i.en_zona_sat(long_min, lat_min, long_max, lat_max):
            sat_en_zona.append(i)
    return sat_en_zona