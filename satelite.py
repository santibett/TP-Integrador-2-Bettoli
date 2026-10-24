class Satelite:
    def __init__(self, nombre, numero_catalogo, latitud, longitud, altitud):
        if -90 > latitud or latitud > 90: 
            raise ValueError("Latitud fuera de rango")
        if -180 > longitud or longitud > 180:
            raise ValueError("Longitud fuera de rango")
        if altitud < 100:
            raise ValueError("Altitud fuera de rango")
        if not nombre:
            raise ValueError("Nombre vacio")
        if type(numero_catalogo) is not int :
            raise ValueError("El catalogo no es un entero")
        self.nombre = nombre 
        self.numero_catalogo = numero_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud 
    def tipo_orbita(self):
        orbita = ""
        if self.altitud < 2000:
            orbita == "LEO"
        if self.altitud < 34000:
            orbita == "LEO"
        if self.altitud < 37000:
            orbita == "LEO"
        if self.altitud < 37000:
            orbita == "LEO"
        



        ISS (ZARYA) | 25544 | LEO | 419.7 km