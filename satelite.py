class El_Satelite:
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

        if self.altitud < 2000:
            return "LEO"
        if self.altitud < 34000:
            return "MEO"
        if self.altitud <= 37000:
            return "GEO"
        if self.altitud > 37000:
            return "HEO"
        
    def __str__(self): #_str_ hace que la clase "El_Satelite" tenga como predeterminado este texto cuando se quiera imprimir
        return f"{self.nombre} | {self.numero_catalogo} | {self.tipo_orbita()} | {self.altitud} km"
    
    def en_zona_sat(self, longitud_mínima, latitud_mínima, longitud_máxima, latitud_máxima):
        return (longitud_mínima <= self.longitud <= longitud_máxima) and (latitud_mínima <= self.latitud <= latitud_máxima)
    