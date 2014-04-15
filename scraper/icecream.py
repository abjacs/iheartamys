import urllib
import urlparse
from bs4 import BeautifulSoup

#
# TODO: abstract to support fro-yo and fruite ices
# TODO: note- pagination is optional and not *guaranteed* on any page
#

class IceCreamFlavorsScraper(object):

    @staticmethod
    def parse_ice_cream(url):
        ice_creams = []
        
        # a.journal-entry-navigation-current
        # <a class="journal-entry-navigation-current" href="/ice-creams/aztec-chocolate.html">Aztec&nbsp;Chocolate</a>
        
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)
        
        for ice_cream_link in soup.select("a.journal-entry-navigation-current"):
            (flavor, href) = (ice_cream_link.text, ice_cream_link.attrs.get("href", ""))
            href = urlparse.urljoin(url, href)
            
            print (flavor, href)
            ice_cream = IceCream(flavor, href)
            
            ice_creams.append(ice_cream)
        
        return ice_creams
    
    @staticmethod
    def parse(url):
        """
        <a class="paginationPageNumber"  href="/ice-creams/?currentPage=20" >20</a>
        """
        
        ice_creams = []

        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content)

        # last paginated page
        paginated_links = soup.select("a.paginationPageNumber")
        last_page_link = paginated_links[-1]
        last_page_num = last_page_link.text

        # use last link as template
        # strip off everything after equal sign
        # ex: /ice-creams/?currentPage=2
        relative_link = last_page_link.attrs["href"].replace(last_page_num, "")

        # cast to int
        last_page_num = int(last_page_num)

        first_page = int(paginated_links[0].text)
        last_page = int(last_page_link.text)

        # range(x, y) exposes set [x, y) so + 1 to expose set [x, y]
        for i in range(1, last_page + 1):
            url_fragment = relative_link + str(i)
            absolute_url = urlparse.urljoin(url, url_fragment)
            print absolute_url
            ice_creams_from_page = IceCreamFlavorsScraper.parse_ice_cream(absolute_url)
            
            ice_creams += ice_creams_from_page
            
        # only expose flavors
        ice_creams = [ice_cream.flavor for ice_cream in ice_creams]
        return ice_creams

class IceCream(object):
    def __init__(self, flavor, absolute_href):
        self.flavor = flavor
        self.href = absolute_href

if __name__ == "__main__":
    urls = [
        "http://www.amysicecreams.com/ice-creams/",
        "http://www.amysicecreams.com/froyo/",
        "http://www.amysicecreams.com/fruit-ices/"
    ]
    
    for url in urls:
        print IceCreamFlavorsScraper.parse(url)
