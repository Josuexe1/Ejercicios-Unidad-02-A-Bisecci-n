import numpy as np
import matplotlib.pyplot as plt

# Generamos los valores de x y añadimos el valor aleatorio
x = np.linspace(-2, 2, 500) + 0.0001234
y1 = x**2 - 1
y2 = np.exp(1 - x**2)

# Graficamos las funciones
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$y = x^2 - 1$', color='blue')
plt.plot(x, y2, label=r'$y = e^{1 - x^2}$', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de $y = x^2 - 1$ y $y = e^{1 - x^2}$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()


def funcion(x):
    return x**2 - 1 - np.exp(1 - x**2)
def biseccion(funcion, a, b, tolerancia=1e-3):
    while abs(b - a) > tolerancia:
        punto_medio = (a + b) / 2
        if funcion(punto_medio) == 0:
            return punto_medio
        elif funcion(a) * funcion(punto_medio) < 0:
            b = punto_medio
        else:
            a = punto_medio
    return (a + b) / 2
a, b = -2, 0
tolerancia = 1e-3
raiz = biseccion(funcion, a, b, tolerancia)

print(f"La raíz en el intervalo [{a}, {b}] es aproximadamente {raiz:.3f}")
