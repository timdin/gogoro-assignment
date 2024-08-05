# dataModel impl for vehicles
from model.model import dataModel, dataModelList

class film(dataModel):
    def get_name(self):
        return self.title
    
    def get_species(self):
        return self.species
    
    def get_id(self):
        return self.episode_id

    def __str__(self):
        return f"title: {self.get_name()} - id: {self.get_id()}"
    
class films(dataModelList):
    def __init__(self, raw_data):
        self.data = []
        super().__init__(raw_data)
        for single in self.rawdata:
            self.data.append(film(single))
