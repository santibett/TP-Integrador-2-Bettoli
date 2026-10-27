import sys
from catalogo import leer_json,crear_catalogo,resumir_satelites,satelites_en_zona
def main():
    if len(sys.argv) < 3:
        print("Faltan argumentos")
        print("Deberia ingresar algo como:")
        print("python consultar_satelites.py datos/satelites.json resumen")
        print("python consultar_satelites.py datos/satelites.json zona lon_min lat_min lon_max lat_max")
        exit()
    
    ruta_json = sys.argv[1]
    consulta = sys.argv[2]
    datos = leer_json(ruta_json)
    catalogo = crear_catalogo(datos)
    if consulta == "resumen":
        resumen = resumir_satelites(catalogo)
        print(f"Resumen sobre satelites de tu archivo:")
        print("---"*20) 
        for orbita, info in resumen.items():
            print(f"Orbita: {orbita}")
            print(f"Cantidad de satelites: {info["cantidad"]}")
            print(f"Maximo de altitud: {info["maximo"]} km")
            print(f"Minimo de altitud: {info["minimo"]} km")
            print(f"Promedio de altitud: {info["promedio"]} km")
            print("---"*20) 
            
    if consulta == "zona":
        longitud_min = float(sys.argv[3])
        latitud_min = float(sys.argv[4])
        longitud_max = float(sys.argv[5])
        latitud_max = float(sys.argv[6])
        en_zona = satelites_en_zona(catalogo, longitud_min, latitud_min, longitud_max, latitud_max)
        print("Satelites que están dentro de la zona:")
        print(f"Latitud ({latitud_min} ; {latitud_max})")
        print(f"Longitud ({longitud_min} ; {longitud_max})")
        print(f"Cantidad: {len(en_zona)}")
        for i in en_zona:
            print(i.mostrar()) 
main()