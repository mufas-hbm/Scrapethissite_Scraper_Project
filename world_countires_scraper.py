import requests
from bs4 import BeautifulSoup
import pandas as pd


class CountriesScraper():
    def __init__(self):
        self.url= "https://www.scrapethissite.com/pages/simple/"
        self.countries_list = []
    
    def get_countries_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        countries = soup.find_all('div', class_='col-md-4 country')
        for country in countries:
            country_data = {
                "name": self.get_country_name(country),
                "capital":self.get_country_capital(country),
                "population":self.get_country_population(country),
                "area":self.get_country_area(country)
            }
            self.countries_list.append(country_data) # add data to list
            """print(f'Country name: {self.get_country_name(country)}')
            print(f'    Capital: {self.get_country_capital(country)}')
            print(f'    Population: {self.get_country_population(country)}')
            print(f'    Area: {self.get_country_area(country)}')"""

    def get_country_name(self, country):
        country_name = country.find('h3', class_='country-name').text.strip()
        return country_name
    
    def get_country_capital(self, country):
        country_capital = country.find('span', class_='country-capital').text.strip()
        return country_capital
    
    def get_country_population(self, country):
        country_population = int(country.find('span', class_='country-population').text.strip())
        return country_population
    
    def get_country_area(self, country):
        country_area = float(country.find('span', class_='country-area').text.strip())
        return country_area

    def save_to_csv(self, filename = "countries_data.csv"):
        if not self.countries_list:
            print("no data to save")
            return None
        df = pd.DataFrame(self.countries_list)
        df.to_csv(filename, index=False, sep=',')
        print(f"data saved to {filename}")



scraper = CountriesScraper() 
scraper.get_countries_data()
scraper.save_to_csv()