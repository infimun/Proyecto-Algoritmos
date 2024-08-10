import requests
import json

class Movie:
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director


    def from_dict(data):
        return Movie(
            title=data['title'],
            episode_id=data['episode_id'],
            release_date=data['release_date'],
            opening_crawl=data['opening_crawl'],
            director=data['director']
        )

    def mostrar(self):
        print(f"{self.title}, {self.episode_id}, {self.release_date}, {self.opening_crawl}, {self.director}")

class Planeta:
    def __init__(self, nombre, orbita, rotacion, habitantes, clima, episodios, personajes) -> None:
        self.nombre = nombre
        self.orbita = orbita
        self.rotacion = rotacion
        self.habitantes = habitantes
        self.clima = clima
        self.episodios = episodios
        self.personajes = personajes

    def from_dict(data):
        return Planeta(
            nombre=data['name'],
            orbita=['orbital_period'],
            rotacion=['rotation_period'],
            habitantes=data['population'],
            clima=data['climate'],
            episodios=data['films'],
            personajes=data['residents'],
        )

    
    def mostrar(self):
        print(f"{self.nombre}, {self.episodios}")