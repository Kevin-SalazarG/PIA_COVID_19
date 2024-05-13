import re
from Clases.CountryCovidData import CountryCovidData
from Utils.TextColor import TextColor

def historial_covid():
    print(TextColor.GREEN + "Mostrando historial de COVID...")

def historial_paises(covid_api):
    while True:
        pais = input("Ingrese el nombre de un país o escriba 'regresar' para volver al menú principal: ")
        if pais.lower() == 'regresar':
            menu()
            break
        elif re.match(r'^[a-zA-Z\s]+$', pais):
            data = covid_api.get_country_data(pais.lower())
            if data:
                covid_api.show_country_data(pais.lower())
            else:
                print(TextColor.RED + f"No se encontraron datos para el país '{pais}'.")
        else:
            print(TextColor.RED + "Entrada inválida. Por favor, ingrese solo letras.")

def comparar_paises(covid_api):
    while True:
        pais1 = input("Ingrese el nombre del primer país o escriba 'regresar' para volver al menú principal: ")
        if pais1.lower() == 'regresar':
            menu()
            break
        elif re.match(r'^[a-zA-Z\s]+$', pais1):
            pais2 = input("Ingrese el nombre del segundo país: ")
            if re.match(r'^[a-zA-Z\s]+$', pais2):
                data1 = covid_api.get_country_data(pais1.lower())
                data2 = covid_api.get_country_data(pais2.lower())
                if data1 and data2:
                    print(TextColor.GREEN + "\nComparando datos de COVID-19 entre " + TextColor.WHITE + pais1 + TextColor.GREEN + " y " + TextColor.WHITE + pais2 + TextColor.RESET)
                    covid_api.compare_countries(pais1, pais2)
                else:
                    print(TextColor.RED + "No se encontraron datos para el país " + TextColor.WHITE + pais1 + TextColor.RED + " o " + TextColor.WHITE + pais2 + TextColor.RESET)
            else:
                print(TextColor.RED + "Entrada inválida para el segundo país. Por favor, ingrese solo letras.")
        else:
            print(TextColor.RED + "Entrada inválida para el primer país. Por favor, ingrese solo letras.")

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
            break
        elif opcion == "2":
            historial_paises(covid_api)
            break
        elif opcion == "3":
            comparar_paises(covid_api)
            break
        elif opcion == "4":
            print(TextColor.BOLD + TextColor.YELLOW + "Cerrando programa...")
            break
        else:
            print(TextColor.RED, "Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()