"""basic script level approach"""

import requests

BASE_URL = "https://swapi.py4e.com/api/"
DEFAULT_TIMEOUT = 10
FILM_URL = BASE_URL + "films/"
VEHICLE_URL = BASE_URL + "vehicles/"

# 1. How many different species appears in film-6 (Revenge of the Sith) ?

res = requests.get(FILM_URL + "6", timeout=DEFAULT_TIMEOUT)
body = res.json()

print(f"How many different species appears in film-6 (Revenge of the Sith)?\n It was: {len(body["species"])}")

# 2. List all the film names and sort the names by episode_id
res = requests.get(FILM_URL, timeout=DEFAULT_TIMEOUT)
body = res.json()
films = body["results"]
films.sort(key=lambda x : x["episode_id"])
sortedNames = list(map(lambda x: x["title"], films))
print(f"Please list all the film names and sort the name by episode_id\n It was: {sortedNames}")

# 3. Please find out all vehicles which max_atmosphering_speed is over 1000.
res = requests.get(VEHICLE_URL, timeout = DEFAULT_TIMEOUT)
body = res.json()
vehicles = body["results"]
qualifiedVehicles = list(filter(lambda x : x["name"] if int(x
["max_atmosphering_speed"]) > 1000 else None, vehicles))
filteredNames = list(map(lambda x: x["name"], qualifiedVehicles))
print(f"""Please find out all vehicles which max_atmosphering_speed is over 1000.
 It was: {filteredNames}""")
