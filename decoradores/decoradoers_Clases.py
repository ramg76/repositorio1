def decorador_clase(cls):
    class ClaseDecorada(cls):
        def metodo_decorado(self):
            print("Estamos en el metodo decorado")
            return self.metodo_original()

    return ClaseDecorada


@decorador_clase
class Miclase:
    def metodo_original(self):
        print("Estamos en el metodo original")

mi_objeto = Miclase()
mi_objeto.metodo_decorado()