# enumerate for category
from enum import Enum

class Category(str, Enum):
    # enumerate for categories
    FILM = "films"
    VEHICLE = "vehicles"

if __name__ == '__main__':
    print(Category.FILM.value)