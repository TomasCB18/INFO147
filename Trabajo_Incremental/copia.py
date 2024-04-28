import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('defunciones_covid19_2020_2024.csv', sep=';')

#print(df)


# grafico de barra para mostrar defunciones totales por region
df_filtrado = df[df['NOMBRE_REGION'] != 'Ignorada']
defunciones_por_region = df_filtrado['NOMBRE_REGION'].value_counts()
defunciones_por_region = defunciones_por_region.sort_values(ascending=False)
defunciones_por_region.plot(kind='bar', color='skyblue')

plt.title('Defunciones por región')
plt.xlabel('Región')
plt.ylabel('Número de defunciones')


plt.xticks(rotation=45, ha='right') 
plt.tight_layout() 
plt.show()


# grafico de barras para contar el número de defunciones por año
defunciones_por_año = df['AÑO'].value_counts().sort_index()
defunciones_por_año.plot(kind='bar', color='skyblue')
plt.title('Defunciones por año')
plt.xlabel('Año')
plt.ylabel('Número de defunciones')
plt.show()



# grafico de línea para mostrar la distribución de defunciones por edad
defunciones_por_edad = df['EDAD_CANT'].value_counts().sort_index()
defunciones_por_edad.plot()
plt.title('Distribución de defunciones por edad')
plt.xlabel('Edad')
plt.ylabel('Número de defunciones')
plt.show()


#sacar media y desviacion estandar de todos estos datos, despues normalizar estos datos, 
# Contar el número de defunciones por año
defunciones_por_año = df['AÑO'].value_counts().sort_index()

# Calcular la moda, la media y la desviación estándar
moda = defunciones_por_año.mode()[0]
media = defunciones_por_año.mean()
desviacion_estandar = defunciones_por_año.std()

# Crear el gráfico de líneas
plt.plot(defunciones_por_año.index, defunciones_por_año.values, marker='o', color='skyblue', linestyle='-')

# Títulos y etiquetas
plt.title('Defunciones por año')
plt.xlabel('Año')
plt.ylabel('Número de defunciones')

# Mostrar la moda, la media y la desviación estándar en el gráfico
#plt.text(defunciones_por_año.index[-1], defunciones_por_año.values[-1], f'Moda: {moda}\nMedia: {media:.2f}\nDesviación estándar: {desviacion_estandar:.2f}', va='top', ha='right', color='black', bbox=dict(facecolor='white', alpha=0.5))

# Rotar etiquetas del eje x para mayor claridad
plt.xticks(rotation=45, ha='right')

# Ajustar diseño del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.grid(True)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Cargar los datos
df = pd.read_csv('defunciones_covid19_2020_2024.csv', sep=';')

# Mapear los códigos de lugar de defunción a nombres
place_mapping = {
    'Hospital o Clínica': 'Hospital',
    'Casa habitación': 'Casa habitación',
}
# La otra se mantiene como "Otro"

# Función para generar el gráfico interactivo
def plot_pie_chart(year):
    # Filtrar los datos para la región Metropolitana y el año seleccionado
    df_year = df[(df['NOMBRE_REGION'] == 'Metropolitana de Santiago') & (df['AÑO'] == year)]
    
    # Mapear los códigos a nombres de lugares de defunción
    df_year.loc[:, 'LUGAR_DEFUNCION'] = df_year['LUGAR_DEFUNCION'].map(place_mapping).fillna('Otro')

    # Contar los fallecidos por lugar de defunción
    place_of_death_counts = df_year['LUGAR_DEFUNCION'].value_counts()
    
    # Asegurarse de que haya una entrada para "Otro" incluso si no hay fallecimientos registrados en ese lugar
    place_of_death_counts['Otro'] = place_of_death_counts.get('Otro', 0)
    
    # Crear un gráfico de torta
    plt.figure(figsize=(8, 6))
    plt.pie(place_of_death_counts, labels=place_of_death_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Porcentaje de fallecidos por lugar de defunción en la Región Metropolitana en {year}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

# Crear el widget interactivo para seleccionar el año
year_selector = widgets.Dropdown(
    options=list(range(2020, 2025)),
    value=2020,
    description='Año:',
    disabled=False,
)

# Llamar a la función plot_pie_chart cuando se cambie el valor del widget
widgets.interactive(plot_pie_chart, year=year_selector)