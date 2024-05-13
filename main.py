import re
from Clases.CountryCovidData import CountryCovidData

def historial_covid():
    print("Mostrando historial de COVID...")

def historial_paises():
    covid_api = CountryCovidData()
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
                print(f"No se encontraron datos para el país '{pais}'.")
        else:
            print("Entrada inválida. Por favor, ingrese solo letras.")

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1) Historial de COVID")
        print("2) Historial por países")
        print("3) Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            historial_covid()
            break
        elif opcion == "2":
            historial_paises()
            break
        elif opcion == "3":
            print("Cerrando programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()