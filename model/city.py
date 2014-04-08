import simplejson as json

class City(object):
    def __init__(self, name, locations):
        self.name = name
        self.locations = locations
        
    def as_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
