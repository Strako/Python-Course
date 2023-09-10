import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo: edad vs. altura (en centímetros)
edad = np.array([5, 8, 10, 14, 18])
altura = np.array([110, 130, 140, 160, 170])

# Crear un modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo a los datos de entrenamiento
edad = edad.reshape(-1, 1)  # Convertir a una matriz de una sola característica
model.fit(edad, altura)

# Predecir la altura para una edad dada
edad_nueva = 12
altura_predicha = model.predict([[edad_nueva]])

print(f"Para una edad de {edad_nueva} años, la altura predicha es {altura_predicha[0]:.2f} cm")

# Visualización de la predicción
plt.scatter(edad_nueva, altura_predicha[0], color='black')
# Visualización de los datos y la línea de regresión
plt.scatter(edad, altura, color='blue')
plt.plot(edad, model.predict(edad), color='red', linewidth=2)
plt.xlabel('Edad (años)')
plt.ylabel('Altura (cm)')
plt.title('Regresión Lineal: Edad vs. Altura')
plt.show()