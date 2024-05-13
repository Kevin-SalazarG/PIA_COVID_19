import requests
from typing import Optional
from Utils.TextColor import TextColor

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

    def show_country_data(self, country: str) -> None:
        data = self.get_country_data(country)
        if data:
            print(TextColor.GREEN + f"Mostrando datos de COVID-19 para {data['country']}" + TextColor.RESET)
            for key, value in data.items():
                if key != 'country':
                    print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print(TextColor.YELLOW + f"No se encontraron datos para el país '{country}'." + TextColor.RESET)

    def get_country_population(self, country: str) -> Optional[int]:
        data = self.get_country_data(country)
        if data and "population" in data:
            return data["population"]
        else:
            print(TextColor.YELLOW + f"No se pudo encontrar la población para el país '{country}'." + TextColor.RESET)
            return None

    def compare_countries(self, country1: str, country2: str) -> None:
        data1 = self.get_country_data(country1)
        data2 = self.get_country_data(country2)
        if data1 and data2:
            print(TextColor.BLUE + f"\nComparando datos de COVID-19 entre {data1['country']} y {data2['country']}:" + TextColor.RESET)
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

if __name__ == "__main__":
    covid_data = CountryCovidData()
