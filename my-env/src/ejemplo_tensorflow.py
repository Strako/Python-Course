import tensorflow as tf
import numpy as np

# Generar datos de entrenamiento ficticios: alturas y edades
np.random.seed(0)
alturas = np.random.uniform(140, 200, size=100)
edades = np.random.uniform(15, 30, size=100)

# Crear un modelo simple
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='linear', input_shape=(1,))
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
modelo.fit(alturas, edades, epochs=1000, verbose=0)

# Hacer una predicción para una altura dada
altura_nueva = np.array([160], dtype=np.float32)
edad_predicha = modelo.predict(altura_nueva)
print("Edad predicha para una altura de 160 cm:", edad_predicha[0][0])

