import requests

class Apy:
    def __init__(self) -> None:
        pass
    
    def get_data(self, url):
         
         responses = requests.get(url)
         datos = responses.json()
         return datos["results"]
    
        

    def get_pelicula(self):
        peliculas = self.get_data("https://swapi.py4e.com/api/films")
        
        return peliculas

    def get_planetas(self):
        planetas = self.get_data("https://swapi.py4e.com/api/planets")
        
        return planetas
