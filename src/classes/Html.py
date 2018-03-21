from classes.Url import Url
import urllib.request

class Html:
    def __init__(self,url):
        if isinstance(url,Url):
            self.url = url
        else:
            raise ValueError('wrong type give, URL object required')

    #lets perform a get on the url
    def get(self):
        try:
            u = urllib.request.urlopen(self.url.get_url())
            return u.read()
        except:
            pass