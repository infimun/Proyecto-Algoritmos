#prueba para las especies

class Species:
    def __init__(self, name, classification, designation, average_height, skin_colors, hair_colors, eye_colors, average_lifespan, homeworld_url, language):
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.skin_colors = skin_colors
        self.hair_colors = hair_colors
        self.eye_colors = eye_colors
        self.average_lifespan = average_lifespan
        self.homeworld_url = homeworld_url
        self.homeworld_name = None  # Nuevo atributo para almacenar el nombre del planeta
        self.language = language

    @staticmethod
    def from_dict(data):
        species = Species(
            name=data['properties']['name'],
            classification=data['properties']['classification'],
            designation=data['properties']['designation'],
            average_height=data['properties']['average_height'],
            skin_colors=data['properties']['skin_colors'],
            hair_colors=data['properties']['hair_colors'],
            eye_colors=data['properties']['eye_colors'],
            average_lifespan=data['properties']['average_lifespan'],
            homeworld_url=data['properties']['homeworld'],
            language=data['properties']['language']
        )
<<<<<<< HEAD
        return species
=======
        return species
>>>>>>> 9663ed376413ad22da1023fdd523cfd60e597e82
