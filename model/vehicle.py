# dataModel impl for vehicles
from model.model import dataModel, dataModelList

class vehicle(dataModel):
    def get_name(self):
        return self.name
    
    def get_atmosphering_speed(self):
        try:
            return int(self.max_atmosphering_speed)
        except:
            return 0

    def __str__(self):
        return f"name: {self.get_name()} - speed: {self.get_atmosphering_speed()}"
    
        
class vehicles(dataModelList):
    def __init__(self, raw_data):
        self.data = []
        super().__init__(raw_data)
        for single in self.rawdata:
            self.data.append(vehicle(single))

    def filter_by_speed(self, speed: int):
        self.data = list(filter(lambda x: x if x.get_atmosphering_speed()>speed else None, self.data))
