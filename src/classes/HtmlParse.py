from bs4 import BeautifulSoup

class HtmlParse:
    def __init__(self,html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def findAll(self, element):
        return self.soup.find_all(element)

    def findAll(self, element, attribute):
        for attr in self.soup.findAll(element):
            print(attr.get(attribute))