def saludar (func):
    print("Esto se imprime antes")
    func()

def hola():
    print("¡Hola!")

saludar(hola)
