import urllib
from bs4 import BeautifulSoup

class FlavorBoardScraper(object):
    def parse(self, url):
        """
        div#body # container
        
        h2 title # category
        child ul # flavors
        """

        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        # container
        container = soup.find("div#body")
        
        # category
        categories = container.find_all("h2")
        
        for category in categories:
            # category name
            # flavors
            continue

if __name__ == "__main__":
    url = "http://www.amysicecreams.com/burnet-rd-flavor-board/"
    
    flavors = {}
    
    content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content)
    
    # container
    container = soup.select("div#body")[0]
    
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
        
        print flavors