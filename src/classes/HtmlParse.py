from bs4 import BeautifulSoup

class HtmlParse:
    def __init__(self,html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def findAll(self, element, attribute=None):
        links = []
        list1 = self.soup.findAll(element)

        if list1:
            for attr in list1:
                if attr is not None:
                    if attribute is not None:
                        links.append(attr.get(attribute))
                    else:
                        links.append(attr)

        return links