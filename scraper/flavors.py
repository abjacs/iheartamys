import urllib
import urlparse
from bs4 import BeautifulSoup

#
# TODO: abstract to support fro-yo and fruite ices
# TODO: note- pagination is optional and not *guaranteed* on any page
#

class FlavorScraper(object):
    
    """
    def __init__(self, url):
        self.url = url
        
        self.flavor_page_links = self.__find_flavor_pages(url)
    """
    
    @staticmethod
    def __find_flavor_pages(url):
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
            
            # use first link as template
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
    
    def parse_ice_cream(url):
        flavors = []
        
        # a.journal-entry-navigation-current
        # <a class="journal-entry-navigation-current" href="/ice-creams/aztec-chocolate.html">Aztec&nbsp;Chocolate</a>
        
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        for ice_cream_link in soup.select("a.journal-entry-navigation-current"):
            (flavor, href) = (ice_cream_link.text, ice_cream_link.attrs.get("href", ""))
            href = urlparse.urljoin(url, href)
            
            print (flavor, href)
            ice_cream = IceCream(flavor, href)
            
            flavors.append(ice_cream)
        
        return flavors
    
    def parse(url):
        """
        <a class="paginationPageNumber"  href="/ice-creams/?currentPage=20" >20</a>
        """
        
        flavors = []

        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        # default to first page as last page
        last_page = 1
        relative_link = ""
        
        # check for pagination
        paginated_links = soup.select("a.paginationPageNumber")
        if(len(paginated_links) > 0):    
            # last paginated page
            last_page_link = paginated_links[-1]
            last_page = int(last_page_link.text)
        
            # use first link as template
            # strip off everything after equal sign
            # ex: /ice-creams/?currentPage=2
            relative_link = last_page_link.attrs["href"].replace(last_page_link.text, "")

        # range(x, y) exposes set [x, y) so + 1 to for y-inclusive set [x, y]
        for i in range(1, last_page + 1):
            url_fragment = relative_link + str(i)
            absolute_url = urlparse.urljoin(url, url_fragment)
            print absolute_url
            flavors_from_page = FlavorScraper.parse_ice_cream(absolute_url)
            
            flavors += flavors_from_page
            
        # only expose flavors
        flavors = [ice_cream.flavor for ice_cream in flavors]
        return flavors
        
    

class IceCream(object):
    def __init__(self, flavor, absolute_href):
        self.flavor = flavor
        self.href = absolute_href

if __name__ == "__main__":
    flavor_scraper = FlavorScraper()
    
    urls = [
        "http://www.amysicecreams.com/ice-creams/",
        "http://www.amysicecreams.com/froyo/",
        "http://www.amysicecreams.com/fruit-ices/"
    ]
    
    for url in urls:
        print url
        print FlavorScraper.find_flavor_pages(url)
        print
