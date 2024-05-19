import re
import os
import requests
from Clases.CountryCovidData import CountryCovidData
from Utils.TextColor import TextColor

def historial_covid():
    nombre_archivo = "historial_covid.pdf"
    try:
        if os.path.exists(nombre_archivo):
            print(TextColor.ORANGE + "El archivo", TextColor.WHITE + nombre_archivo, TextColor.ORANGE + "ya existe.")
        else:
            respuesta = requests.get("https://www.scielo.org.mx/pdf/eq/v31n2/0187-893X-eq-31-02-3.pdf")
            if respuesta.status_code == 200:
                with open(nombre_archivo, 'wb') as archivo:
                    archivo.write(respuesta.content)
                print(TextColor.GREEN + "Documento descargado exitosamente:", TextColor.WHITE + nombre_archivo)
            else:
                print(TextColor.RED + "Error al descargar el documento:", TextColor.WHITE + nombre_archivo)
    except Exception as e:
        print(TextColor.RED + f'Ha ocurrido un error: {e}')

def historial_paises(covid_api):
    while True:
        pais1 = input("Ingrese el nombre del país o escriba 'regresar o r' para volver al menú principal: ")
        if pais1.lower() in ['regresar', 'r']:
            return
        if not re.match(r'^[a-zA-Z\s]+$', pais):
            print(TextColor.RED + "Entrada inválida. Por favor, ingrese solo letras." + TextColor.RESET)
            continue
        try:
            data = covid_api.get_country_data(pais.lower())
            if data:
                print(TextColor.GREEN + f"Información de COVID-19 para el país '{pais}':")
                print(f"{TextColor.YELLOW}País: {TextColor.WHITE}{data['country']}")
                print(f"{TextColor.YELLOW}Casos totales: {TextColor.WHITE}{data['cases']}")
                print(f"{TextColor.YELLOW}Muertes totales: {TextColor.WHITE}{data['deaths']}")
                print(f"{TextColor.YELLOW}Recuperados totales: {TextColor.WHITE}{data['recovered']}")
                print(f"{TextColor.YELLOW}Casos activos: {TextColor.WHITE}{data['active']}")
                print(f"{TextColor.YELLOW}Casos hoy: {TextColor.WHITE}{data['todayCases']}")
                print(f"{TextColor.YELLOW}Muertes hoy: {TextColor.WHITE}{data['todayDeaths']}")
                print(f"{TextColor.YELLOW}Recuperados hoy: {TextColor.WHITE}{data['todayRecovered']}")
                print(f"{TextColor.YELLOW}Casos por millón de personas: {TextColor.WHITE}{data['casesPerOneMillion']}")
                print(f"{TextColor.YELLOW}Muertes por millón de personas: {TextColor.WHITE}{data['deathsPerOneMillion']}")
                print(f"{TextColor.YELLOW}Tests realizados: {TextColor.WHITE}{data['tests']}")
                print(f"{TextColor.YELLOW}Tests por millón de personas: {TextColor.WHITE}{data['testsPerOneMillion']}")
                print(f"{TextColor.YELLOW}Población: {TextColor.WHITE}{data['population']}")
            else:
                print(TextColor.RED + f"No se encontraron datos para el país '{pais}'." + TextColor.RESET)
        except Exception as e:
            print(TextColor.RED + f"Error al obtener datos para el país '{pais}': {e}" + TextColor.RESET)


def comparar_paises(covid_api):
    while True:
        pais1 = input("Ingrese el nombre del primer país o escriba 'regresar o r' para volver al menú principal: ")
        if pais1.lower() in ['regresar', 'r']:
            return
        elif re.match(r'^[a-zA-Z\s]+$', pais1):
            pais2 = input("Ingrese el nombre del segundo país: ")
            if re.match(r'^[a-zA-Z\s]+$', pais2):
                data1 = covid_api.get_country_data(pais1.lower())
                data2 = covid_api.get_country_data(pais2.lower())
                if data1 and data2:
                    print(TextColor.GREEN + "\nComparando datos de COVID-19 entre " + TextColor.WHITE + pais1 + TextColor.GREEN + " y " + TextColor.WHITE + pais2 + TextColor.RESET)
                    covid_api.compare_countries(pais1, pais2)

                    save_option = input("¿Desea guardar la comparación en un archivo Excel? (s/n): ").strip().lower()
                    if save_option == 's':
                        while True:
                            filename = input("Ingrese el nombre del archivo: ").strip()
                            if filename and not filename.isspace():
                                filename += ".xlsx"
                                covid_api.save_comparison_to_excel(filename, pais1, pais2)
                                break
                            else:
                                print(TextColor.RED + "Nombre de archivo inválido. Por favor, ingrese un nombre válido." + TextColor.RESET)
                else:
                    print(TextColor.RED + "No se encontraron datos para el país " + TextColor.WHITE + pais1 + TextColor.RED + " o " + TextColor.WHITE + pais2 + TextColor.RESET)
            else:
                print(TextColor.RED + "Entrada inválida para el segundo país. Por favor, ingrese solo letras." + TextColor.RESET)
        else:
            print(TextColor.RED + "Entrada inválida para el primer país. Por favor, ingrese solo letras." + TextColor.RESET)

def menu():
    covid_api = CountryCovidData()
    while True:
        print(TextColor.BOLD, TextColor.GREEN, "\nSeleccione una opción:")
        print(TextColor.CYAN, "1)", TextColor.RESET, "Historial de COVID")
        print(TextColor.CYAN, "2)", TextColor.RESET, "Historial por países")
        print(TextColor.CYAN, "3)", TextColor.RESET, "Comparar datos entre países")
        print(TextColor.CYAN, "4)", TextColor.YELLOW, "Salir", TextColor.RESET)
        opcion = input(TextColor.ORANGE + "Opción: " + TextColor.RESET)
        if opcion == "1":
            historial_covid()
        elif opcion == "2":
            historial_paises(covid_api)
        elif opcion == "3":
            comparar_paises(covid_api)
        elif opcion == "4":
            print(TextColor.BOLD + TextColor.YELLOW + "Cerrando programa...")
            break
        else:
            print(TextColor.RED, "Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()