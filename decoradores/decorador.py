"""def mi_decorador(func):
    def envoltura():
        print("Algo se hace antes de la funcion 1")
        func()
        print("algo se hace despues de la funcion 2")

    return envoltura

@mi_decorador
def saludar():
    print("¡Hola desde Python")

saludar()
"""
def decorador(func):
    def nueva_funcion():
        print("Funcionalidad adicional antes de llamar a la funcion original")
        func()
        print("Funcionalidad adicional despues de llamar a la funcion original")

    return nueva_funcion

@decorador
def funcion_decorada():
    print("Soy la funcion original")


funcion_decorada()


