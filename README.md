# Proyecto de Análisis de Datos de COVID-19

Este proyecto permite realizar varias operaciones relacionadas con el análisis de datos de COVID-19 a nivel mundial y por país. Utiliza datos en tiempo real de la API [disease.sh](https://disease.sh/).

## Funcionalidades

1. **Historial de COVID-19**: Descarga el historial de COVID-19 en formato PDF desde [esta fuente](https://www.scielo.org.mx/pdf/eq/v31n2/0187-893X-eq-31-02-3.pdf).

2. **Historial por países**: Muestra información detallada sobre COVID-19 para un país específico.

3. **Comparación de datos entre países**: Permite comparar diferentes métricas de COVID-19 entre dos países y guardar los resultados en un archivo Excel.

## Instrucciones de Uso

1. Instala las dependencias del proyecto ejecutando `pip install -r requirements.txt`.

2. Ejecuta el script `main.py` para iniciar la aplicación.

3. Selecciona la opción correspondiente al análisis que deseas realizar:
    - **Opción 1**: Historial de COVID-19.
    - **Opción 2**: Historial por países.
        - Ingresa el nombre completo o la abreviatura del país deseado.
        - Para obtener la lista de abreviaturas de los países, consulta [este enlace](https://es.wikipedia.org/wiki/ISO_3166-1#ISO_3166-1_alpha-2).
    - **Opción 3**: Comparar datos entre países.
        - Ingresa el nombre completo o la abreviatura de los países deseados.
        - Para obtener la lista de abreviaturas de los países, consulta [este enlace](https://es.wikipedia.org/wiki/ISO_3166-1#ISO_3166-1_alpha-2).
    - **Opción 4**: Salir del programa.

4. Sigue las instrucciones que aparecen en pantalla para completar la operación seleccionada.

## Requisitos

- Python 3.x
- Conexión a Internet

## Notas

- Algunas operaciones pueden tardar en completarse dependiendo de la velocidad de tu conexión a Internet y la disponibilidad de los servidores de la API.

- Asegúrate de tener una conexión estable a Internet para obtener los datos más actualizados.

¡Disfruta explorando los datos de COVID-19 con esta aplicación!
