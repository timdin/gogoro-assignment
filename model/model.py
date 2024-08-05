# interface definition
import json

class dataModel():
    def __init__(self, raw_data):
        json_data = None
        if not isinstance(raw_data, dict):
            json_data = json.loads(raw_data)
        else:
            json_data = raw_data
        for key, value in json_data.items():
            setattr(self, key, value)

class dataModelList():
    def __init__(self, raw_data):
        self.rawdata = []
        json_data = None
        if not isinstance(raw_data, list):
            json_data = json.loads(raw_data)
        else:
            json_data = raw_data
        for single in json_data:
            self.rawdata.append(single)

    def __str__(self):
        return ", ".join(map(lambda x: x.__str__(), self.data))
    
    def sort(self, key, reverse=False):
        self.data.sort(key = lambda x: getattr(x, key), reverse=reverse)