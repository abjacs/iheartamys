from datetime import datetime
import urllib
from bs4 import BeautifulSoup
from model import location, city, flavorboard

class Api(object):
    HOME = "http://www.amysicecreams.com/"
    # TODO
    # hard-coding for now...
    CITIES = [ "http://www.amysicecreams.com/austin-stores/", "http://www.amysicecreams.com/houston/", "http://www.amysicecreams.com/san-antonio/" ]
    
    def __init__(self):
        flavors = { "ice cream" : [ "mexican vanilla", "cinammon", "chocolate"], "fruit ice" : [ "pineapple" ], "frozen yogurt" : [] }
        flavor_board = flavorboard.FlavorBoard(datetime.now(), flavors)
        arboretum = location.Location("Arboretum", flavor_board)
        
        locations = [ arboretum ]
        
        self.cities = { "Austin" : city.City("Austin", locations), "San Antonio" : city.City("San Antonio", []) }
        
    """
    def __init(self):
        # north austin
        arboretum = location.Location("Arboretum", None, url = "http://www.amysicecreams.com/arboretum")
        austinville_78750 = location.Location("Austinville 78750", None, url="http://www.amysicecreams.com/78750/")
        
        austin_locations = []
    """
    
    def get_cities(self):
        return self.cities
        
    def get_city(self, city_name):
        return self.cities.get(city_name, None)
        
    
if __name__ == "__main__":
    print "Dummy API example\n"
    
    api = Api()
    
    cities = api.get_cities()
    b = api.get_city("asdf")
    
    print b
    print
    
    city = cities["Austin"]
    
    for city in cities.values():
        print city.name
        
        for location in city.locations:
            print "\t" + location.name
        
            for (category, flavors) in location.flavor_board.flavors.iteritems():
                print "\t\t%s: %s" % (category, flavors)



#        
# example usage of api        
#
"""
from amys import api

amys = api.Api()

cities = amys.get_cities()
austin = amys.get_city("austin")

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
"""
        
        