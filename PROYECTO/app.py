from api import Apy
from center import Movie, Planeta


class App:
    def __init__(self) -> None:
        self.peliculas = []
        self.planetas = []
        self.dict_url_peliculas = {}
        
    def run(self):
        self.cargar_dato()
        self.mostrar_peliculas()
        self.mostrar_planetas()
        print(self.dict_url_peliculas)
    
    def cargar_dato(self):
        self.cargar_peliculas()
        self.cargar_planetas()

    def cargar_peliculas(self):
        api = Apy()
        x = 1
        peliculas_apy = api.get_pelicula()
        for pelicula in peliculas_apy:
            
            capitulo = Movie.from_dict(pelicula)
            self.peliculas.append(capitulo)
            self.dict_url_peliculas[f"https://swapi.py4e.com/api/films/{x}/"] = capitulo.title
            x += 1


    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
          pelicula.mostrar()
          print("-"*50)

    def cargar_planetas(self):
        api = Apy()
        planetas_apy = api.get_planetas()
        for planeta in planetas_apy:
            objeto_planeta = Planeta.from_dict(planeta)
            nombre_episodios = []
            for episodio in objeto_planeta.episodios:
                nombre = self.dict_url_peliculas[episodio]
                nombre_episodios.append(nombre)
            
            objeto_planeta.episodios = nombre_episodios

            self.planetas.append(objeto_planeta)


    def mostrar_planetas(self):
        for planeta in self.planetas:
          planeta.mostrar()
          print("-"*50)



            
            

    

