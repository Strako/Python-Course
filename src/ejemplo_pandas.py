import pandas as pd

# Crear un diccionario con datos
datos = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David','Jose'],
    'Edad': [28, 24, 22, 31, 34],
    'Ciudad': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Chicago']
}

# Crear un DataFrame a partir del diccionario
dataframe = pd.DataFrame(datos)

# Mostrar el DataFrame
print(dataframe)


# Filtrar personas mayores de 25 años
mayores_25 = dataframe[dataframe['Edad'] > 25]
print("\nPersonas mayores de 25 años:")
print(mayores_25)

# Calcular la media de las edades
media_edades = dataframe['Edad'].mean()
print("\nMedia de edades:", media_edades)

# Ordenar el DataFrame por edad en orden descendente
dataframe_ordenado = dataframe.sort_values(by='Edad', ascending=False)
print("\nDataFrame ordenado por edad:")
print(dataframe_ordenado)

# Agrupar por ciudad y calcular la media de edades en cada ciudad
grupo_ciudad = dataframe.groupby('Ciudad')['Edad'].mean()
print("\nMedia de edades por ciudad:")
print(grupo_ciudad)