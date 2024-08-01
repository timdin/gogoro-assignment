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
# exhaustive retrival of vehicle
vehicles = []
next_url = VEHICLE_URL
while next_url:
    res = requests.get(next_url, timeout = DEFAULT_TIMEOUT)
    body = res.json()
    vehicles.extend(body["results"])
    next_url = body["next"]

# since there are non-digit strings exists in the response, avoid the lambda solution
# qualifiedVehicles = list(
#     filter(
#         lambda x : x["name"] if int(x["max_atmosphering_speed"]) > 1000 else None, vehicles
#         )
#     )
# filteredNames = list(map(lambda x: x["name"], qualifiedVehicles))

filteredNames = []
for vehicle in vehicles:
    try:
        if int(vehicle["max_atmosphering_speed"])>=1000:
            filteredNames.append(vehicle["name"])
    except ValueError:
        # only catch value error here, since we are only suppressing the non-digit strings casting
        continue

print(f"""Please find out all vehicles which max_atmosphering_speed is over 1000.
 It was: {filteredNames}""")
