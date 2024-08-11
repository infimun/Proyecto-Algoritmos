import requests
from swapi_client import SWAPIClient
from models.movie import Movie
from models.species import Species
from models.planet import Planet


def listar_peliculas():
    movies_data = SWAPIClient.get_movies()
    movies = [Movie.from_dict(movie) for movie in movies_data]
    for movie in movies:
        print(f'\nTítulo: {movie.title}')
        print(f'Episodio: {movie.episode_id}')
        print(f'Fecha de lanzamiento: {movie.release_date}')
        print(f'Director: {movie.director}')
        print(f'Introducción: {movie.opening_crawl}')
        print('-'*70)

        listar_peliculas()
            