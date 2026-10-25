from catalogo import leer_json,crear_catalogo,resumir_satelites,satelites_en_zona
import pytest
import json
archivo = [{"OBJECT_NAME": "CALSPHERE 1",
  "OBJECT_ID": "1964-063C",
  "EPOCH": "2026-10-14T14:21:25.466688",
  "MEAN_MOTION": 13.76730837,
  "ECCENTRICITY": 0.00243553,
  "INCLINATION": 90.2208,
  "RA_OF_ASC_NODE": 74.5342,
  "NORAD_CAT_ID": 900}]
with open ("datos/satelite_para_test.json", "w") as el_archivo:
    json.dump(archivo, el_archivo)
entrada = "datos/satelite_para_test.json"
salida = [{"OBJECT_NAME": "CALSPHERE 1",
  "OBJECT_ID": "1964-063C",
  "EPOCH": "2026-10-14T14:21:25.466688",
  "MEAN_MOTION": 13.76730837,
  "ECCENTRICITY": 0.00243553,
  "INCLINATION": 90.2208,
  "RA_OF_ASC_NODE": 74.5342,
  "NORAD_CAT_ID": 900}]
def test_leer_json_valido():
    assert leer_json(entrada) == salida
def test_leer_json_invalido():
    with pytest.raises(FileNotFoundError):
        leer_json("pedro.json")
#def test_crear_catalogo_valido():
    #assert crear_catalogo(salida) == es complicada la salida de esta porque pasa por la clase.

satelite_completo = [{
  "OBJECT_NAME": "CALSPHERE 1",
  "OBJECT_ID": "1964-063C",
  "EPOCH": "2026-10-14T14:21:25.466688",
  "MEAN_MOTION": 13.76730837,
  "ECCENTRICITY": 0.00243553,
  "INCLINATION": 90.2208,
  "RA_OF_ASC_NODE": 74.5342,
  "ARG_OF_PERICENTER": 291.4443,
  "MEAN_ANOMALY": 198.023,
  "EPHEMERIS_TYPE": 0,
  "CLASSIFICATION_TYPE": "U",
  "NORAD_CAT_ID": 900,
  "ELEMENT_SET_NO": 999,
  "REV_AT_EPOCH": 8785,
  "BSTAR": 0.00056429819,
  "MEAN_MOTION_DOT": 5.64e-06,
  "MEAN_MOTION_DDOT": 0
 }]
"""
def test_crear_catalogo_invalido():
    assert len(crear_catalogo(satelite_completo)) == 0
""" #La funcion obtener_posicion de funciones_bases.py me complicó validar el error
catalogo_prueba = crear_catalogo(satelite_completo)
salida_resumir = {"LEO": {
            "cantidad": 1,
            "minimo": 984.495,
            "maximo": 984.495,
            "promedio": 984.5
        }}
def test_resumir_satelites_valido():
    assert resumir_satelites(catalogo_prueba) == salida_resumir
def test_resumir_satelites_invalido():
    assert resumir_satelites([]) == {} #deberia dar un diccionario vacio si le paso una lista 
    with pytest.raises(AttributeError):
            resumir_satelites(["hola", "2", "30"])
    with pytest.raises(TypeError):
            resumir_satelites(2)
def test_satelites_en_zona_valido():
     resultado_prueba = satelites_en_zona(catalogo_prueba, -1000, -1000, 10000, 10000)
     assert resultado_prueba[0].nombre == "CALSPHERE 1"
     assert resultado_prueba[0].numero_catalogo == 900
     assert satelites_en_zona(catalogo_prueba, 0,0,0,0) == [] #ningun satelite cae en esa zona
def test_satelites_en_zona_invalido():
    with pytest.raises(TypeError):
        satelites_en_zona(0,0,0,0) 
    with pytest.raises(TypeError):
        satelites_en_zona("hola")
    