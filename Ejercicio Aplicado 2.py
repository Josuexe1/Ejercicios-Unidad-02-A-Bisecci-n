import numpy as np
g = 9.81  
s0 = 300  
m = 0.25  
k = 0.1   
tolerancia = 0.01  

def s(t):
    return s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - np.exp(-k * t / m))

def biseccion(funcion, a, b, tolerancia):
    while abs(b - a) > tolerancia:
        punto_medio = (a + b) / 2
        if funcion(punto_medio) == 0:
            return punto_medio
        elif funcion(a) * funcion(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
    return (a + b) / 2

a, b = 0, 100
tiempo_caida = biseccion(s, a, b, tolerancia)

print(f"El tiempo que tarda en golpear el piso es aproximadamente {tiempo_caida:.2f} segundos")
