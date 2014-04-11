import urllib
from bs4 import BeautifulSoup

class FlavorBoardScraper(object):
    
    @staticmethod
    def parse(url):
        """
        div#body # container
        
        h2 title # category
        child ul # flavors
        """
        
        print url
        flavors = {}
    
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
    
        # container
        container = soup.select("div.body")[0]
    
        # category
        categories = container.find_all("h2")
    
        for category_tag in categories:
            category = category_tag.text
            # flavors
            flavor_ul = category_tag.find_next("ul")
            flavor_list_items = flavor_ul.find_all("li")
    
            # TODO: strip out empty values
            flavor_list = [ flavor.text for flavor in flavor_list_items ]
            flavors[category] = flavor_list
            
        return flavors

if __name__ == "__main__":
    url = "http://www.amysicecreams.com/burnet-rd-flavor-board/"
    
    print FlavorBoardScraper.parse(url)
    
