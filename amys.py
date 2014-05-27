from datetime import datetime
import urllib
from bs4 import BeautifulSoup
from model import location, city, flavorboard
from scraper import flavorboard as board_scraper
from scraper import flavors as flavors_scraper


class Api(object):
    HOME = "http://www.amysicecreams.com/"
        
    CITIES = {
        "Austin" : { 
            "Arboretum" : "http://www.amysicecreams.com/arboretum-flavor-board/", 
            "Austinville 78750" : "http://www.amysicecreams.com/austinvill-78750-flavor-board/", 
            "Burnet" : "http://www.amysicecreams.com/burnet-rd-flavor-board/", 
            "6th Street" : "http://www.amysicecreams.com/6th-street-flavor-board/", 
            "Guad" : "http://www.amysicecreams.com/the-guad-flavor-board/",
            "SoCo" : "http://www.amysicecreams.com/soco-flavor-board/", 
            "Airport" : "http://www.amysicecreams.com/airport-flavor-board/", 
            "Austinville 78704" : "http://www.amysicecreams.com/south-austinville-flavor-board/", 
            "Super South" : "http://www.amysicecreams.com/super-south-flavor-board/", 
            "The Grove" : "http://www.amysicecreams.com/the-grove-flavor-board/", 
            "Westgate" : "http://www.amysicecreams.com/westgateflavors", 
            "Hill Country Galleria" : "http://www.amysicecreams.com/hill-country-galleria-flavor-b/",
            # TODO: this does not parse...
            "Mira Vista" : "http://www.amysicecreams.com/mira-vista-flavor-board/" 
        }, 
    
        "San Antonio" : {}, 
    
        "Houston" : {}
    }
    
    FLAVORS = {
        "ice cream" : "http://www.amysicecreams.com/ice-creams/",
        "frozen yogurt" : "http://www.amysicecreams.com/froyo/",
        "fruit ice" : "http://www.amysicecreams.com/fruit-ices/"
    }
    
    def __init__(self):
        self.cities = {}
        
        #"""          
        for city_name in Api.CITIES:
            print "%s" % city_name
            locations = []
        
            for (location_name, flavor_url) in Api.CITIES[city_name].iteritems():
                flavors = board_scraper.FlavorBoardScraper.parse(flavor_url)
            
                # TODO: parse active_date isntead of using now()
                flavor_board = flavorboard.FlavorBoard(datetime.now(), flavors)
                curr_location = location.Location(location_name, flavor_board)
            
                locations.append(curr_location)
            self.cities.update({ city_name : city.City(city_name, locations) })
        #"""
    
    def get_cities(self):
        cities = sorted(self.CITIES.keys())
        
        return cities
        
    def get_city(self, city_name):
        return self.cities.get(city_name, {})
        
    def get_flavors(self, flavors = [ ]):
        flavors_with_url = {}
        
        # default to self.Flavors
        if (not flavors):
            flavors = self.FLAVORS.keys()
        
        for flavor in flavors:
            (flavor, url) = flavor, self.FLAVORS.get(flavor, "")
            # ternary: a if test else b
            flavors_with_url[flavor] = ( flavors_scraper.FlavorScraper.parse(url) if url else [] )
            
        return flavors_with_url
        
    def get_flavors_for_location(self, city, location):
        city = self.FLAVORS.get(city, {})
        
    
if __name__ == "__main__":
    print "Dummy API example\n"
    
    api = Api()    
    
    cities = api.get_cities()
    
    city = api.get_city("Austin")
    
    # city struture example
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
        
        