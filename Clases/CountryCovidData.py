import requests
from typing import Optional

class CountryCovidData:
    def __init__(self):
        self.data = {}

    def get_country_data(self, country: str) -> Optional[dict]:
        url = f"https://disease.sh/v3/covid-19/countries/{country}"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            self.data[country] = response.json()
            return self.data[country]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los datos del país '{country}': {e}")
            return None

    def show_country_data(self, country: str) -> None:
        if country in self.data:
            data = self.data[country]
            print(f"Mostrando datos de COVID-19 para {data['country']}")
            for key, value in data.items():
                if key != 'country':
                    print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print(f"No se encontraron datos para el país '{country}'.")

if __name__ == "__main__":
    covid_data = CountryCovidData()