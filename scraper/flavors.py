import urllib
import urlparse
from bs4 import BeautifulSoup


class Flavor(object):
    def __init__(self, flavor, absolute_href):
        self.flavor = flavor
        self.href = absolute_href

class FlavorScraper(object):
    
    @staticmethod
    def parse(url):
        flavors = []
        
        flavor_urls = FlavorScraper.__find_flavors_urls(url)
        for flavor_url in flavor_urls:
            flavors_from_page = FlavorScraper.parse_flavors(flavor_url)
            flavors += flavors_from_page
            
        # only expose flavors
        flavors = [ice_cream.flavor for ice_cream in flavors]
        return flavors
    
    @staticmethod
    def __find_flavors_urls(url):
        flavor_urls = []
        
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        # MARKUP: <a class="paginationPageNumber"  href="/ice-creams/?currentPage=20" >20</a>        
        paginated_links = soup.select("a.paginationPageNumber")
        if(len(paginated_links) > 0):
            # last paginated page
            last_page_link = paginated_links[-1]
            
            start = int(paginated_links[0].text)
            end = int(last_page_link.text)
            
            # use last link as template
            # strip off everything after equal sign
            # ex: /ice-creams/?currentPage=2
            relative_link = last_page_link.attrs["href"].replace(last_page_link.text, "")
            
            # range(x, y) exposes set [x, y) so + 1 to for y-inclusive set [x, y]
            for i in range(start, end + 1):
                url_fragment = relative_link + str(i)
                absolute_url = urlparse.urljoin(url, url_fragment)
                print absolute_url
                
                flavor_urls.append(absolute_url)
        else:
            # no pagination
            flavor_urls = [ url ]
                
        return flavor_urls  
    
    @staticmethod
    def parse_flavors(url):
        flavors = []
        
        # MARKUP: a.journal-entry-navigation-current
        # MARKUP: <a class="journal-entry-navigation-current" href="/ice-creams/aztec-chocolate.html">Aztec&nbsp;Chocolate</a>
        
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        for ice_cream_link in soup.select("a.journal-entry-navigation-current"):
            (flavor, href) = (ice_cream_link.text, ice_cream_link.attrs.get("href", ""))
            href = urlparse.urljoin(url, href)
            
            flavor = Flavor(flavor, href)
            flavors.append(flavor)
        
        return flavors

if __name__ == "__main__":
    flavor_scraper = FlavorScraper()
    
    urls = [
        "http://www.amysicecreams.com/ice-creams/",
        "http://www.amysicecreams.com/froyo/",
        "http://www.amysicecreams.com/fruit-ices/"
    ]
    
    for url in urls:
        print url
        print FlavorScraper.parse(url)
        print
