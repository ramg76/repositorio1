suma = lambda a,b : a+b
print(suma(3,4))

maximo = lambda a,b:a if a > b else b
print(maximo(10 , 20))


numeros= [1,2,3,4,5]
impares = list(filter(lambda x : x % 2 != 0 , numeros))
print(impares)

def funcion_potencia(n):
    return lambda x : x**n

cuadrado = funcion_potencia(2)
cubo = funcion_potencia(3)

print(cuadrado(5))
print(cubo(5))