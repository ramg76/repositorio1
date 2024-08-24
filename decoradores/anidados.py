def decorador1(func):
    def funcion_interna():
        print("Decorador 1")
        func()
    return funcion_interna

def decorador2(func):
    def funcion_interna():
        print("Decorador 2")
        func()
    return funcion_interna


@decorador1
@decorador2

def mi_funcion():
    print("Funcion original")

mi_funcion()

