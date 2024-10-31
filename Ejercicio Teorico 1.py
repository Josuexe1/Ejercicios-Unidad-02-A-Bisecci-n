import numpy as np

def f(x):
    return x**3 - x - 1

def biseccion(funcion, a, b, tolerancia, max_iteraciones=100):
    iteracion = 0
    while abs(b - a) > tolerancia and iteracion < max_iteraciones:
        iteracion += 1
        punto_medio = (a + b) / 2
        if funcion(punto_medio) == 0:
            return punto_medio, iteracion
        elif funcion(a) * funcion(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
    return (a + b) / 2, iteracion
a, b = 1, 2
tolerancia = 1e-4
raiz, iteraciones = biseccion(f, a, b, tolerancia)
print(f"La raíz aproximada es {raiz:.4f}")
print(f"Número de iteraciones necesarias: {iteraciones}")
