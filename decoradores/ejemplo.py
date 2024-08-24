def decorador1(func):
    def envoltura():
        print("Decorador 1 antes")
        func()
        print("Decorador 1 después")
    return envoltura

def decorador2(func):
    def envoltura():
        print("Decorador 2 antes")
        func()
        print("Decorador 2 después")
    return envoltura

@decorador1
@decorador2
def mi_funcion():
    print("Función ejecutándose")

mi_funcion()

