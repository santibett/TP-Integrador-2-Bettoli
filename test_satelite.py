from satelite import El_Satelite
import pytest
satelite_prueba = El_Satelite("SAT", 2322, 0, 0, 1000)


def test_crear_satelite_valido():
    assert satelite_prueba.nombre == "SAT"
    assert satelite_prueba.numero_catalogo == 2322
    assert satelite_prueba.latitud == 0
    assert satelite_prueba.longitud == 0
    assert satelite_prueba.altitud == 1000
def test_crear_satelite_invalido():
    with pytest.raises(TypeError):
        El_Satelite("SAT") #falta de argumentos
def test_latitud_valida():
    satelite_prueba.latitud = -90
    assert satelite_prueba.latitud == -90
    satelite_prueba.latitud = 90
    assert satelite_prueba.latitud == 90
def test_latitud_invalida():
    with pytest.raises(ValueError):
        El_Satelite("SAT", 2322, -91, 0, 1000) #menor
    with pytest.raises(ValueError):
        El_Satelite("SAT", 2322, 91, 0, 1000) #mayor
def test_longitud_valida():
    satelite_prueba.longitud = -180
    assert satelite_prueba.longitud == -180
    satelite_prueba.longitud = 180
    assert satelite_prueba.longitud == 180
def test_longitud_invalida():
    with pytest.raises(ValueError):
        El_Satelite("SAT", 2322, 0, -181, 1000)
    with pytest.raises(ValueError):
        El_Satelite("SAT", 2322, 0, 181, 1000)
def test_nombre_invalido():
    with pytest.raises(ValueError):
        El_Satelite("", 2322, 0, 0, 1000)
def test_numero_catalogo_invalido():
    with pytest.raises(ValueError):
        El_Satelite("aaa", 2322.3, 0, 0, 1000) #tiene que ser entero
def test_tipo_orbita_LEO():
    satelite_prueba.altitud = 1000
    assert satelite_prueba.tipo_orbita() == "LEO"
    satelite_prueba.altitud = 1999
    assert satelite_prueba.tipo_orbita() == "LEO"
def test_tipo_orbita_MEO():
    satelite_prueba.altitud = 2000
    assert satelite_prueba.tipo_orbita() == "MEO"
    satelite_prueba.altitud = 33999
    assert satelite_prueba.tipo_orbita() == "MEO"
def test_tipo_orbita_GEO():
    satelite_prueba.altitud = 34000
    assert satelite_prueba.tipo_orbita() == "GEO"
    satelite_prueba.altitud = 37000
    assert satelite_prueba.tipo_orbita() == "GEO"
def test_tipo_orbita_HEO():
    satelite_prueba.altitud = 37001
    assert satelite_prueba.tipo_orbita() == "HEO"
    satelite_prueba.altitud = 90000
    assert satelite_prueba.tipo_orbita() == "HEO"
def test_tipo_orbita_invalida():
    satelite_prueba.altitud = "str"
    with pytest.raises(TypeError):
        satelite_prueba.tipo_orbita()