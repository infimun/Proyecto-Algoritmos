#crear clase peliculas y su modelo para informacion 
import requests
from swapi_client import SWAPIClient

class Movie:
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

    @staticmethod
    def from_dict(data):
        return Movie(
            title=data['properties']['title'],
            episode_id=data['properties']['episode_id'],
            release_date=data['properties']['release_date'],
            opening_crawl=data['properties']['opening_crawl'],
            director=data['properties']['director']
        )

