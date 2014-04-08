from datetime import datetime
import simplejson as json


        
class FlavorBoard(object):
    def __init__(self, active_for_date, flavors):
        self.active_for = active_for_date
        
        self.flavors = flavors
        
        self.kinds = flavors.keys()
        
class Flavor(object):
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
class Location(object):
    def __init__(self, name, flavor_board):
        self.name = name
        
        self.flavor_board = flavor_board
        
class Api(object):
    url = "http://www.amysicecreams.com/"
    
    if __name__ == "__main__":
        print "Dummy API example"


#        
# example usage of api        
#
from amys import api

amys = api.Api()

cities = amys.get_cities()
austin = amys.get_location("austin")

for city in cities:
    print city.name # Austin
    print city.num_locations # 5
    
    for location in city.locations:
        # API #1
        print location.flavors # { "ice cream" : [ "mexican vanilla", "chocolate", "cinammon" ], "frozen yogurt" : [ "yellow belly" ] }
        print location.flavor_kinds # location.flavors.keys()
        
        
        # API #2
        print location.flavor_board.flavors
        print location.flavor_board.kinds # location.flavor_board.flavors.keys()
        print location.flavor_board.active_as_of
        
        # general location infomration
        print location.name # Arboretum
        print location.area # North Austin
        print location.address # 10000 Research Blvd, Ste. 140
        
        