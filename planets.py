class Planet:
    def __init__(self, name, diameter, orbital_period, rotation_period, gravity, population, climate, terrain, surface_water):
        self.name = name
        self.diameter = diameter
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.films = []
        self.characters = []

    @staticmethod
    def from_dict(data):
        planet = Planet(
            name=data['properties']['name'],
            diameter=data['properties'].get('diameter', 'N/A'),
            orbital_period=data['properties'].get('orbital_period', 'N/A'),
            rotation_period=data['properties'].get('rotation_period', 'N/A'),
            gravity=data['properties'].get('gravity', 'N/A'),
            population=data['properties'].get('population', 'N/A'),
            climate=data['properties'].get('climate', 'N/A'),
            terrain=data['properties'].get('terrain', 'N/A'),
            surface_water=data['properties'].get('surface_water', 'N/A')
        )
        planet.films = data['properties'].get('films', [])
        planet.characters = data['properties'].get('residents', [])
        return planet
