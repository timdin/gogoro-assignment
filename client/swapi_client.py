"""This is the default client for the swapi service."""

import json
import requests
from const.const import Category

# this is the basic client for the swapi service
class swapiClient():
    def __init__(self):
        self.base_url = "https://swapi.py4e.com/api"
        self.timeout = 10

    def get_single(self, category:Category, item_id) -> str:
        """
        function call for getting a single item under the given category with item_id
        """
        res = requests.get(f"{self.base_url}/{category.value}/{item_id}", timeout=self.timeout)
        return res.text
    def get_list(self, category:Category, page=0, exhaustive=False) -> str:
        """
        function call for getting list with the given page
        if exhaustive = True, then the function will retrieve all results regardless of the page
        """
        if exhaustive:
            data_list = []
            next_url = f"{self.base_url}/{category.value}"
            while next_url:
                res = requests.get(next_url, timeout=self.timeout)
                body = res.json()
                data_list.extend(body["results"])
                next_url = body["next"]
            return json.dumps(data_list)
        res = requests.get(f"{self.base_url}/{category.value}/?page={page}", timeout=self.timeout)
        return json.dumps(res.json()["results"])



if __name__ == "__main__":
    c = swapiClient()
    