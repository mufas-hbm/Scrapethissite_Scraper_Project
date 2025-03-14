import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd

class CountriesManager():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
    
    def handle_empty_results(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if result.empty:  # Check if the result is an empty DataFrame
                return "The search produced no results."
            return result
        return inner

    @handle_empty_results
    def filter_by_population(self, population: int):
        return self.data[self.data['population'] >= population]
    
    @handle_empty_results
    def filter_by_population_range(self, min_population: int, max_population: int):
        return self.data[(self.data['population'] >= min_population) & (self.data['population'] <= max_population)]
    
    @handle_empty_results
    def filter_by_area(self, area:float):
        return self.data[self.data['area'] >= area]
    
    @handle_empty_results
    def search_countries_by_letter(self, letter:str):
        return self.data[self.data['name'].str.startswith(letter.capitalize())]
    
    def sort_by_column(self,column_name: str, ascending=True):
        return self.data.sort_values(by=column_name, ascending= ascending)
    
    def add_density_column(self):
        self.data['density'] = self.data['population'] / self.data['area']
        return self.data

    @handle_empty_results
    def find_country(self, country_name: str):
        return self.data[self.data['name'].str.contains(country_name)]
    
    def save_to_csv(self, data,filename):
        data.to_csv(filename, index=False)

    def save_to_json(self, data, filename):
        data.to_json(filename)

    def plot_top_population(self, top_n=20):
        sorted_data = self.data.sort_values(by="population", ascending=True).tail(top_n)
        plt.figure(figsize=(12, 6))
        sns.barplot(data=sorted_data, x="population", y="name", hue='name', legend=False, orient='h')
        plt.title(f"Top {top_n} Countries by Population")
        plt.xlabel("Population")
        plt.ylabel("Country")
        plt.show()

countries_manager = CountriesManager("countries_data.csv")
#print(countries_manager.filter_by_population(500000))
countries_letter_a = countries_manager.search_countries_by_letter("AC")
print(countries_letter_a)
print(countries_manager.find_country("Alemania"))
print(countries_manager.filter_by_population_range(50000, 85000))
countries_manager.plot_top_population()