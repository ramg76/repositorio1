def obtener_saludo():
    def hola():
        print("Hola tu")
    return hola

saludo = obtener_saludo()
saludo()