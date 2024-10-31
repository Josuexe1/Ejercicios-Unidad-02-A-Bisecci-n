def biseccion(funcion, a, b, tolerancia=1e-5):
    while abs(b - a) > tolerancia:
        punto_medio = (a + b) / 2
        if funcion(punto_medio) == 0:
            return punto_medio
        if funcion(a) * funcion(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
            
    return (a + b) / 2  

def evaluar_intervalos(funcion, intervalos, tolerancia=1e-5):
    resultados = []
    for a, b in intervalos:
        raiz_aproximada = biseccion(funcion, a, b, tolerancia)
        resultados.append((a, b, raiz_aproximada))
    return resultados

funcion = lambda x: x**3 - 7 * x**2 + 14 * x - 6
intervalos = [(0, 1), (1, 3.2), (3.2, 4)]
tolerancia = 1e-5
resultados = evaluar_intervalos(funcion, intervalos, tolerancia)
for a, b, raiz in resultados:
    print(f"La raíz en el intervalo [{a}, {b}] es aproximadamente {raiz:.5f}")
