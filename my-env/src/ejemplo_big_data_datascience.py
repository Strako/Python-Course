import random
import pandas as pd
import matplotlib.pyplot as plt

# Generar un conjunto de datos ficticio de ventas
datos_ventas = []
productos = ['Producto A', 'Producto B', 'Producto C']
regiones = ['Norte', 'Sur', 'Este', 'Oeste']

for _ in range(1000):
    producto = random.choice(productos)
    region = random.choice(regiones)
    cantidad_vendida = random.randint(1, 10)
    precio_unitario = random.uniform(10, 100)
    total_venta = cantidad_vendida * precio_unitario
    datos_ventas.append({'producto': producto, 'region': region, 'cantidad': cantidad_vendida, 'precio': precio_unitario, 'total': total_venta})

'''
DataFrame es una estructura de datos 
esencial en análisis y manipulación de 
datos que se utiliza ampliamente en 
ciencias de datos, análisis financiero,
procesamiento de información y otras áreas relacionadas
'''
# Crear un DataFrame a partir de los datos
df_ventas = pd.DataFrame(datos_ventas)

# Calcular el total de ventas por producto y por región utilizando diccionarios
ventas_por_producto = {}
ventas_por_region = {}

for _, venta in df_ventas.iterrows():
    producto = venta['producto']
    region = venta['region']
    total_venta = venta['total']

    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + total_venta
    ventas_por_region[region] = ventas_por_region.get(region, 0) + total_venta

# Visualizar los totales de ventas por producto
plt.bar(ventas_por_producto.keys(), ventas_por_producto.values())
plt.xlabel('Producto')
plt.ylabel('Total de Ventas')
plt.title('Ventas por Producto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualizar los totales de ventas por región
plt.bar(ventas_por_region.keys(), ventas_por_region.values())
plt.xlabel('Región')
plt.ylabel('Total de Ventas')
plt.title('Ventas por Región')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()