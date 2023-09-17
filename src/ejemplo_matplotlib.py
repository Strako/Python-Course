import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['Manzanas', 'Plátanos', 'Naranjas', 'Uvas']
valores = [30, 45, 25, 20]

# Crear el gráfico de barras
plt.bar(etiquetas, valores)

# Agregar etiquetas y título
plt.xlabel('Frutas')
plt.ylabel('Cantidad')
plt.title('Cantidad de Frutas')

# Mostrar el gráfico
plt.show()