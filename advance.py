from client.swapi_client import swapiClient

from model.film import film, films
from model.vehicle import vehicles
from const.const import Category

client = swapiClient()

# 1. How many different species appears in film-6 (Revenge of the Sith) ?
film6 = film(client.get_single(Category.FILM, 6))
print(f"""How many different species appears in film-6 (Revenge of the Sith) ?
      {len(film6.get_species())}""")

# 2. List all the film names and sort the names by episode_id
film_list = films(client.get_list(Category.FILM, exhaustive=True))
film_list.sort(key = "episode_id")
print(f"""List all the film names and sort the names by episode_id
      {film_list}""")
# 3. Please find out all vehicles which max_atmosphering_speed is over 1000.
vehicle_list = vehicles(client.get_list(Category.VEHICLE, exhaustive=True))
vehicle_list.filter_by_speed(1000)
print(f"""List all the vehicles which max_atmosphering_speed is over 1000
      {vehicle_list}""")
