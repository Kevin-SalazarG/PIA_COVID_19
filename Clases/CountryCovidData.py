import requests
from typing import Optional
from Utils.TextColor import TextColor
from Clases.ExcelHandler import ExcelHandler
from openpyxl.chart import Reference

class CountryCovidData:
    def __init__(self):
        self.data = {}

    def _fetch_country_data(self, country: str) -> Optional[dict]:
        url = f"https://disease.sh/v3/covid-19/countries/{country}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "message" in data:
                print(TextColor.RED + f"Error: {data['message']}" + TextColor.RESET)
                return None
            return data
        except requests.exceptions.RequestException as e:
            print(TextColor.RED + f"Error al obtener los datos del país '{country}': {e}" + TextColor.RESET)
            return None

    def get_country_data(self, country: str) -> Optional[dict]:
        if country.lower() not in self.data:
            self.data[country.lower()] = self._fetch_country_data(country)
        return self.data.get(country.lower())

    def compare_countries(self, country1: str, country2: str) -> None:
        data1 = self.get_country_data(country1)
        data2 = self.get_country_data(country2)
        if data1 and data2:
            print(TextColor.CYAN + f"\nComparando datos de COVID-19 entre {data1['country']} y {data2['country']}:" + TextColor.RESET)
            important_keys = ["cases", "deaths", "recovered", "tests"]
            for key in important_keys:
                value1 = data1.get(key, "Datos no disponibles")
                value2 = data2.get(key, "Datos no disponibles")
                print(f"{key.replace('_', ' ').title()}:")
                print(f"{data1['country']}: {value1}")
                print(f"{data2['country']}: {value2}")
                if key == "cases":
                    self._compare_population_ratio(data1, data2)
                print()
        else:
            print(TextColor.YELLOW + f"No se encontraron datos para el país '{country1}' o '{country2}'." + TextColor.RESET)

    def _compare_population_ratio(self, data1: dict, data2: dict) -> None:
        country1_population = data1.get("population")
        country2_population = data2.get("population")
        if country1_population and country2_population:
            ratio1 = data1["cases"] / country1_population
            ratio2 = data2["cases"] / country2_population
            print(f"{data1['country']} tiene {ratio1:.5f} casos por persona.")
            print(f"{data2['country']} tiene {ratio2:.5f} casos por persona.")
        else:
            print(TextColor.YELLOW + "No se pudieron obtener los datos de población para comparar la tasa de casos por persona." + TextColor.RESET)

    def save_comparison_to_excel(self, filename: str, country1: str, country2: str) -> None:
        data1 = self.get_country_data(country1)
        data2 = self.get_country_data(country2)
        if not data1 or not data2:
            print(TextColor.RED + f"No se pudieron obtener datos para uno de los países: {country1}, {country2}" + TextColor.RESET)
            return

        excel_handler = ExcelHandler(filename)
        excel_handler.create_sheet(f"Comparación {country1} vs {country2}")

        headers = ["Dato", country1, country2]
        excel_handler.add_headers(headers)

        important_keys = ["cases", "deaths", "recovered", "active", "tests", "population"]
        for key in important_keys:
            value1 = data1.get(key, "Datos no disponibles")
            value2 = data2.get(key, "Datos no disponibles")
            excel_handler.add_row([key.replace('_', ' ').title(), value1, value2])

        country1_population = data1.get("population")
        country2_population = data2.get("population")
        if country1_population and country2_population:
            ratio1 = data1["cases"] / country1_population
            ratio2 = data2["cases"] / country2_population
            excel_handler.add_row(["Casos por persona", f"{ratio1:.5f}", f"{ratio2:.5f}"])
        else:
            excel_handler.add_row(["Casos por persona", "Datos no disponibles", "Datos no disponibles"])

        excel_handler.adjust_column_widths()

        data_range = Reference(excel_handler.ws, min_col=2, min_row=1, max_col=3, max_row=len(important_keys) + 1)
        category_range = Reference(excel_handler.ws, min_col=1, min_row=2, max_row=len(important_keys) + 1)
        excel_handler.create_bar_chart("Comparación de datos de COVID-19", "Datos", "Valores", data_range, category_range, "E5")

        excel_handler.save()

if __name__ == "__main__":
    covid_data = CountryCovidData()
    covid_
