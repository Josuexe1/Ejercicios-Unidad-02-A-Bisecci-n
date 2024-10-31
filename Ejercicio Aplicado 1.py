import numpy as np

# Parámetros dados
L = 10  # cm
r = 1   # cm
V = 12.4  # cm^3

# Definimos la función f(h)
def funcion(h):
    return L * (0.5 * np.pi * r**2 - r**2 * np.arcsin(h / r) - h * np.sqrt(r**2 - h**2)) - V

# Método de bisección
def biseccion(funcion, a, b, tolerancia=0.01):
    while abs(b - a) > tolerancia:
        punto_medio = (a + b) / 2
        if funcion(punto_medio) == 0:
            return punto_medio
        elif funcion(a) * funcion(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
    return (a + b) / 2

# Intervalo y tolerancia
a, b = 0, r
tolerancia = 0.01
h = biseccion(funcion, a, b, tolerancia)

print(f"La profundidad del agua en el abrevadero es aproximadamente {h:.2f} cm")
