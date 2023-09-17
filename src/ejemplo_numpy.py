import numpy as np

# Crear un arreglo unidimensional (vector) con NumPy
vector = np.array([1, 2, 3, 4, 5])
print("Vector:")
print(vector)

# Crear una matriz (arreglo bidimensional) con NumPy
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz:")
print(matriz)

# Operaciones básicas con arreglos
suma_vector = vector + 10
producto_matriz = matriz * 2
division_matriz = matriz / 3

print("\nSuma del vector con 10:")
print(suma_vector)
print("\nProducto de la matriz por 2:")
print(producto_matriz)
print("\nDivisión de la matriz por 3:")
print(division_matriz)

# Funciones matemáticas con NumPy
seno_vector = np.sin(vector)
exponencial_matriz = np.exp(matriz)

print("\nSeno del vector:")
print(seno_vector)
print("\nExponencial de la matriz:")
print(exponencial_matriz)