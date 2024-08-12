#No sirve por ahora...


"""import requests
from models.planet import Planet

armas = [
    "Bastones Gaffi",
    "Batería de Energía",
    "Blaster",
    "Bowcaster",
    "Buscador (Seeker)",
    "Cañón de iones",
    "Cañón láser",
    "Cesta gungan",
    "Dardo sable kaminiano",
    "Detonadores Térmicos",
    "Electro-Jabber",
    "Eletro-bastón gungan",
    "Gaderffii",
    "Lightsaber",
    "Mísiles de concusión",
    "Plataforma de Armas Orbital",
    "Pistola blaster BlasTech DH-44",
    "Pistolas blasters de Naboo",
    "Pistola Blaster Merr-Sonn modelo 44",
    "Pistola blaster Pesada BlasTech DL-44",
    "Quarrel",
    "Rifle blaster Blastech E-11 (Rifle de Stormtrooper)",
    "Rifle de Battle Droid",
    "Torpedo de protones",
    "Torreta de anti-infanteria DF .9",
    "Turboláser",
    ]

class Mision:
    def __init__(self, name, planeta, nave, armas, integrantes ) -> None:
        self.name = name
        self.planeta = planeta
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes
        if not name:
            raise ValueError
      


def get_mision():
    while True:
        try:
            name= input("Nombre de la mision")
            return name 
                
        except ValueError:
            print("No se introdujo nombre")
        else:
            break
    print(name)
    
  
    



def crear_mision():
    pass


get_mision()

        

"""