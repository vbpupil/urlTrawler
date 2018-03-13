from classes.url import Url
import urllib.request

class Html:
    def __init__(self,url):
        if isinstance(url,Url):
            self.url = url
        else:
            raise ValueError('wrong type give, URL required')

    #lets perform a get on the url
    def get(self):
        try:
            u = urllib.urlopen(self.url.getUrl())
        except:
            u = urllib.request.urlopen(self.url.getUrl())

        return u.read()
